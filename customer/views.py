# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render
import datetime,time
from django.core import serializers
# Create your views here.
from customer.models import *
from django.core.paginator import Paginator


def main_view(request):
    return render(request, 'main.html')


def center(request):
        # noticeList = NoticeInfo.objects.all()

    return render(request, 'center.html')
def left(request):
    return render(request, 'left.html')
def top(request):
    return render(request, 'top.html')
def down(request):
    return render(request, 'down.html')

#关怀提醒
def get_careObj(request):

    selectDays = request.GET.get('selectDays','')
    selectDays = int(selectDays)
    date = datetime.datetime.now()-datetime.timedelta(days=selectDays)
    careObjs = CustomerCare.objects.filter(care_time__gte=date).order_by('-care_time')

    if careObjs:
        careList = serializers.serialize('json', careObjs)
        return JsonResponse({'careList':careList})
    return JsonResponse({'careList':[]})

#联系提醒
def get_linkObj(request):
    linkSelectDays = request.GET.get('linkSelectDays', '')
    linkSelectDays = int(linkSelectDays)

    date = datetime.datetime.now() - datetime.timedelta(days=linkSelectDays)
    linkObjs = CustomerLinkreord.objects.filter(link_time__gte=date).order_by('-link_time')

    if linkObjs:
        linkList = serializers.serialize('json', linkObjs)
        return JsonResponse({'linkList': linkList})
    return JsonResponse({'linkList': []})

#公告提醒
def get_noticeObj(request):
    noticeObjs = NoticeInfo.objects.all().order_by('-notice_endtime')
    noticeList = serializers.serialize('json',noticeObjs)
    return JsonResponse({'noticeList':noticeList})
    # import json
    #全部公告对象，部分字段
    # noticeObjs = NoticeInfo.objects.values('user__user_name','notice_item','notice_content','notice_endtime').order_by('-notice_endtime')
    #建空列表用来装格式化好时间的对象字符串
    # nList = []

    # for noticeObj in noticeObjs:
    #     #格式化时间字段
    #     # noticeObj['notice_endtime'] = datetime.datetime.strftime(noticeObj['notice_endtime'],'%Y-%m-%d %H:%M:%S')
    #     noticeObj['notice_endtime'] = '%s-%s-%s %s:%s:%s'%(noticeObj['notice_endtime'].year,noticeObj['notice_endtime'].month,noticeObj['notice_endtime'].day,noticeObj['notice_endtime'].hour,noticeObj['notice_endtime'].minute,noticeObj['notice_endtime'].second)
    #     #将对象转成json字符串
    #     noticeStr = json.dumps(noticeObj)
    #     print noticeStr
    #
    #     #将格式化好的json字符串放入新列表
    #     nList.append(noticeStr)
    # noticeStr = serializers.serialize('json',noticeObjs)
    # return JsonResponse({'noticeList':str(nList)})
#当天过生日的人
def get_birthObj(request):
    datenow = datetime.datetime.now()
    birthMonth = datenow.month
    birthDay = datenow.day
    birthListDay = CustomerInfo.objects.filter(birth_day__month=birthMonth,birth_day__day=birthDay)
    birthList = serializers.serialize('json',birthListDay)
    return JsonResponse({'birthList':birthList})


#参数：分页内容、页码数，每页条数
def paginatorFunc(cusInfoList,num,count):
    pagiObj = Paginator(cusInfoList, count)
    t_per_page = pagiObj.page(num)
    #获取全部页数
    lenPage = pagiObj.num_pages
    if num < 1:
        num = 1
    elif num > lenPage:
        num = lenPage
    return t_per_page,lenPage,num
