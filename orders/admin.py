from django.contrib import admin

# Register your models here.

from orders.models import Size, Topping, Pizza, Pizza_Type, Option, Order, Pizza_Assembly, Pasta, Item, Salad, Dinner_Plate_Type

admin.site.register(Pizza_Type)
admin.site.register(Size)
admin.site.register(Topping)
admin.site.register(Pizza)
admin.site.register(Option)
admin.site.register(Pasta)
admin.site.register(Item)
admin.site.register(Salad)
admin.site.register(Pizza_Assembly)
admin.site.register(Dinner_Plate_Type)

class OrderAdmin(admin.ModelAdmin):

    list_display = ['id', 'customer', 'is_complete', 'is_paid', 'update_date', 'total']
    list_editable = ['is_complete']

admin.site.register(Order,OrderAdmin)



