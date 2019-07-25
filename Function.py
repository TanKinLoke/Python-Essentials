print ("Chester is Awesome")
print ("Nelson is Awesome")
print ("Harry is Awesome")

def everyoneIsAwesome(): #define "everyoneIsAwesome" as a command/function
    print ("Chester is Awesome")
    print ("Nelson is Awesome")
    print ("Harry is Awesome")
    print ("") #skip a line

everyoneIsAwesome()
everyoneIsAwesome()

def sayMyName(name):
    print ("YO! " + name)

sayMyName("Zhe Yuan")
sayMyName("Joshua")
sayMyName("Chester")

print ("")

def sayTwoName(name, name2):
    print ("YO! " + name) #Both are string so can be add together
    print ("YO! " + name2)

sayTwoName("brian","Chester")

print ("")

def sum(num1, num2):
    print ("First Number:", num1) #"First Number" is string, num1 is integer, these 2 cannot be added, so use ","
    print ("Second Number:", num2)
    print ("Total:", num1+num2) 

sum(5,10)

print("")
print("Exercise")
print("")

#Exercise
def multiply(num1, num2):
    print(num1, "multiply by", num2,"=",num1*num2)

multiply (5,10)

def multiply(x):
    return(x*x) #Return the answer of x multiply by x

multiply(10)
print (multiply(20)) #This will show it in the console

def minus5(y):
    return(y-5)

print (minus5(minus5(50)))
#Means 50-5-5=40, inside the (minus(50)=45, then (minus5(minus5(50))) means minus 5 again after minus5(50). A function inside a function.

#Exercise2
def multiply3(x):
    return(3*x)

print (multiply3(multiply3(multiply3(5))))

def sayGreetings():
    print("Olla!")

def sayGreetings2():
    print("Annyeonghaseyo!")

sayGreetings()
sayGreetings2()

def minus(num1,num2):
    print(num1-num2)

minus(10,2)

def multi(num1,num2):
    print(num1*num2)

def divide(num1,num2):
    print(num1/num2)

multi (2,4)
divide (4,2)

def plus2(num1):
    return(num1+2)

def result(number):
    print("Result is ...")
    print(number)
    print("Woohoo!")

result(plus2(10))

def minus2(num1):
    print (num1)
    congratulations()

def congratulations():
    print("Woohoo!!!")

minus2(10)

print ("")

def sorryTeacher(customMessage):
    print(customMessage)

def loop(count,customMessage):
    for x in range(0,count):
        sorryTeacher(customMessage)

loop(4,"Sorry teacher I wont be late again")

print ("")

def customMessage(message,x):
    print(x,".",message)

def loop (count,message):
    for x in range(1,count+1):
        customMessage(message,x)

loop (10,"Sorry teacher I will submit my homework on time")