def get__customerList1(request):
    #get请求处理
    if request.method == 'GET':
        #如果get请求有flag参数
        if request.GET.has_key('flag'):
            flag = request.GET.get('flag','')
            num = request.GET.get('num',1)
            num = int(num)
            #姓名
            if flag == '1':
                selectValue = request.GET.get('selectValue', '')
                try:
                    selectList = CustomerInfo.objects.filter(customer_name=selectValue).order_by('customer_id')
                    recordCount = len(selectList)
                    t_per_page, lenPage, num = paginatorFunc(selectList, num,count=3)
                    return render(request, 'customer_list1.html',
                                  {'t_per_page': t_per_page, 'lenPage': lenPage, 'num': num, 'flag': flag,
                                   'recordCount': recordCount, 'selectValue': selectValue})

                except CustomerInfo.DoesNotExist:
                    return HttpResponse('搜索内容不存在')
            #状态
            if flag == '2':
                selectValue = request.GET.get('selectValue', '')
                try:
                    selectList = CustomerCondition.objects.get(condition_name=selectValue).customerinfo_set.all().order_by('customer_id')
                    recordCount = len(selectList)
                    t_per_page, lenPage, num = paginatorFunc(selectList, num,count=3)
                    return render(request, 'customer_list1.html',
                                  {'t_per_page': t_per_page, 'lenPage': lenPage, 'num': num, 'flag': flag,
                                   'recordCount': recordCount, 'selectValue': selectValue})

                except CustomerInfo.DoesNotExist:
                    return HttpResponse('搜索内容不存在')

            #来源
            if flag == '3':
                selectValue = request.GET.get('selectValue','')
                print selectValue
                try:
                    selectList = CustomerSource.objects.get(source_name=selectValue).customerinfo_set.all().order_by('customer_id')
                    recordCount = len(selectList)
                    t_per_page, lenPage, num = paginatorFunc(selectList, num,count=3)

                    return render(request, 'customer_list1.html',
                                  {'t_per_page': t_per_page, 'lenPage': lenPage, 'num': num, 'flag': flag,
                                   'recordCount': recordCount, 'selectValue': selectValue})
                except CustomerInfo.DoesNotExist:
                    return HttpResponse('搜索内容不存在')
            # 类型
            if flag == '4':
                selectValue = request.GET.get('selectValue', '')
                try:
                    selectList = CustomerType.objects.get(type_name=selectValue).customerinfo_set.all().order_by('customer_id')
                    recordCount = len(selectList)
                    t_per_page, lenPage, num = paginatorFunc(selectList, num,count=3)
                    return render(request, 'customer_list1.html',
                                  {'t_per_page': t_per_page, 'lenPage': lenPage, 'num': num, 'flag': flag,
                                   'recordCount': recordCount, 'selectValue': selectValue})
                except CustomerInfo.DoesNotExist:
                    return HttpResponse('搜索内容不存在')
            # 公司
            if flag == '6':
                selectValue = request.GET.get('selectValue', '')
                try:
                    selectList = CustomerInfo.objects.filter(customer_company=selectValue).order_by('customer_id')
                    recordCount = len(selectList)
                    t_per_page, lenPage, num = paginatorFunc(selectList, num,count=3)
                    return render(request, 'customer_list1.html',
                                  {'t_per_page': t_per_page, 'lenPage': lenPage, 'num': num, 'flag': flag,
                                   'recordCount': recordCount, 'selectValue': selectValue})
                except CustomerInfo.DoesNotExist:
                    return HttpResponse('搜索内容不存在')
            # 所属员工
            if flag == '5':
                selectValue = request.GET.get('selectValue', '')
                try:
                    selectList = UserInfo.objects.get(user_name=selectValue).customerinfo_set.all().order_by('customer_id')
                    recordCount = len(selectList)
                    t_per_page, lenPage, num = paginatorFunc(selectList, num,count=3)
                    return render(request, 'customer_list1.html',
                                  {'t_per_page': t_per_page, 'lenPage': lenPage, 'num': num, 'flag': flag,
                                   'recordCount': recordCount, 'selectValue': selectValue})
                except CustomerInfo.DoesNotExist:
                    return HttpResponse('搜索内容不存在')


        else:
            num = request.GET.get('num',1)
            num = int(num)
            allCusInfo = CustomerInfo.objects.all().order_by('customer_id')
            recordCount = len(allCusInfo)
            t_per_page,lenPage,num = paginatorFunc(allCusInfo,num,count=3)
            return render(request,'customer_list1.html',{'t_per_page':t_per_page,'lenPage':lenPage,'num':num,'recordCount':recordCount})
    #post请求处理
    else:
        selectValue = request.POST.get('customerInput','')
        queryType = request.POST.get('queryType','')
        num = request.POST.get('num',1)
        #判断输入框是否有值
        if selectValue:
            #客户姓名 1
            if queryType == '1':
                selectList = CustomerInfo.objects.filter(customer_name=selectValue).order_by('customer_id')
                recordCount = len(selectList)
                t_per_page, lenPage,num = paginatorFunc(selectList,num,count=3)
                #返回页面内容，页面内容、全部页数
                return render(request, 'customer_list1.html',
                              {'t_per_page': t_per_page, 'lenPage': lenPage, 'num': num,'flag':1,'recordCount':recordCount,'selectValue':selectValue})
            # 客户状态 2
            elif queryType == '2':
                selectList = CustomerCondition.objects.get(condition_name=selectValue).customerinfo_set.all().order_by('customer_id')
                recordCount = len(selectList)
                t_per_page, lenPage, num = paginatorFunc(selectList, num,count=3)
                return render(request, 'customer_list1.html',
                              {'t_per_page': t_per_page, 'lenPage': lenPage, 'num': num,'flag':2,'recordCount':recordCount,'selectValue':selectValue})
            #客户来源 3
            elif queryType == '3':
                selectList = CustomerSource.objects.get(source_name=selectValue).customerinfo_set.all().order_by('customer_id')
                recordCount = len(selectList)
                t_per_page, lenPage, num = paginatorFunc(selectList, num,count=3)
                return render(request, 'customer_list1.html',
                              {'t_per_page': t_per_page, 'lenPage': lenPage, 'num': num,'flag':3,'recordCount':recordCount,'selectValue':selectValue})
            #客户类型 4
            elif queryType == '4':
                selectList = CustomerType.objects.get(type_name=selectValue).customerinfo_set.all().order_by('customer_id')
                recordCount = len(selectList)
                t_per_page, lenPage, num = paginatorFunc(selectList, num,count=3)
                return render(request, 'customer_list1.html',
                              {'t_per_page': t_per_page, 'lenPage': lenPage, 'num': num,'flag':4,'recordCount':recordCount,'selectValue':selectValue})
            #所属员工 5
            elif queryType == '5':
                selectList = UserInfo.objects.get(user_name=selectValue).customerinfo_set.all().order_by('customer_id')
                recordCount = len(selectList)
                t_per_page, lenPage, num = paginatorFunc(selectList, num,count=3)
                return render(request, 'customer_list1.html',
                              {'t_per_page': t_per_page, 'lenPage': lenPage, 'num': num,'flag':5,'recordCount':recordCount,'selectValue':selectValue})
            #客户公司 6
            elif queryType == '6':
                selectList = CustomerInfo.objects.filter(customer_company=selectValue).order_by('customer_id')
                recordCount = len(selectList)
                t_per_page, lenPage, num = paginatorFunc(selectList, num,count=3)
                return render(request, 'customer_list1.html',
                              {'t_per_page': t_per_page, 'lenPage': lenPage, 'num': num,'flag':6,'recordCount':recordCount,'selectValue':selectValue})
        else:
            return HttpResponseRedirect('/main/customer_list1.html')
