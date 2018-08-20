# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import math
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.core import serializers
# Create your views here.
from django.views import View

from customer.models import CustomerSource


def index_view(request):
    user= request.session.get('user_str','')
    if user:
        return render(request,'index.html')
    else:
        return HttpResponseRedirect('/employee/login/')


def center(request):

    return render(request, 'center.html')
def left(request):
    return render(request, 'left.html')
def top(request):
    return render(request, 'top.html')
def down(request):
    return render(request, 'down.html')


def customer_list(request):
    return render(request,'customer_source_list.html')

from django.core.paginator import Paginator

#分页函数，返回每页对象列表和当前页码
def page(value,num=1,size=2):
    num = int(num)
    if num < 1:
        num = 1
    # 计算总页数
    if value:
        total_records = CustomerSource.objects.filter(source_name=value)
        counts =total_records.count()
    else:
        total_records = CustomerSource.objects.all()
        counts =total_records.count()
    total_pages = int(math.ceil(counts*1.0/size))
    if num > total_pages:
        num = total_pages
        # print num
    source_list = total_records[((num - 1) * size):(num * size)]
    # print num,source_list
    return source_list,num,total_pages,counts

def query_customer_source(request):
    #接受data
    num =int(request.GET.get('num',1))
    value =request.GET.get('value','')
    # flag =request.GET.get('flag','')
    # print num,value
    source_list,num,total_pages,counts =page(value=value,num=num)
    source_str = serializers.serialize('json', source_list)
    pre_page = num - 1
    if num<total_pages:
        next_page = num + 1
    else:
        next_page =0
    # print  source_str
    # return JsonResponse({'source_str':source_str})
    # if flag:
    #     return JsonResponse({'flag':flag,'num': num, 'source_str': source_str, 'per_page': pre_page, 'next_page': next_page,
    #                          'total_pages': total_pages, 'counts': counts})
    return JsonResponse({'num':num,'source_str':source_str,'per_page':pre_page,'next_page':next_page,'total_pages':total_pages,'counts':counts})

def delete_one(request):
    source_name = request.GET.get('source_name','')
    print source_name
    source_obj =CustomerSource.objects.filter(source_name=source_name)
    source_obj.update(is_used=0)
    return HttpResponseRedirect('/customer/customer_source_list.html/')

class CustomerSourceAdd(View):
    def get(self,request):
        return render(request,'customer_source_add.html')
    def post(self,request):
        source_name = request.POST.get('sourceName')
        print source_name
        try:
            source_obj =CustomerSource.objects.get(source_name=source_name)
        except CustomerSource.DoesNotExist:
            CustomerSource.objects.create(source_name=source_name,is_used =1)
        return HttpResponseRedirect('/customer/customer_source_list.html/')

