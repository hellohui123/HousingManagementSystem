# -*- coding: utf-8 -*-
from __future__ import unicode_literals

<<<<<<< HEAD
import jsonpickle
import datetime

import re
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.core.serializers import serialize
# Create your views here.
from django.views import View

from customer.models import UserInfo, NoticeInfo, DepartmentInfo, HouseInfo, HouseType


def center(request):

    return render(request, 'center.html')
def left(request):
    return render(request, 'left.html')
def top(request):
    return render(request, 'top.html')
def down(request):
    return render(request, 'down.html')
#用户类，登录设置session用
class User(object):
    def __init__(self,uname,pwd):
        self.uname = uname
        self.pwd=pwd

#三年免登录功能
class Login(View):
    def get(self,request,*args,**kwargs):
        return render(request,'login.html')
    def post(self,request,*args,**kwargs):
        #获取参数
        uname = request.POST.get('userNum','')
        pwd = request.POST.get('userPw','')
        #非空判断
        if uname and pwd:
            #核对数据库
            user= UserInfo.objects.filter(user_num =uname,user_pw=pwd)
            if user:
                user_obj =User(uname=uname,pwd=pwd)
                user_str = jsonpickle.dumps(user_obj)
                request.session['user_str']=user_str
                request.session.set_expiry(3*365*24*60*60)
                return HttpResponseRedirect('/customer/')
        return HttpResponseRedirect('/employee/login/')

class HandleNotice(View):
    def get(self,request):
        #接受页码参数
        current_page = request.GET.get('page',1)
        # print current_page
        current_page = int(current_page)
        #查询所有公告
        notice_list = NoticeInfo.objects.filter(is_used=1)
        page_obj =Paginator(notice_list,per_page=1)
        size =page_obj.per_page
        pre_nums = (current_page-1)*size
        if current_page>page_obj.num_pages:
            current_page=1
        per_page_notices = page_obj.page(current_page)
        flag=1
        return render(request,'notice_list.html',{'flag':flag,'pre_nums':pre_nums,'notice_list':per_page_notices,'page_obj':page_obj,'current_page':current_page})
    def post(self,request):
        '''条件查询'''
        query_words =request.POST.get('noticeInput','')
        query_type = request.POST.get('queryType','')
        # print query_words,query_type
        if query_type=='公告内容':
            query_notice = NoticeInfo.objects.filter(Q(is_used=1)&Q(notice_content=query_words))
        else:
            query_notice = NoticeInfo.objects.filter(Q(is_used=1)&Q(notice_item=query_words))
        # print query_notice
        pre_nums =0
        page_obj = Paginator(query_notice, per_page=1)
        size = page_obj.per_page
        pre_nums = 0
        per_page_notices = page_obj.page(1)
        flag=0
        return render(request,'notice_list.html',{'flag':flag,'pre_nums':pre_nums,'notice_list':per_page_notices,'page_obj':page_obj,'current_page':1})
def delete_notice(request):
    notice_id = request.GET.get("notice_id",'')
    NoticeInfo.objects.filter(notice_id=notice_id).update(is_used=0)
    return HttpResponseRedirect('/employee/notice_list.html')


class AddNotice(View):
    def get(self,request):
        return render(request,'add_notice.html')
    def post(self,request):
        #1.获取表单参数
        user_id = request.POST.get('noticePublisher','')
        notice_item =request.POST.get('noticeName','')
        notice_content =request.POST.get('noticeContent','')
        start_time = request.POST.get('startTime','')
        end_time = request.POST.get('endTime','')
        is_used = request.POST.get('flagLabel','')
        print start_time
        #2.存储数据库
         #格式化字符串为日期
        notice_time =datetime.datetime.strptime(start_time,"%Y-%m-%d %H:%M:%S")
        notice_endtime = datetime.datetime.strptime(end_time,"%Y-%m-%d %H:%M:%S")
         #存储数据
        NoticeInfo.objects.create(user_id=user_id,notice_item =notice_item,notice_content=notice_content,notice_time=notice_time,notice_endtime=notice_endtime,is_used=is_used)
        return HttpResponseRedirect('/employee/notice_list.html')