def get_customer_add(request):

    return render(request,'customer_add.html')


def get_customer_edit(request):
    if request.method == 'GET':
        customerid = request.GET.get('id','')
        if customerid:
            try:
                cusUser = CustomerInfo.objects.get(customer_id=customerid)
                users = UserInfo.objects.all()
                conditions = CustomerCondition.objects.all()
                types = CustomerType.objects.all()
                sources = CustomerSource.objects.all()
                return render(request,'customer_edit.html',{'customerid':customerid,'cusUser':cusUser,'userList':users,'conditions':conditions,'types':types,'sources':sources})

            except CustomerInfo.DoesNotExist:
                return HttpResponse('没有这个用户！')
        return HttpResponse('请填写用户名')


def get_customer_detail(request):
    id = request.GET.get('id')
    objInfo = CustomerInfo.objects.get(customer_id=id)
    return render(request,'customer_detail.html',{'objInfo':objInfo,'cid':id})


def customerUpdateServlet(request):
    postList = ['customerForUser','Source','customerName','customerCondition','customerSex','customerType','customerBirthday','customerMobile','customerQq','customerAddress','customerEmail','customerJob','customerBlog','customerTel','customerMsn','customerCompany','customerAddMan','customerChangeMan','customerRemark']
    customerForUser = request.POST.get('customerForUser','')

    source = request.POST.get('Source','')
    customerId = request.POST.get('customerId','')
    customerCondition = request.POST.get('customerCondition','')
    customerSex = request.POST.get('customerSex','')
    customerType = request.POST.get('customerType','')
    customerBirthday = request.POST.get('customerBirthday','')
    customerMobile = request.POST.get('customerMobile','')
    customerQq = request.POST.get('customerQq','')
    customerAddress = request.POST.get('customerAddress','')
    customerEmail = request.POST.get('customerEmail','')
    customerJob = request.POST.get('customerJob','')
    customerBlog = request.POST.get('customerBlog','')
    customerTel = request.POST.get('customerTel','')
    customerMsn = request.POST.get('customerMsn','')
    customerCompany = request.POST.get('customerCompany','')
    customerAddMan = request.POST.get('customerAddMan','')
    customerChangeMan = request.POST.get('customerChangeMan','')
    customerRemark = request.POST.get('customerRemark','')

    userUp = UserInfo.objects.get(user_id=customerForUser)
    sourceUp = CustomerSource.objects.get(source_id=source)
    conditionUp = CustomerCondition.objects.get(condition_id=customerCondition)
    typeUp = CustomerType.objects.get(type_id=customerType)
    customerObj = CustomerInfo.objects.filter(customer_id=customerId)
    customerObj.update(user=userUp,source=sourceUp,condition=conditionUp,type=typeUp,customer_sex=customerSex,customer_mobile=customerMobile,customer_qq=customerQq,customer_email=customerEmail,customer_address=customerAddress,customer_job=customerJob,customer_blog=customerBlog,customer_msn=customerMsn,customer_tel=customerTel,customer_company=customerCompany,change_man=customerChangeMan,customer_remark=customerRemark)

    return HttpResponseRedirect('/main/customer_detail.html?id=%s'%customerId)


