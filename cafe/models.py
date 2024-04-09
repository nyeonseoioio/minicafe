from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('cafe/category_detail', args = (self.id , ))

class Menu(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    slug = models.SlugField()
    menu_name = models.CharField(verbose_name = 'TITLE',max_length=100)
    price = models.IntegerField()
    explain = models.CharField(max_length=100)
    temperature_choices = [
        ('ICE', 'Ice'),
        ('HOT', 'Hot'),
    ]
    # class Meta:
    #     verbose_name = 'menu'
    #     verbose_name_plural = 'menus'
    #     db_table = 'cafe_menus'

    def __str__(self):
        return self.menu_name
    
    def get_absolute_url(self):
        return reverse('cafe:category_detail', args=[str(self.id)])

class Order(models.Model):
    menu = models.ForeignKey(Menu, on_delete = models.CASCADE)
    order_time = models.DateTimeField(auto_now_add=True)
    # 정수가 될 수 없는 필드
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.quantity
    


class Payment(models.Model):
    order = models.ForeignKey(Order, on_delete= models.CASCADE)
    payment_time = models.DateTimeField(auto_now_add = True)
    payment_method = models.CharField(max_length=50)
    payment_amount = models.IntegerField() 

    def __str__(self):
        return self.payment_amount