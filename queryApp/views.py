from django.views.generic import View
from django.http import HttpResponse, JsonResponse
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
    customer_info = dict()
    customer_info['id'] = customer.id
    customer_info['customer_name'] = customer.customer_name
    customer_info['customer_mobile'] = customer.customer_mobile_number
    customer_info['customer_due_amount'] = customer.customer_due_amount
    print(customer_info)
    context = {
        'customer': customer,
        'customer_info' : customer_info
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


class updateUser(View):
    def get(self,request):
        id1 = request.GET.get('customer_id',None)
        cn = request.GET.get('customer_name', None)
        cmn = request.GET.get('customer_mobile_number', None)
        cda = request.GET.get('customer_due_amount', None)
        print("dddd",id1,cn,cmn,cda)
        customer = MSE_CUSTOMERS.objects.get(id=id1)
        customer.customer_name = cn
        print("xxx")
        customer.customer_mobile_number = cmn
        customer.customer_due_amount = cda
        customer.save()
        customer = {
            'id': customer.id,
            'customer_name': customer.customer_name,
            'customer_mobile_number': customer.customer_mobile_number,
            'customer_due_amount': customer.customer_due_amount
        }
        data = {
            'customer': customer
        }
        return JsonResponse(data)