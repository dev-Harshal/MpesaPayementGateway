from django.db import models
from atomicloops.models import ATLBaseModel,Users




class PaymentDetails(ATLBaseModel):
    customer = models.ForeignKey(Users,db_column='customer',on_delete=models.CASCADE)
    phoneNo = models.CharField(max_length=13,db_column='phone_no',null=True,blank=True)
    amount = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)

    status_choices = [
        ('NA','Na'),
        ('Successful','Successful'),
        ('Failed','Failed'),
    ]

    status = models.CharField(max_length=10,choices=status_choices,default='NA')