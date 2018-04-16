from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Size(models.Model):
    description = models.CharField(max_length=5)

    def __unicode__(self):
	    return self.description

class Topping(models.Model):
    description = models.CharField(max_length=24)

    def __unicode__(self):
	    return self.description

class Option(models.Model):
    description = models.CharField(max_length=24)
    number_of_topings = models.IntegerField(default=0)

    def __unicode__(self):
        return self.description

class Pizza_Type(models.Model):
    description = models.CharField(max_length=24)

    def __unicode__(self):
        return self.description

class Dinner_Plate_Type(models.Model):
    description = models.CharField(max_length=24)

    def __unicode__(self):
        return self.description

class Pizza(models.Model):

    type = models.ForeignKey(Pizza_Type, null=True, on_delete=models.SET_NULL)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    size = models.ForeignKey(Size, null=True, on_delete=models.SET_NULL)
    option = models.ForeignKey(Option, null=True, on_delete=models.SET_NULL)

    def __unicode__(self):
        return str(self.id)

class Pasta(models.Model):

    description = models.CharField(max_length=24)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)

    def __unicode__(self):
        return str(self.id)

class Salad(models.Model):

    description = models.CharField(max_length=24)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)

    def __unicode__(self):
        return str(self.id)

class Item(models.Model):

    type = models.ForeignKey(Dinner_Plate_Type, null=True, on_delete=models.SET_NULL)
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0.00)
    size = models.ForeignKey(Size, null=False, on_delete=models.PROTECT)

    def __unicode__(self):
        return str(self.id)


class Pizza_Assembly (models.Model):

    pizza = models.ForeignKey(Pizza, null=False, on_delete=models.PROTECT)
    toppings = models.ManyToManyField(Topping)

    def __unicode__(self):
        return str(self.id)

class Order(models.Model):

    customer = models.ForeignKey(User, null=False, on_delete=models.PROTECT)
    create_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)
    pizzas_assemblies = models.ManyToManyField(Pizza_Assembly)
    dinner_plates = models.ManyToManyField(Item)
    salads = models.ManyToManyField(Salad)
    pastas = models.ManyToManyField(Pasta)
    is_complete = models.BooleanField(default=False)
    is_paid = models.BooleanField(default=False)
    total = models.DecimalField(max_digits=6,decimal_places=2,default=0.00)

    def __unicode__(self):
        return str(self.id)
