from django.contrib import admin

from main.models import Publisher, Book, Order, OrderItems


class OrderItemsInline(admin.TabularInline):
    model = OrderItems
    extra = 3


class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemsInline]

admin.site.register(Publisher)
admin.site.register(Book)
admin.site.register(Order, OrderAdmin)