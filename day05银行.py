import time
print("系统正在加载\n" ,end="")
for i in range(3):
    print("...\n", end="")
    time.sleep(0.5)
print("                   西牛贺州银行欢迎您                 ")
print("|------------1、开户                     ------------|")
print("|------------2、取钱                     ------------|")
print("|------------3、存钱                     ------------|")
print("|------------4、转账                     ------------|")
print("|------------5、查询                     ------------|")
print("|------------6、退出                     ------------|")
print("=====================================================")
import random
bank={}#创建一个空的字典
#开户逻辑
bank_name="西牛贺州银行"
#                第一个对应第一个 不是名称对应名称
def bank_adduser(account,username,password,country,province,street,door):
    if  len(bank) >100:
        return 3
    if account in bank:#  如变量在容器内执行下面的代码
        return 2
    bank[account]={
      #  "account":account,
        "username":username,
        "password":password,
        "country":country,
        "province":province,
        "street":street,
        "door":door,
        "money":0,
        "bank_name":bank_name
    }
    return 1
def adduser():#定义了一个方法
    username=input("请输入您的用户名")
    password = input("请输入您的密码")
    print("请输入您的地址")
    country=input("\t\t请输入您的国家")
    province=input("\t\t请输入您的省份")
    street=input("\t\t请输入您的街道")
    door=input("\t\t请输入您的门牌号")
    account=random.randint(10000000,99999999)
    stast=bank_adduser(account,username,password,country,province,street,door)
    #        调用方法   （元素，，，，，，，，，）
    if stast ==3 :
        print("你去别的银行吧")
    elif stast== 2:
        print("开户失败，你别重复")
    elif stast== 1:
        info = '''
                    ------------个人信息------------
                    用户名:%s
                    账号：%s
                    密码：*****
                    国籍：%s
                    省份：%s
                    街道：%s
                    门牌号：%s
                    余额：%s
                    开户行名称：%s
                '''
        # 每个元素都可传入%
        print(info % (username, account, country, province, street, door, bank[account]["money"], bank_name))
#{'frank': {'account': 88474479, 'password': '1234', 'country': '1', 'province': '1', 'street': '1', 'door': '1', 'money': 0, 'bank_name': '狼腾测试猿银行'}}
#3.存钱
def   addmoney():#定义了一个方法
    account = input("请输入您的账户")
    if account in bank:
        money1 = float(input("请输入存取金额：￥"))
        bank[account]["money"] += money1
        print("当前余额：￥", bank[account]["money"])
    else:
       print("账号不存在。请检查账户输入")
       return False
#2.取钱
def   qumoney():#定义了一个方法
    account = input("请输入您的账户")
    if account in bank:
        password = input("请输入您的密码")
        if password == bank[account]["password"]:
            money2 = float(input("请取出金额：￥"))
            bank[account]["money"] -= money2
            if bank[account]["money"] < 0:
                print("余额不足")
            else:
                print("当前余额：￥", bank[account]["money"])
        else:
            print("密码错误，请检查密码输入")
    else:
        print("账号不存在。请检查账户输入")
        return False
# 转账
def zz():
    account1 = int(input("请输入转出的账号"))
    account2 = int(input("请输入转入的账号"))
    if account1 and account2 in bank:
        password = input("请输入转出的账号密码")
        if password == bank[account1]["password"]:
            print("当前余额为￥", bank[account1]["money"])
            money = float(input("请输入转账金额：￥"))
            if money <= bank[account1]["money"]:
                bank[account1]["money"] -= money
                bank[account2]["money"] += money
                print("转账成功！")
        else:
                print("密码错误，请检查密码输入")
    else:
            print("账号不存在。请检查账户输入")

# 查询功能
def cha():
    caccount = int(input("请输入想要查询的账号："))
    if caccount in bank:
        password= input("请输入密码：")
        if password == bank[caccount]["password"]:
            print("密码正确！")
            info = '''
            用户名：%s
            账号：%s
            密码：%s 
                                                                                                       地址：%s
            余额：%s元
            开户行名称：%s
            '''
            print(info % (bank[caccount]["username"], caccount, bank[caccount]["password"],
                          bank[caccount]["country"] + bank[caccount]["province"] + bank[caccount][
                              "street"] + bank[caccount]["door"], bank[caccount]["money"],
                          bank[caccount]["bank_name"]))
        else:
            print("密码错误，请检查密码输入")
    else:
        print("账号不存在。请检查账户输入")


while True:
    begin = input("请选择业务")
    if begin == "1":
        adduser()
    elif begin == "2":
        qumoney()
    elif begin == "3":
        addmoney()
    elif begin == "4":
        zz()
    elif begin == "5":
        cha()
    else:
        print(6, "、退出")
        break