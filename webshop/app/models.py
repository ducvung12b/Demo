from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Create your models here.

#Form register
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','password1','password2']


class Product(models.Model):
    name = models.CharField(max_length=200,null =True)
    price = models.IntegerField()
    hot = models.IntegerField()
    describe = models.CharField(max_length=400,null=True)
    image = models.ImageField(null=True,blank=True)
    def __str__(self):
        return self.name
    #No Image
    @property
    def ImageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


class Order(models.Model):
    customer = models.ForeignKey(User,on_delete=models.SET_NULL,blank =True,null =True)
    date_order = models.DateField(auto_now_add=True)
    complete = models.BooleanField(default=False,null=True,blank = False)
    transaction_id = models.CharField(max_length=200,null = True)
    def __str__(self):
        return str(self.id)
    
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total
    
class OrderItem(models.Model):
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,blank =True,null =True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,blank =True,null =True)
    quantity = models.IntegerField(default=0,null=True,blank=True)
    date_added = models.DateField(auto_now_add=True)
    @property
    def get_total(self):
        total = self.product.price*self.quantity
        return total


class ShippingAddress(models.Model):
    consignee = models.CharField(max_length=200,null=True)
    address = models.CharField(max_length=200,null=True)
    city = models.CharField(max_length=200,null=True)
    state = models.CharField(max_length=200,null=True)
    phone = models.CharField(max_length=10,null=True)
    email = models.EmailField(null=True)
    date_added = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.consignee


class Review(models.Model):
    userview = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.ForeignKey(Product, on_delete=models.CASCADE)
    review_desp = models.CharField(max_length=100)
    rating = models.IntegerField()
    def __str__(self):
        return str(self.item)
    