def add_publisher(request):
    #获取所有用户
    user_list = UserInfo.objects.filter(is_used=1)
    #序列化
    user_str =serialize('json',user_list)
    #返回Json对象
    return JsonResponse({"user_str":user_str})


class Handle_dept(View):
    def get(self,request):
        '''查询所有'''
        current_page = request.GET.get('page',1)
        current_page =int(current_page)
        #1.获取所有部门对象列表
        dept_list =DepartmentInfo.objects.filter(is_used=1)
        #2.分页
        paginator = Paginator(dept_list,1)
        per_page_depts =paginator.page(current_page)
        #前一页最后一条记录下标
        size = paginator.per_page
        pre_nums = size*(current_page-1)
        flag=1
        return render(request,'dept_list.html',{'flag':flag,'paginator':paginator,'dept_list':per_page_depts,'current_page':current_page,'pre_nums':pre_nums})

    def post(self,request):
        '''关键字查询'''
        #获取部门名
        current_page=int(1)
        dept_name =request.POST.get('departmentName','')
        #获取数据库数据
        dept_list = DepartmentInfo.objects.filter(department_name=dept_name)
        #分页
        paginator = Paginator(dept_list,1)
        per_page_depts =paginator.page(1)
        pre_nums =0
        flag=0
        return render(request,'dept_list.html',{'flag':flag,'paginator':paginator,'dept_list':per_page_depts,'current_page':current_page,'pre_nums':pre_nums})






def delete_dept(request):
    dept_id = request.GET.get("dept_id", '')
    DepartmentInfo.objects.filter(department_id=dept_id).update(is_used=0)
    return HttpResponseRedirect('/employee/dept_list.html')


class HandleHouseInfo(View):
    def get(self,request):
        '''查询所有'''
        current_page = request.GET.get('page', 1)
        current_page = int(current_page)
        base_url =request.path
        base_url =base_url+'?'
        # print base_url
        # 1.获取所有房屋列表
        house_list = HouseInfo.objects.filter(is_used=1)
        # 2.分页
        paginator = Paginator(house_list, 3)
        per_page_houses = paginator.page(current_page)
        # 前一页最后一条记录下标
        size = paginator.per_page
        pre_nums = size * (current_page - 1)
        return render(request,'house_list.html',{'base_url':base_url,'house_list':per_page_houses,'paginator':paginator,'current_page':current_page,'pre_nums':pre_nums})

def delete_hosue_info(request):
    '''删除房屋信息'''
    house_id = request.GET.get("house_id", '')
    HouseInfo.objects.filter(house_id=house_id).update(is_used=0)
    return HttpResponseRedirect('/employee/house_list.html')


class UpdateHouseInfo(View):
    def post(self,request):
        '''修改房屋信息'''
        #1.接受参数
        house_id =request.GET.get('house_id','')
        # print house_id
        house_type_id = request.POST.get('houseType',)
        # print house_type_id
        empolyee_id = request.POST.get('employee',)
        # print empolyee_id
        house_address = request.POST.get('houseAddress',)
        house_price = request.POST.get('housePrice',)
        house_environment = request.POST.get('houseEnvironment', )
        is_used =request.POST.get('flagLabel')
        #2.与数据库交互，修改响应信息
        # obj=HouseInfo.objects.filter(house_id=house_id)
        # print obj
        HouseInfo.objects.filter(house_id=house_id).update(type_id=house_type_id,user_id=empolyee_id,house_address=house_address,house_price=house_price,house_ambient=house_environment,is_used=is_used)
        return HttpResponseRedirect('/employee/house_list.html')


def get_house_type(request):
    '''得到所有房屋类型'''
    house_types =HouseType.objects.filter(is_used=1)
    house_types_str =serialize('json',house_types)
    return JsonResponse({'house_types_str':house_types_str})


