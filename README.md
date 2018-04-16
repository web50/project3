# Project 3

Web Programming with Python and JavaScript

# Created by Sergey L. Sundukovskiy

<h3>File Content</h3>

<h4>forms.py</h4>

Contains definition of all the forms (RegisterForm, LoginForm, ToppingsForm)

<h4>db.sqlite3</h4>

Contains database for the entire assignment

<h4>admin.py</h4>

Contains registration of all the model object with django admin and
custom definition for OrderAdmin. To allow admin (sergey) with password (galaug01) to
see all the orders that have been placed and modify order status. It fulfills 
Viewing Orders and Personal Touch requirement of the assignment allowing site 
administrators to mark orders as complete. It also fulfills Adding Items 
requirement of the assignment 

<h4>models.py</h4>

Contains contains definition and relationship between model objects representing 
(Pizza, Toppings, Order, Salad, Dinner Plate, Pasta )

<h4>urls.py</h4>

Contains contains definition of all  the applications routes

<h4>views.py</h4>

Contains contains main code of the application. Among many other things it fulfills 
Logout requirement of the assignment  

<h4>login.html</h4>

Contains a Login form. It fulfills Login requirement of the assignment 

<h4>register.html</h4>

Contains a Registration form. It fulfills Registration requirement of the assignment 

<h4>index.html</h4>

Contains html and python code for displaying Restaurant Menu. It fulfills 
Menu requirement of the assignment 

<h4>visitor.html</h4>

Contains html and python code for displaying navigation menu of the application

<h4>cart.html</h4>

Contains html and python code for displaying and adding items added to cart. It fulfills 
Shopping Cart requirement of the assignment 

<h4>order.html</h4>

Contains html and python code for placing orders. It fulfills Placing an Order 
requirement of the assignment 

<h4>order_list.html</h4>

Contains html and python code for displaying placed orders for a particular user. 
It fulfills Personal Touch requirement of the assignment, allowing site administrators 
to mark orders as complete and allowing users to see the status of their pending 
or completed orders 

<h3>Short Description</h3>

Initial project implementation only handled placing orders containing 
Pizza and Pizza Toppings. Subsequent implementation added support for placing orders for
Dinner Plates, Salads and Pastas

<h4>Special Pizza requires 5 toppings</h4> 

<h4>Admin username is 'sergey' password 'galaug01'</h4> 

