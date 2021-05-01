from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
# Create your models here.
#an online couon usually consists of acode that is given to users,valid for aspecific time frame.code can be 
#redeemed one or multiple times, our coupons will be valid for clients that enter the coupon in aspecific time frame
#coupons will not have any limitations in terms of the number of times they can be reddemed,and they will be
#applied to the total value of the shopping cart.hence create amodel to store the coupon code,avalid timeframe
#and the discount to apply

class Coupon(models.Model):
    code = models.CharField(max_length=50,unique=True)#users have to enter this inorder to apply coupon to their purchase
    valid_from = models.DateTimeField()#from when coupon becomes valid
    valid_to = models.DateTimeField()#when the coupon becomes invalid
    discount = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)])#discount rate to apply
    #(percentage,so it takes from 0to100.use validators for this field to limit the minimum and max accepted values)
    active = models.BooleanField()#indicates whether coupon is active

    def __str__(self):
        return self.code