from django.contrib.auth import authenticate, login, logout
from .forms import RegisterForm, LoginForm, ToppingsForm
from .models import Topping, Pizza_Assembly, Pizza_Type, Pizza, Order, Size, Option, Salad, Pasta, Item, Dinner_Plate_Type
from django.shortcuts import render
from django.shortcuts import redirect
from decimal import Decimal
from django.contrib import messages

def index(request):


    # Get all collections needed to display menu
    pizzas = Pizza.objects.all()
    toppings = Topping.objects.all()
    sizes = Size.objects.all()
    types = Pizza_Type.objects.all()
    options = Option.objects.all()
    salads = Salad.objects.all()
    pastas = Pasta.objects.all()
    items = Item.objects.all()
    plates = Dinner_Plate_Type.objects.all()

    # Pass all collections to the index page
    return render(request, 'index.html', {'pizzas': pizzas, 'toppings': toppings, 'sizes': sizes, 'types': types,
                                          'options': options, 'salads': salads, 'pastas': pastas, 'items': items,
                                          'plates': plates })

def exit(request):

    # Logout current user and redirect to the menu
    logout(request)
    return redirect("/")

def enter(request):

    # Create form from the request
    form = LoginForm(request.POST or None)

    # If form is valid extract data
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']

        # Try to authenticate the user
        user = authenticate(username=username, password=password)

        # If user exists but not in the active state return an error
        # If user does not exist return and error
        # Otherwise login the user
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect("/")
            else:
                messages.error(request, "User is not active !!!")
        else:
            messages.error(request, "Incorrect user login !!!")

    return render(request, 'login.html', {'form': form})


def register(request):

    # Create form from the request
    form = RegisterForm(request.POST or None)

    # If form is valid extract data and save the user in the database
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)

        # If user is not found return all the error encountered during registration
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            messages.error(request, form.errors)
    else:
        messages.error(request, form.errors)

    return render(request, 'register.html', {'form': form})

def process_order(request, id, item):

    # If user is not authenticated redirect them to the login page
    if not request.user.is_authenticated:
        return render(request, 'login.html')
    else:
        if request.method == "POST":

            # Retrieve and order from the data base that has not been completed. It is impossible to have more than
            # one uncompleted order for the same user
            order = Order.objects.filter(customer=request.user.id, is_paid=False).first()

            # If order does not exist it must be new order
            if order is None:
                order = Order()
                order.customer = request.user
                order.is_complete = False
                order.is_paid = False
                order.save()

            # Check to see what is being ordered
            if item == "pizza":

                pizza = Pizza.objects.get(pk=id)
                toppings = Topping.objects.filter(description__in=request.POST.getlist('toppings'))

                if pizza.option.number_of_topings != len(request.POST.getlist('toppings')):
                    form = ToppingsForm()
                    return render(request, 'cart.html', {'error': 'Number of selected topics does not match choice of Pizza',
                                                         'pizza': pizza, 'form': form })

                # Looks like user is ordering pizza
                pizza_assembly = Pizza_Assembly()
                pizza_assembly.pizza = pizza
                pizza_assembly.save()
                pizza_assembly.toppings.add(*list(toppings))
                pizza_assembly.save()


                order.pizzas_assemblies.add(pizza_assembly)
                order.total = Decimal(order.total) + pizza.price
                order.save()

            elif item == "salad":

                # Looks like user is ordering salad
                salad = Salad.objects.get(pk=id)
                order.salads.add(salad)
                order.total = Decimal(order.total) + salad.price
                order.save()

            elif item == "pasta":

                # Looks like user is ordering pasta
                pasta = Pasta.objects.get(pk=id)
                order.pastas.add(pasta)
                order.total = Decimal(order.total) + pasta.price
                order.save()

            elif item == "plate":

                # Looks like user is ordering dinner plate
                plate = Item.objects.get(pk=id)
                order.dinner_plates.add(plate)
                order.total = Decimal(order.total) + plate.price
                order.save()

            return render(request, 'order.html', {'order': order})

        elif request.method == "GET":

            # if user is ordering pizza display toppings sellection form
            if item == "pizza":
                form = ToppingsForm()
                pizza = Pizza.objects.get(pk=id)

                return render(request, 'cart.html', {'pizza': pizza, 'form': form})

            elif item == "salad":
                salad = Salad.objects.get(pk=id)

                return render(request, 'cart.html', {'salad': salad })

            elif item == "pasta":
                pasta = Pasta.objects.get(pk=id)

                return render(request, 'cart.html', {'pasta': pasta })

            elif item == "plate":
                plate = Item.objects.get(pk=id)

                return render(request, 'cart.html', {'plate': plate })

            else:
                return redirect("/")

def process_cart(request, order_id):

    # If user is not authenticated redirect them to the login page
    if not request.user.is_authenticated:
        return render(request, 'login.html')
    else:
        if request.method == "POST":

            # Looks like user is trying to pay for the order
            order = Order.objects.get(pk=order_id)
            order.is_paid = True
            order.save()

            return redirect("/")

        elif request.method == "GET":

            # Looks like user is trying to see what's in the cart
            if order_id is not '0':
                # If order id is passed fetch it, otherwise get first order for the user that has not been paid
                order = Order.objects.get(pk=order_id)
            else:
                order = Order.objects.filter(customer=request.user.id, is_paid=False).first()

            if order is None:
                return render(request, 'order.html', {'error': 'There are currently no active orders in the cart !!!'})
            else:
                return render(request, 'order.html', {'order': order})

def clear_cart(request):

    # If user is not authenticated redirect them to the login page
    if not request.user.is_authenticated:
        return render(request, 'login.html')
    else:
        if request.method == "POST":

            # Looks like user is trying to start over. Let's delete first incomplete order
            order = Order.objects.filter(customer=request.user.id, is_paid=False).first()
            if order is not None:
                order.delete()

            return redirect("/")


def display_orders(request):

    # If user is not authenticated redirect them to the login page
    if not request.user.is_authenticated:
        return render(request, 'login.html')
    else:

        # Fetch all the paid orders for a given user
        orders = Order.objects.filter(customer=request.user.id, is_paid=True).all()

        if len(orders) == 0:
            return render(request, 'order_list.html',
                          {'error': 'You have no orders !!!'})
        else:
            return render(request, 'order_list.html', {'orders': orders})
