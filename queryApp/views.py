from django.core.serializers import json
from django.http import HttpResponse
from django.shortcuts import render
from .forms import createForm
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
    # customer_list = list()
    customer = MSE_CUSTOMERS.objects.all()
    # for i in customer:
    #     temp_dict = dict()
    #     temp_dict['customer_name'] = i.customer_name
    #     temp_dict['customer_mobile_number'] = i.customer_mobile_number
    #     temp_dict['customer_due_amount'] = i.customer_due_amount
    #     customer_list.append(temp_dict)
    context = {
        'customer' : customer,

    }
    return render(request,'customers.html',context)

def detail_view_via_form(request,id):
    customer = MSE_CUSTOMERS.objects.get(id=id)
    form = createForm(request.POST or None,instance=customer)
    if form.is_valid():
        form.save()
    context = {
        'customer': customer,
        'form': form,
    }
    return render(request, 'customer_detail.html', context)


def detail_view(request,id):
    customer = MSE_CUSTOMERS.objects.get(id=id)
    context = {
        'customer': customer,
    }
    return render(request, 'customer_detail_queryset.html', context)


def chart(request):
    customer_name_array = []
    customer_due_amount= []
    customer = MSE_CUSTOMERS.objects.all()
    for i in customer:
       customer_name_array.append(i.customer_name)
       customer_due_amount.append(i.customer_due_amount)
    context = {
        'customer': customer_name_array,
        'customer_due': customer_due_amount,
    }
    return render(request, 'line_chart.html', context)

def map(request):
    return render(request, 'map.html')


def customer_saved(request):
    customer_name = request.GET['customer_name']
    customer_mobile_number = request.GET['customer_mobile_number']
    customer_due_amount = request.GET['customer_due_amount']
    customer = MSE_CUSTOMERS.objects.get(id=id)

    for i in customer:
        i.customer_name = customer_name
        i.customer_mobile_number = customer_mobile_number
        i.customer_due_amount = customer_due_amount
        customer_name.save()
        customer_mobile_number.save()
        customer_due_amount.save()
    data_dict = dict()
    data_dict["status"] = "202"
    return HttpResponse(json.dumps(data_dict))
    # return HttpResponse(json.dumps(data_dict))
