from django.db import models
from user.models import CustomerUser
from cart.models import Cart
# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(CustomerUser, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    shiping_address = models.CharField(default='', max_length=255)
    order_decription = models.TextField(default='')
    # subtotal =models.FloatField(default=0)
    phone = models.CharField(null= True, max_length=255)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return str(self.id)
    