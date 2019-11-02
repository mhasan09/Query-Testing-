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
    # customers = MSE_CUSTOMERS.objects.all()
    # customer_name = MSE_CUSTOMERS.objects.values_list('customer_name', flat=True)
    # customer_mobile_number = MSE_CUSTOMERS.objects.values_list('customer_mobile_number', flat=True)
    # customer_due_amount = MSE_CUSTOMERS.objects.values_list('customer_due_amount', flat=True)
    # customers_dict = dict()
    # customers_dict['customer_name'] = customer_name
    # customers_dict['customer_mobile_number'] = customer_mobile_number
    # customers_dict['customer_due_amount'] = customer_due_amount
    # customers_list = list()
    # customers_list.append(customers_dict)
    # print(customers_list)
    # context = {
    #     'customer' : customers,
    #     'customers_list' : customers_list
    # }
    # return render(request,'customers.html',context)
    customer_list = list()
    customer = MSE_CUSTOMERS.objects.all()
    for i in customer:
        temp_dict = dict()
        temp_dict['customer_name'] = i.customer_name
        temp_dict['customer_mobile_number'] = i.customer_mobile_number
        temp_dict['customer_due_amount'] = i.customer_due_amount
        customer_list.append(temp_dict)
    context = {
        'customer' : customer_list,
    }
    print(customer_list)
    return render(request,'customers.html',context)