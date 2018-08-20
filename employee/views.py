# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from customer.models import HouseType

#进入房屋类型页面
def house_type_view(request):
    # 获取请求参数
    num = request.GET.get('num', 1)
    # houseTypeName = request.GET.get('houseTypeName')
    num = int(num)
    #获取数据库数据
    houseTypes = HouseType.objects.all().order_by('type_id')
    #创建分页器对象，并显示每页展示信息条数
    pageObj = Paginator(houseTypes, 2)
    #显示当前页码数中的内容
    per_page = pageObj.page(num)
    #页面信息总条数
    counter = len(houseTypes)
    #获取每页总条数(如果总共十条数据，则显示5页）
    page_counter = pageObj.num_pages

    return render(request,'house_type_list.html',{'flag':1,'num':num,'per_page':per_page,'counter':counter,'page_counter':page_counter})

#进入添加房屋类型页面
def house_add(request):
    return render(request,'house_add.html')
#处理房屋类型添加功能
def deal_house_add(request):
    #获取数据请求参数
    typeNames = request.POST.get('typeNames')
    #判断是否为空
    if typeNames:
        try:
            HouseType.objects.get(type_name=typeNames)
            return HttpResponse('该房屋类型已存在')
        except:
            house_type = HouseType(type_name=typeNames)
            house_type.save()
            return HttpResponse('添加成功')
    else:
        return HttpResponse('房屋类型不能为空')

#处理查询功能
def deal_house_type_query(request):
    #获取请求参数
    houseTypeName = request.POST.get('houseTypeName')
    #非空判断：
    if houseTypeName:
        num = request.GET.get('num', 1)
        num = int(num)
        #获取数据库数据
        houseTypes = HouseType.objects.filter(type_name=houseTypeName).order_by('type_id')
        # houseTotals = HouseType.objects.all().count()
        pageObj = Paginator(houseTypes, 2)
        per_page = pageObj.page(num)
        counter = len(houseTypes)
        page_counter = pageObj.num_pages
        return render(request, 'house_type_list.html', {'num':num,'per_page': per_page,'counter':counter,'flag':0,'houseTypeName':houseTypeName,'page_counter':page_counter})
    else:
        return HttpResponseRedirect('/employee/house_type')

    # 处理房屋分页功能
# def deal_house_page(request):
    # # 获取请求参数
    # num = request.GET.get('num', 1)
    # num = int(num)
    # print num
    # #获取数据库数据
    # pageData = HouseType.objects.all().order_by('type_id')
    # #创建分页器对象，并显示每页展示信息条数
    # pageObj = Paginator(pageData, 2)
    # #显示当前页码数中的内容
    # per_page = pageObj.page(num)
    # #页面信息总条数
    # counter = len(pageData)
    # #获取每页总条数(如果总共十条数据，则显示5页）
    # page_counter = pageObj.num_pages
    # return render(request,'house_type_list.html',{'num':num,'per_page':per_page,'counter':counter,'page_counter':page_counter})





#处理删除功能
def deal_house_delete(request):
    #获取请求参数
    house_type_id = request.GET.get('houseTypeId')
    # 获取数据库所有数据
    house_name = HouseType(type_id=house_type_id)
    house_name.delete()
    return HttpResponse('删除成功')
