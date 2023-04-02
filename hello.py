# # print("hello")

# # print(2+3)

# # n = int(input("enter your number"))
# # print("number is :" ,n)

# delhi_bang = 245
# bang_ker = 235
# total_distance = delhi_bang + bang_ker
# # print(total_distance)
# speed = 69
# time = total_distance/speed
# print(round(time,5))

# print(6-5.9)

# s = 'shivang scored good marks which is '
# num = '25'
# print(s+num)

# address = ''' f-33a 
# tird fllor
# laxmi nagar '''
# print(address)

# item1 = 'sydney'
# item2 = 'melbournce'
# item3 = 'brisbane'
# item4 = 'perth'
# australia = ['sydney','melbournce','brisbane','perth']
# # print(items)
# items.append('adelaide')
# print(items)

# india = ['delhi','mumbai','indore','rajasthan']
# pakistan = ['karachi','islamabad','lahore','sialkot']
# china = ['beijing','shanghai','shenzhen','tianjin']
# city = input("enter city\n")
# if city in australia:
#     print("australia op")
# elif city in india:
#     print("india op")
# elif city in pakistan:
#     print("pakistan op")
# else :
#     print("china op")

# a = int(input("enter your 1 number"))
# b = int(input("enter your 2 number"))
# c = int(input("enter your 3 number"))
# if (a>b and a>c):
#     print("A bada67")
# elif (c>b and c>a):
#     print("C bada")
# else :
#     print("B bada")


# exp = [69,69,79,33,67]
# total = 0
# for item in exp:
#     total = total + item
# print(total)
# for i in range(1,11,2):
#     print(i+1)
# for i in range(len(exp)):
#     print("month",i+1,"expenses is :",exp[i])
# for i in exp:
#     if i==79:
#         print("key found in",i )
# else :
#     print("key not found in",i)

# for i in range(1,6):
#     if i%2==0:
#         continue
#     print(i*i)

# i = 1
# while i <=5 :
#     print(i)
#     i = i+1

# def calculate_total(exp):
#     total = 0
#     for items in exp:
#         total = total + items
#     return total
# tommy  = [1200,2300,3200,4500]
# harry = [1200,3400,6700,4500]
# tom = calculate_total(tommy)
# har = calculate_total(harry)

# print("tommy expenses :",tom)
# print("harry expenses :",har)

# def sum(a,b):
#     print("a",a)
#     print("b",b)
#     total = a + b
#     print("total",total)
#     return total
# n = sum(5,6)

# d = {"shivang":7006935960 , "rohan": 8527601257 , "kartikay": 9910615050}
# print(d)
# d["papa"] = 8851091030
# print(d)                                                   DICTIONARY BASICS
# del d["papa"]
# print(d)
# d.clear()
# print(d)

# import calendar
# # cal = calendar.month(2016,1)                           USING CALENDER MODULE
# # print(cal)
# if calendar.isleap(2016):
#     print("yes")

# import user_define_functions as f
# area = f.(5,10)                                      CREATING OWN FUNCTION/MODULES
# print(area)

# def calculate_area(base,height):
#     print("__name__ :",__name__ )
#     return 1/2 * base * height
# if __name__ == "__main__" :                          __name__ == "__main__"  CONCEPT 
#     print("i am in hello.py")
#     a = calculate_area(20,10)
#     print("area",a)

# x = int(input("enter 1 number :"))
# y = int(input("enter 2 number :"))
# try:
#      z = x/y
# except Exception as e:                                  TRY AND EXCEPT CONCEPT
#      print("exception occured",e)
#      z = None
# print("division is ",z)

# class human:
#     def __init__(self,n,o) :
#         self.name = n
#         self.occupation = o
#     def do_work(self):
#         if self.occupation == "tennis player" :
#             print(self.name, "plays tennis")
#         elif self.occupation == "actor" :
#             print(self.name, "shoots movie")
#     def do_speaks(self):                                      tells us about class and its method
#        print(self.name, "how you doing" )
# tom = human("shivang","actor")
# print(tom.do_work())
# print(tom.do_speaks())
# maria = human("rohan","tennis player")
# print(maria.do_work())
# print(maria.do_speaks())
