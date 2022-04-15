from django.db import models

# Create your models here.
from django.db import models
from product.models import Variation, Product
from user.models import CustomerUser
# Create your models here.
class Cart(models.Model):
    user = models.ForeignKey(CustomerUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)
    def get_cart_total(self):
        cartitem =  self.cartitem_set.all()
        total = sum([item.get_total for item in cartitem])
        return total
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    item = models.ForeignKey(Variation, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    def __str__(self):
        return f'cart_id:{self.cart}'
    @property
    def get_total(self):
        total = self.quantity * self.product.price
        return total