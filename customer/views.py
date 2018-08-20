# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import math
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import time
# Create your views here.

from customer.models import CustomerType, CustomerInfo


def index_view(request):
    return render(request,'index.html')


def center(request):
    return render(request, 'center.html')


def left(request):
    return render(request, 'left.html')

#进入添加数据页面
def customerType1(request):
    # 获取请求参数
    num = request.GET.get('num', 1)
    # houseTypeName = request.GET.get('houseTypeName')
    num = int(num)
    # 获取数据库数据
    customers = CustomerType.objects.all().order_by('type_id')
    # 创建分页器对象，并显示每页展示信息条数
    pageObj = Paginator(customers, 2)
    # 显示当前页码数中的内容
    per_page = pageObj.page(num)
    # 页面信息总条数
    counter = len(customers)
    # 获取每页总条数(如果总共十条数据，则显示5页）
    page_counter = pageObj.num_pages
    return render(request,'customer_type1.html',{'flag':1,'num':num,'per_page':per_page,'counter':counter,'page_counter':page_counter})
#查询功能记录数的处理
def deal_customer_query(request):

    TypeName = request.POST.get('TypeName')
    # 非空判断：
    if TypeName:
        num = request.GET.get('num', 1)
        num = int(num)
        # 获取数据库数据
        customersTypes = CustomerType.objects.filter(type_name=TypeName).order_by('type_id')
        # houseTotals = HouseType.objects.all().count()
        pageObj = Paginator(customersTypes, 2)
        per_page = pageObj.page(num)
        counter = len(customersTypes)
        page_counter = pageObj.num_pages
        return render(request,'customer_type1.html',{'num':num,'per_page':per_page,'customersTypes':customersTypes,'counter':counter,'page_counter':page_counter})
    else:
        return HttpResponseRedirect('/index/customer_type1')
        # customers_all_datas = CustomerType.objects.all()
        # return render(request,'customer_type1.html',{'customers_all_datas':customers_all_datas})
#处理客户类型分页功能
def deal_customer_page(request):
    pass
#进入添加数据页面
def customer_add(request):
    return render(request,'customer_add.html')

  #添加功能处理
def deal_customer_add(request):
    # 获取请求参数
    TypeName = request.POST.get('typeName')

        # 获取数据库所有信息
    if TypeName:
        try:
            CustomerType.objects.get(type_name=TypeName)
        except:
            typeName=CustomerType(type_name=TypeName)
            typeName.save()
            return HttpResponse('添加成功')
            # time.sleep(1)
            # return HttpResponseRedirect('/index/customer_type1')
        return HttpResponse('添加失败')
#处理删除功能
def deal_customer_delete(request):
    #获取请求参数
    type_id = request.GET.get('type_id')
    #获取数据库所有数据
    type_name = CustomerType(type_id=type_id)
    type_infors = CustomerInfo.objects.all()
    for type_infor in type_infors:
        type_infor.delete()
    type_name.delete()

    return HttpResponse('删除成功')




def top(request):
    return render(request, 'top.html')
def down(request):
    return render(request, 'down.html')