def receive_house_info(request):
    house_id =request.GET.get('house_id','')
    house_type =request.GET.get('house_type','')
    type_obj =HouseType.objects.get(type_name=house_type)
    empolyee =request.GET.get('empolyee','')
    empolyee_obj =UserInfo.objects.get(user_name=empolyee)
    house_address =request.GET.get('house_address','')
    house_price =request.GET.get('house_price','')
    house_environment =request.GET.get('house_environment','')
    return render(request,'update_house_info.html',{'house_id':house_id,'type_obj':type_obj,'empolyee_obj':empolyee_obj,'house_address':house_address,'house_price':house_price,'house_environment':house_environment})


def get_employee(request):
    '''得到所有员工对象'''
    employee = UserInfo.objects.filter(is_used=1)
    employee_str = serialize('json', employee)
    return JsonResponse({'employee_str': employee_str})


class Add_house_info(View):
    def get(self,request):
        return render(request,'add_house_info.html')
    def post(self,request):
        house_type_id = request.POST.get('houseType', )
        print '房屋类型：'+house_type_id
        empolyee_id = request.POST.get('employee', )
        print '员工：'+empolyee_id
        house_address = request.POST.get('houseAddress', )
        print '地址：'+house_address
        house_price = request.POST.get('housePrice', )
        print '价格：'+house_price
        house_environment = request.POST.get('houseEnvironment', )
        print '环境：'+house_environment
        is_used = request.POST.get('flagLabel')
        print '可用：'+is_used
        try:
            HouseInfo.objects.get(Q(type_id=house_type_id)&Q(user_id=empolyee_id)&Q(house_address=house_address)&Q(house_price=house_price)&Q(house_ambient=house_environment)&Q(is_used=is_used))
        except HouseInfo.DoesNotExist:
            HouseInfo.objects.create(type_id=house_type_id,user_id=empolyee_id,house_address=house_address,house_price=house_price,house_ambient=house_environment,is_used=is_used)
        return HttpResponseRedirect('/employee/house_list.html')

class Query_by_keys(View):
    def get(self,request):
        '''条件查询翻页'''
        current_page = request.GET.get('page', 1)
        current_page = int(current_page)
        flag =request.GET.get('flag','')
        print flag
        base_url =request.path
        if flag:
            base_url = base_url + '?' + 'flag=' + flag
            base_url =base_url+'&'
            # 1.获取所有房屋列表
            house_list = HouseInfo.objects.filter(Q(is_used=1) & Q(type_id=flag))
            if len(house_list) == False:
                house_list = HouseInfo.objects.filter(Q(is_used=1) & Q(house_id=flag))
        else:
            house_list=[]
            base_url =base_url+'?'
        print base_url
        # 2.分页
        paginator = Paginator(house_list, 1)
        per_page_houses = paginator.page(current_page)
        # 前一页最后一条记录下标
        size = paginator.per_page
        pre_nums = size * (current_page - 1)
        return render(request,'house_list.html',{'base_url':base_url,'house_list':per_page_houses,'paginator':paginator,'current_page':current_page,'pre_nums':pre_nums})
    def post(self,request):
        '''条件查询房屋信息'''
        query_words = request.POST.get('houseInput', '')
        query_type = request.POST.get('queryType', '')
        print query_words,query_type
        if query_type == '1':  # 房屋类型
            # 查询出房屋类型的id
            try:
                type_obj = HouseType.objects.get(type_name=query_words)
                type_id =type_obj.type_id
                # type_id =int(float(type_id))
                type_id =str(type_id)
                # print type_id
                # query_house = HouseInfo.objects.filter(Q(is_used=1) & Q(type_id=type_obj.type_id))
                return HttpResponseRedirect('/employee/query_by_keys/?flag='+type_id)
            except HouseType.DoesNotExist:
                return HttpResponseRedirect('/employee/query_by_keys/')
        else:
            #'地址查询'
            try:
                query_house = HouseInfo.objects.get(Q(is_used=1)&Q(house_address=query_words))
                house_id =query_house.house_id
                house_id =str(house_id)
                return HttpResponseRedirect('/employee/query_by_keys/?flag='+house_id)
            except HouseInfo.DoesNotExist:
                return HttpResponseRedirect('/employee/query_by_keys/')

