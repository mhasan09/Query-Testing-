from django.shortcuts import render
from queryApp.models import *
import names,random
# Create your views here.


def data_load(request):
    for i in range(0,100):
        obj = MSE_CUSTOMERS()
        obj.customer_name = names.get_first_name()
        obj.customer_mobile_number = "01"+str(random.randint(300000000,999999999))
        obj.customer_due_amount =random.randint(10,10000)
        obj.save()
def data_send(request):
    customers = MSE_CUSTOMERS.objects.all()
    return render(request,'customers.html',{'customers':customers})