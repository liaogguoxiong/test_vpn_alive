#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time             : 2019-10-18 17:55
# @Author           : lgx
# @project_name     : request
# @File             : ping_test.py
# @Des: 测试vpn是否在线

import os,sys
from email_of_zabbix import *
os.system('chcp 65001')

def test():
    """
    测试vpn是否在线
    :return:
    """

    receiver = "297979949@qq.com"
    """
    发生故障之后,只发送一次邮件
    0:表示未发送过
    1:表示已经发
    """
    times_path="send_sing"
    with open(times_path,"r",encoding="utf-8") as f:
        r1=f.readline()
    times=int(r1)
    """
    vpn恢复之后,发送恢复通知
    0:表示未发送过
    1:表示已经发
    """
    recover_sign="recover_sign"
    with open(recover_sign,"r",encoding="utf-8") as f:
        r2=f.readline()
    r_sign=int(r2)

    ip='192.168.20.57'
    cmd="ping {}".format(ip)
    res=os.system(cmd)
    if res == 0:
        print("vpn还在运行")
        with open(times_path, "w", encoding="utf-8") as f:
            f.write("0")
        if r_sign == 0:
            sujbect = "vpn恢复了"
            content = "vpn已经恢复了"
            send_email(receiver, sujbect, content)
            with open(recover_sign, "w", encoding="utf-8") as f:
                f.write("1")


    else:

        sujbect="vpn挂掉了"
        content="vpn挂掉了,请尽快重新登陆vpn"
        if times == 0:
            """
            为0,表示没有发送过报错邮件
            """
            send_email(receiver,sujbect,content)
            print("邮件发送成功")
            with open(times_path, "w", encoding="utf-8") as f:
                f.write("1")
            with open(recover_sign, "w", encoding="utf-8") as f:
                f.write("0")
        else:
            print("邮件已经发送过了")



test()


