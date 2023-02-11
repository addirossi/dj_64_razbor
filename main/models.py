from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=50)

    objects = models.Manager()

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE, related_name='books')
    year = models.PositiveSmallIntegerField()

    objects = models.Manager()

    def __str__(self):
        return self.title


class Order(models.Model):
    address = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    books = models.ManyToManyField(Book, through='OrderItems')

    objects = models.Manager()

    def __str__(self):
        return f'Заказ № {self.id}'


class OrderItems(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    book = models.ForeignKey(Book, on_delete=models.RESTRICT)
    quantity = models.PositiveSmallIntegerField(default=1)
