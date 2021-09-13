#1.实现输入10个数字，并打印10个数的求和结果
i=0
num=0
while 10-i>0:
     a=input("请输入一个数字")
     a= int(a)
     i=i+1
     num = num + a
print("结果等于",num)
#//////////////////////
'''
#1.实现输入10个数字，并打印10个数的求和结果
print("请依次输入10个数")
print("1 2 3 4 5 6 7 8 9 10" "方便记录数字数量")
a0,a1,a2,a3,a4,a5,a6,a7,a8,a9 =input().split()
num=0
num =int(a0)+int(a1)+int(a2)+int(a3)+int(a4)+int(a5)+int(a6)+int(a7)+int(a8)+int(a9)
#num =a0,a1,a2,a3,a4,a5,a6,a7,a8,a9
print(num)
'''
#//////////////////////
#2.从键盘依次输入10个数，最后打印最大的数、10个数的和、和平均数。
i=0
z=0
num=0
b=0
while 9 - i > 0:
     a=input("请输入一个数字")
     a= int(a)
     max(a, b)
     if b<a :
       b=a
     else:
       b=b
       i=i+1
     num=num + a
p=num/10
print("和为",num)
print("平均数为",p)
print("最大的数是", b)
#3.使用random模块，如何产生 50~150之间的数？
import random
#                 范围
num=random.randint(50, 150)#   随机一个数字赋值给num
#        这是一个随机数函数   起始值为0     终止值为20000
print(num)

'''4.从键盘输入任意三边，判断是否能形成三角形，若可以，则判断形成什么三角形
（结果判断：等腰，等边，直角，普通，不能形成三角形。）
'''
print("请输入三个数字，并用空格分别隔开")
a,b,c=map(int ,input().split())
if a<b+c and b<a+c and c<a+b:
    if a==b==c:
        print('等边三角形')
    elif a==b or a==c or b==c:
        if a*a+b*b==c*c or a*a+c*c==b*b or b*b+c*c==a*a:
            print('等腰直角三角形')
        else:
            print('等腰三角形')
    elif a*a+b*b==c*c or a\
            *a+c*c==b*b or b*b+c*c==a*a:
        print('直角三角形')
    else:
        print('普通三角形')
else:
    print('无法构成三角形')
'''5.有以下两个数，使用+，-号实现两个数的调换。
A=56
B=78
实现效果：
A=78
B=56
'''
A=56
B=78
A=A+B
B=A-B
A=A-B
print(A,B)
#6.实现登陆系统的三次密码输入错误锁定功能（用户名：root,密码：admin）
a=input("输入你的用户名")
if a=='root'or a=='ROOT' :
    b = input("请输入你的密码")
    if b=='admin'or b=='ADMIN':
        print("密码正确")
    else:
        b = input("密码错误，请重新输入你的密码")
        if b=='admin'or b=='ADMIN':
            print("密码正确")
        else:
            b = input("密码错误，请重新输入你的密码")
            if b == 'admin' or b == 'ADMIN':
                print("密码正确")
            else:
                print("密码错误已经三次，请到柜台办理修改密码业务")
#7.编程实现下列图形的打印
print("       *")
print("      * *")
print("     * * *")
print("    * * * *")
print("   * * * * *")
print("  * * * * * *")
print(" * * * * * * * ")
#8.使用while循环实现99乘法表的打印。
'''i = 1
for i in range(1,10 ):
    for j in range(1,i+1):
        print('{}x{}={}\t'.format(j, i, i * j), end='')
    print()'''
i=1
while i<10:
    j=1
    while j<i+1:
        print('{}x{}={}\t'.format(j,i , i*j), end='')
        j=j+1
    i=i+1
    print()
#9.编程实现99乘法表的倒叙打印
i=9
z=0
while i>0:
    j=9-z
    while j>0:
        print('{}*{}={}\t'.format(i,j,i*j),end='')
        j = j - 1
    i=i-1
    z=z+1
    print()
#10.一只青蛙掉在井里了，井高20米，青蛙白天网上爬3米，晚上下滑2米，问第几天能出来？请编程求出。
"""i=0
z=20-i
a=0
j=1
while z>0:
     a=a+3
     if  a ==20 :
      print("你出来了用了",j,"天")
      break
     else :
       a=a-2
       i = a
       z = 20-i
       j=j+1

"""
a=0
j=1
while a < 20:
     a=a+3
     if  a ==20 :
      print("你出来了用了",j,"天")
     else :
       a=a-2
       j=j+1
'''11.判断下列变量命名是否合法
标识符	是否合法	标识符	是否合法
char	是	Cy%ty	否
Oax_li	是	$123	否
fLul	是	3_3 	否
BYTE	是	T_T	是
'''
'''12.继续完成上午的猜数字游戏的需求功能。
1.	添加计数打印功能
2.	添加次数金币功能和锁定系统功能。
猜字游戏
需求：
1、猜的数字是系统产生的，不是自己定义的
2、键盘输入的   操作完填入：input（“提示”）
3、判断			操作完填入：if判断条件 elif 判断条件。。。。。。Else
4、循环			操作完填入：while 条件循环
任务：你的初始资金为100 每猜一次减10  资金为0时或者猜成功游戏结束
    猜大 如果你输入的数字和随机数对比 大于随机数  打印一句话为  猜大了
    猜小 如果你输入的数字和随机数对比 小于随机数  打印一句话为  猜小了
'''
import random
#                 范围
num=random.randint(0, 2)#   随机一个数字赋值给num
#        这是一个随机数函数   起始值为0     终止值为20000
print(num)#打印一个随机数
i=10
z=100-i
print(z)
while z>0:
     a=input("请输入一个数字")# 从键盘上输入一个   字符    赋值给a
     a= int(a)
     if  a == num :
      print("你成功了")
      print("你还剩",z)
      break
     elif  a >num :
       print("猜大了")
       i=i+10
       z=100-i
       print("你还剩",z)
     else :
       print("猜小了")
       i = i+10
       z = 100 - i
       print("你还剩",z)
while z==0:
    print("游戏结束")
    break
#13.用循环来实现20以内的数的阶乘。（1! +2!+3!+…..+20!）
#用循环来实现20以内-的数的阶乘。（1! +2!+3!+…..+20!）
num =int(input("请输入一个数字: "))
    #int(input("请输入一个数字: "))
a = 1
# 查看数字是负数，0 或 正数
if num < 0:
    print("抱歉，负数没有阶乘")
elif num == 0:
    print("0 的阶乘为 1")
else:
    for i in range(1, num + 1):
        a = a * i
    print("%d 的阶乘为 %d" % (num, a))
