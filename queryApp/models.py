from django.db import models

# Create your models here.

class MSE_CUSTOMERS(models.Model):
    customer_name = models.CharField("Customer Name", max_length=150, null=True, blank=True)
    customer_mobile_number = models.CharField("Mobile Number", max_length=13, null=True, blank=True)
    customer_due_amount = models.DecimalField("Due Amount", decimal_places=4, max_digits=10, null=True, blank=True)


    class Meta:
        verbose_name_plural = "Customers"

    def __str__(self):
        return str(self.customer_name) or 'u'