=======
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from customer.models import *
from customer.views import paginatorFunc
# Create your views here.
#处理删除User表数据
def deleteUserInfo(request):
    id = request.GET.get('id','')
    id = int(id)
    UserInfo.objects.get(customer_id=id).delete()

    return HttpResponseRedirect('/employee/empl_list.html')
#处理em_list页面请求
def get_em_list(request):
    #处理get请求
    if request.method == 'GET':
        num = request.GET.get('num',1)
        num = int(num)
        flag = request.GET.get('flag','')
        # 处理有flag参数，查询的请求
        if flag:
            selectValue = request.GET.get('selectValue','')
            # 员工姓名 1
            if flag == '1':
                selectList = UserInfo.objects.filter(user_name=selectValue).order_by('user_id')

                recordCount = len(selectList)
                t_per_page, lenPage, num = paginatorFunc(selectList, num, count=3)
                # 返回页面内容，页面内容、全部页数
                return render(request, 'empl_list.html',
                              {'t_per_page': t_per_page, 'lenPage': lenPage, 'num': num, 'flag': 1,
                               'recordCount': recordCount, 'selectValue': selectValue})
            # 部门名称
            elif flag == '2':
                selectList = DepartmentInfo.objects.get(department_name=selectValue).userinfo_set.all()
                recordCount = len(selectList)
                t_per_page, lenPage, num = paginatorFunc(selectList, num, count=3)
                return render(request, 'empl_list.html',
                              {'t_per_page': t_per_page, 'lenPage': lenPage, 'num': num, 'flag': 2,
                               'recordCount': recordCount, 'selectValue': selectValue})
            # 角色名称
            elif flag == '3':
                selectList = UserRole.objects.get(role_name=selectValue).userinfo_set.all().order_by('user_id')
                recordCount = len(selectList)
                t_per_page, lenPage, num = paginatorFunc(selectList, num, count=3)
                return render(request, 'empl_list.html',
                              {'t_per_page': t_per_page, 'lenPage': lenPage, 'num': num, 'flag': 3,
                               'recordCount': recordCount, 'selectValue': selectValue})
            # 员工学历
            elif flag == '4':
                selectList = UserInfo.objects.filter(user_diploma=selectValue).order_by('user_id')
                recordCount = len(selectList)
                t_per_page, lenPage, num = paginatorFunc(selectList, num, count=3)
                return render(request, 'empl_list.html',
                              {'t_per_page': t_per_page, 'lenPage': lenPage, 'num': num, 'flag': 4,
                               'recordCount': recordCount, 'selectValue': selectValue})
            else:
                return HttpResponse('您查询的项目不存在')
        #处理正常显示所有内容的get请求
        else:
            userObjList = UserInfo.objects.all()
            recordCount = len(userObjList)
            #引入分页器，参数：分页内容、页码数，每页条数
            t_per_page,lenPage,num = paginatorFunc(userObjList,num,count=2)
            return render(request, 'empl_list.html',
                          {'t_per_page': t_per_page, 'lenPage': lenPage, 'num': num, 'recordCount': recordCount})
    #处理post请求
    else:
        selectValue = request.POST.get('userName', '')
        queryType = request.POST.get('queryType', '')
        num = request.POST.get('num', 1)
        print selectValue
        # 判断输入框是否有值
        if selectValue:
            # 员工姓名 1
            if queryType == '1':
                selectList = UserInfo.objects.filter(user_name=selectValue).order_by('user_id')

                recordCount = len(selectList)
                t_per_page, lenPage, num = paginatorFunc(selectList, num, count=3)
                # 返回页面内容，页面内容、全部页数
                return render(request, 'empl_list.html',
                              {'t_per_page': t_per_page, 'lenPage': lenPage, 'num': num, 'flag': 1,
                               'recordCount': recordCount, 'selectValue': selectValue})
            # 部门名称
            elif queryType == '2':
                selectList = DepartmentInfo.objects.get(department_name=selectValue).userinfo_set.all()
                recordCount = len(selectList)
                t_per_page, lenPage, num = paginatorFunc(selectList, num, count=3)
                return render(request, 'empl_list.html',
                              {'t_per_page': t_per_page, 'lenPage': lenPage, 'num': num, 'flag': 2,
                               'recordCount': recordCount, 'selectValue': selectValue})
            # 角色名称
            elif queryType == '3':
                selectList = UserRole.objects.get(role_name=selectValue).userinfo_set.all().order_by('user_id')
                recordCount = len(selectList)
                t_per_page, lenPage, num = paginatorFunc(selectList, num, count=3)
                return render(request, 'empl_list.html',
                              {'t_per_page': t_per_page, 'lenPage': lenPage, 'num': num, 'flag': 3,
                               'recordCount': recordCount, 'selectValue': selectValue})
            # 员工学历
            elif queryType == '4':
                selectList = UserInfo.objects.filter(user_diploma=selectValue).order_by('user_id')
                recordCount = len(selectList)
                t_per_page, lenPage, num = paginatorFunc(selectList, num, count=3)
                return render(request, 'empl_list.html',
                              {'t_per_page': t_per_page, 'lenPage': lenPage, 'num': num, 'flag': 4,
                               'recordCount': recordCount, 'selectValue': selectValue})
            else:
                return HttpResponse('您查询的项目不存在')
        else:
            return HttpResponseRedirect('/employee/empl_list.html')


