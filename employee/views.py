# -*- coding: utf-8 -*-
from __future__ import unicode_literals

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