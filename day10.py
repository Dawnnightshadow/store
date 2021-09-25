'''生产者消费者模型
任务：
当蛋挞篮子已经满了，停3秒钟，继续判断是否满了，若没有则继续造蛋挞
 有6个人卖蛋挞每人3000元，若蓝子不够则用户等待2秒钟。继续判断还有没有，有继续买，一直到钱花完为止'''

import threading
import  time
from  threading import Thread
cake=500
class User(threading.Thread):
    username=""
    money = 0
    buy=0
    def run(self) ->None:
        global cake
        while True:
            if self.money > 0:
                if cake>0:
                    self.money=self.money-2
                    cake=cake - 1
                    # 获取锁，用于线程同步
                    threadLock.acquire()
                    print(self.username,"成功买到了一个蛋挞！还剩，",cake,"个蛋挞")
                    # 释放锁，开启下一个线程
                    threadLock.release()
                    self.buy = self.buy + 1
                    time.sleep(0.02)
                else:
                    time.sleep(0.02)
                    threadLock.acquire()
                    print("正在做，请稍等")
                    # 释放锁，开启下一个线程
                    threadLock.release()
                    continue
            else:
                 # 获取锁，用于线程同步
                 threadLock.acquire()
                 print(self.username,"本次共买到了",self.buy,"个蛋挞！")
                 # 释放锁，开启下一个线程
                 threadLock.release()
                 break
threadLock = threading.Lock()
class worker(threading.Thread):
    username=""
    make=""
    def run(self) ->None:
        global cake
        while True:
            if cake < 500:
                cake=cake + 1
                threadLock.acquire()
                print(self.username,"成功做了一个蛋挞！")
                threadLock.release()
                self.make=self.make+1
                time.sleep(0.02)

            else:
                 time.sleep(0.02)
                 threadLock.acquire()
                 print(self.username, "共做了",self.make,"个蛋挞！")
                 threadLock.release()
                 break
u1=User()
u1.username="张三"
u1.money=3000
u1.buy=0
u2=User()
u2.username="李四"
u2.money=3000
u2.buy=0
u3=User()
u3.username="王五"
u3.money=3000
u3.buy=0
u4=User()
u4.username="赵六"
u4.money=3000
u4.buy=0
u5=User()
u5.username="苏七"
u5.money=3000
u5.buy=0
u6=User()
u6.username="孙八"
u6.money=3000
u6.buy=0
u1.start()
u2.start()
u3.start()
u4.start()
u5.start()
u6.start()
w1=worker()
w1.username="钱一"
w1.make=0
w2=worker()
w2.username="朱二"
w2.make=0
w3=worker()
w3.username="阎三"
w3.make=0
w1.start()
w2.start()
w3.start()