def deleteCusInfo(request):
    id = request.GET.get('delId')
    id = int(id)
    CustomerInfo.objects.get(customer_id=id).delete()

    return HttpResponseRedirect('/main/customer_list1.html')


def createCustomer(request):

    if request.method == 'GET':
        cusSources = CustomerSource.objects.all()
        cusTypes = CustomerType.objects.all()
        cusCoditions = CustomerCondition.objects.all()
        return render(request,'customer_add.html',{'cusSources':cusSources,'cusTypes':cusTypes,'cusCodition':cusCoditions})
    else:
        # postList = ['customerForUser', 'Source', 'customerName', 'customerCondition', 'customerSex', 'customerType',
        #             'customerBirthday', 'customerMobile', 'customerQq', 'customerAddress', 'customerEmail',
        #             'customerJob', 'customerBlog', 'customerTel', 'customerMsn', 'customerCompany', 'customerAddMan',
        #             'customerChangeMan', 'customerRemark']
        #获取请求参数
        sourceId = request.POST.get('customerSource', '')
        customerName = request.POST.get('customerName', '')
        customerConditionId = request.POST.get('customerCondition', '')
        customerSex = request.POST.get('customerSex', '')
        customerTypeId = request.POST.get('customerType', '')
        customerBirthday = request.POST.get('customerBirthday', '')
        customerBirthday = datetime.datetime.strptime(customerBirthday,'%Y-%m-%d %H:%M:%S')
        customerMobile = request.POST.get('customerMobile', '')
        customerQq = request.POST.get('customerQq', '')
        customerAddress = request.POST.get('customerAddress', '')
        customerEmail = request.POST.get('customerEmail', '')
        customerJob = request.POST.get('customerJob', '')
        customerBlog = request.POST.get('customerBlog', '')
        customerTel = request.POST.get('customerTel', '')
        customerMsn = request.POST.get('customerMsn', '')
        customerCompany = request.POST.get('customerCompany', '')
        customerAddMan = request.POST.get('customerAddMan', '')
        customerChangeMan = request.POST.get('customerChangeMan', '')
        customerRemark = request.POST.get('customerRemark', '')

        #获取外键对象，外键是select选取，一定会有值
        sourceUp = CustomerSource.objects.get(source_id=sourceId)
        conditionUp = CustomerCondition.objects.get(condition_id=customerConditionId)
        typeUp = CustomerType.objects.get(type_id=customerTypeId)
        #增加用户信息
        CustomerInfo.objects.create(is_used='1',customer_addman=customerAddMan,birth_day=customerBirthday, customer_name=customerName,source=sourceUp, condition=conditionUp, type=typeUp, customer_sex=customerSex,
                           customer_mobile=customerMobile, customer_qq=customerQq, customer_email=customerEmail,
                           customer_address=customerAddress, customer_job=customerJob, customer_blog=customerBlog,
                           customer_msn=customerMsn, customer_tel=customerTel, customer_company=customerCompany,
                           change_man=customerChangeMan, customer_remark=customerRemark)

        return HttpResponseRedirect('/main/customer_list1.html')