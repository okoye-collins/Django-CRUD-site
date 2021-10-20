from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Item(models.Model):

    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    item_name = models.CharField(max_length=200)
    item_dec = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_img = models.CharField(max_length=500, default="https://farrerpark.thegoodboys.com.sg/wp-content/uploads/2019/11/food-placeholder.jpg")

    def __str__(self):
        return self.item_name


    def get_absolte_url(self):
        return reverse('food:detail', kwargs={'pk': self.pk})