def get_emp_edit(request):
    user_id = request.GET.get('id','')

    userobj = UserInfo.objects.get(user_id=user_id)
    departObjs = DepartmentInfo.objects.all()
    roleObjs = UserRole.objects.all()
    return render(request,'emp_edit.html',{'userobj':userobj,'departObjs':departObjs,'roleObjs':roleObjs})



def userUpdateServlet(request):
    userId = request.POST.get('userId','')
    print userId
    userSex = request.POST.get('userSex','')
    userDiploma = request.POST.get('userDiploma','')
    userDepartmentName = request.POST.get('departmentName','')
    userTel = request.POST.get('userTel','')
    userBankcard = request.POST.get('userBanckcard','')
    userIdcard = request.POST.get('userIdcard','')
    userEmail = request.POST.get('userEmail','')
    userAge = request.POST.get('userAge','')
    userNation = request.POST.get('userNation','')
    userIsmarried = request.POST.get('userIsmarrid','')
    userIntest = request.POST.get('userIntest','')
    userMobile = request.POST.get('userMobile','')
    userChangeman = request.POST.get('userChangeman','')
    userAddress = request.POST.get('userAddress','')
    departmentObj = DepartmentInfo.objects.get(department_name=userDepartmentName)
    UserInfo.objects.filter(user_id=userId).update(department=departmentObj,user_sex=userSex,user_diploma=userDiploma,user_tel=userTel,user_bankcard=userBankcard,user_idnum=userIdcard,
                            user_email=userEmail,user_age=userAge,user_nation=userNation,is_married=userIsmarried,user_intest=userIntest,user_mobile=userMobile,
                            user_changeman=userChangeman,user_address=userAddress)
    # return HttpResponseRedirect('/employee/emp_detail.html?id=%s'%userId)
    return render(request,'skip5seconds.html',{'pageName':'客户信息页','pageHref':'/employee/emp_detail.html?id='+userId})


def emp_detail(request):
    userid = request.GET.get('id','')
    if userid:
        userObj = UserInfo.objects.get(user_id=userid)
        return render(request,'emp_detail.html',{'userObj':userObj})
    else:
        return HttpResponseRedirect('/employee/empl_list.html')
>>>>>>> 5eb9938e74366b08ad26ef23b0627190108e9648
