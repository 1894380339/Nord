from cgi import print_exception
from pickle import TRUE
from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(default='', max_length=200)
    slug = models.CharField(default='',max_length=100)
    description = models.TextField(default='')
    active = models.BooleanField(default=True)
    def __str__(self):
        return self.title
class Product(models.Model):
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    title = models.CharField(default='', max_length=200)
    img_product = models.ImageField(null=True, blank=True)
    description = models.TextField(default='')
    price = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    def __str__(self):
        return f'id: {str(self.id)} {self.title}'
    @property
    def imageURL(self):
        try:
            url = self.img_product.url
        except:
            url=''
        return url
        

class Variation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(default='', max_length=200)
    price = models.IntegerField(default=0)
    sale_price = models.IntegerField(default=0)
    inventory = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
    def __str__(self):
        return f'id:{self.id} - {self.product}'