# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

from customer.models import UserInfo, DepartmentInfo,UserRole

#跳转到员工添加页面
def employee_views(request):
    # 获取部门和角色数据库数据并将其传递给页面
    userRoles = UserRole.objects.all()  # 获取所有角色
    departmentInfors = DepartmentInfo.objects.all()  # 获取部门所有名称
    #将获取到的数据传到页面中
    return render(request,'employee_add.html',{'userRoles':userRoles,'departmentInfors':departmentInfors})

#处理员工添加功能
def deal_employee_add(request):
    #获取请求参数
    userName = request.POST.get('userName')#姓名
    userNum = request.POST.get('userNum')#账号
    userAge = request.POST.get('userAge')#年龄
    userPw = request.POST.get('userPw')#密码
    userSex = request.POST.get('userSex')#性别
    userNation = request.POST.get('userNation')#民族
    userDiploma = request.POST.get('userDiploma')#学历
    isMarried = request.POST.get('isMarried')#婚姻状况
    departmentId = request.POST.get('departmentId')#部门
    roleId = request.POST.get('roleId')#角色
    userTel = request.POST.get('userTel')#座机
    userIntest = request.POST.get('userIntest')#爱好
    userBankcard = request.POST.get('userBankcard')#工资卡号
    userMobile = request.POST.get('userMobile')#手机号
    userIdnum = request.POST.get('userIdnum')#身份证号
    userAddtime = request.POST.get('userAddtime')#用户添加时间
    userAddress = request.POST.get('userAddress')#地址
    userAddman = request.POST.get('userAddman')#添加人
    userEmail = request.POST.get('userEmail')#Email
    #判断非空：
    if userName and userSex and userSex and userMobile and userAge and userAddress and userName and userPw and userTel and userIdnum and userEmail and userAddtime and userAddman and userIntest and userDiploma and userBankcard and userNation and isMarried and roleId:
        userInfor = UserRole.objects.get(role_id=roleId)
        departmentInfor = DepartmentInfo.objects.get(department_id=departmentId)
        data3 = UserInfo(user_name= userName,role=userInfor,department= departmentInfor,user_sex = userSex,user_mobile= userMobile,user_age= userAge,user_address= userAddress,user_num= userNum,user_pw= userPw,user_tel= userTel,user_idnum= userIdnum,user_email= userEmail,user_addtime= userAddtime,user_addman = userAddman,user_changeman= '未修改',user_intest= userIntest,user_diploma= userDiploma,user_bankcard = userBankcard,user_nation= userNation,is_married= isMarried,)
        data3.save()
        return HttpResponse('添加成功')
    return HttpResponse('该用户名不能为空或已存在')

#跳转到添加部门页面
def department_views(request):
    return render(request,'department_add.html')

#处理添加部门功能
def deal_department_add(request):
    #获取请求参数
    departmentName = request.POST.get('departmentName')
    departmentDesc = request.POST.get('departmentDesc')
    #进行非空判断
    if departmentName and departmentDesc:
        try:
            DepartmentInfo.objects.get(department_name=departmentName)
            return HttpResponse('该用户名已存在')
        except:
        #添加到数据库
            departmentInfor = DepartmentInfo(department_name=departmentName,department_desc=departmentDesc)
            departmentInfor.save()
            return HttpResponse('添加成功')
    else:
        return HttpResponse('添加失败')

#跳转到角色添加功能
def role_add_views(request):

    return render(request,'role_add.html')

    #处理角色添加功能
def deal_role_add(request):
    roleName = request.POST.get('roleName')
    rolePower = request.POST.get('rolePower')
    if roleName and rolePower:
        try:
            UserRole.objects.get(role_name=roleName)
            return HttpResponse('该角色已存在')
        except:
            user_role = UserRole(role_name=roleName,role_power=rolePower)
            user_role.save()
            return HttpResponse('添加成功')
    else:
        return HttpResponse('添加失败')

#查看已有角色
def deal_already_exist(request):
    #获取所有角色信息，并显示到页面上
    userRoles = UserRole.objects.all()
    return render(request,'exist_role.html',{'userRoles':userRoles})