#一、猜数字
#经典的猜数字游戏，几乎所有人学编程时都会做。
#
#功能描述：随机选择一个三位以内的数字作为答案。用户输入一个数字，程序会提示大了或是小了，直到用户猜中。
#
#
#
#二、FizzBuzz
#另一道经典编程题。
#
#功能描述：遍历并打印0到100，如果数字能被3整除，显示Fizz；如果数字能被5整除，显示Buzz；如果能同时被3和5整除，就显示FizzBuzz。结果应该类似：0,1,2，Fizz，4，Buzz，6……14，FizzBuzz，16……
#
#
#
#三、猜数字的AI
#和猜数字一样，不过这次是设计一个能猜数字的AI
#
#功能描述：用户输入一个单位以内的数字，AI要用最少的次数猜中，并且显示出猜的次数和数字。
#import random
#b = random.randint(0,999)
#print (b)
#a = int(input())
#print (a)
#if a>b:
#    print ("bigger")
#elif a<b:
#    print ("smaller")
#elif a==b:
#    print ("right")
#print("??")

for i in range(0,100):
    #print (i%3)
    if i == 0:
        print (i)
    elif i%15 ==0:
        print("FizzBuzz")
    elif i%3 == 0:
        print ("Fizz")
    elif i%5 ==0:
        print ("Buzz")
    else :
        print (i)

#import random 
#
##a = random.randint(0,999)
#b = input()
#a = 500
#if a >b:
#    a = a/2
