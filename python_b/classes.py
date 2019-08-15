#  همه چیز دا خل پاستون کلاس هستند 
print( type( 20 ) )  # <class 'int'>
print( type( 21.0 ) ) # <class 'float'>
print( type( [] ) ) # <class 'list'>
print( type( () ) ) # <class 'tuple'>
print( type( {} ) ) # <class 'dict'>
# حالا اگر کلاس خودمان را بسازیم و از آن نمونه بگیریم
# و تایپ آن را مشخص کنیم
class sample():
    pass

print( type( sample ) ) # <class 'type'> بدون نمونه

x = sample() # نمونه گرفته شده
print( type( x ) ) # <class '__main__.sample'> ?????????????
# ----------------------------------------------------------
# <class '__main__.sample'>
# class = blue prints
# هر کلاسی اتریب و متد داره
# ا        اتریب یعنی سخصیت و ویژگی# atribs = characteristic
# متد یعنی عملیات ها                # methods = opearations
# خب حالا روش بیان کردن اتریب چجوریه
# مثال
class Dog():
    # تابع اینیت برای این است که در زمان گرفتن از کلاس همانجا اتریب بدهد
    # وچون یک تابع داخل کلاس الکی نیست در آن سلف میدهیم
    # اینیت در واقع به ما ارور میدهد اگر موقع گرفتن کلاس خواسته هاشو ندیم
    # ----------------------------------------------
    # def __init__(zelf,breed,name):
    # zelf.breed = breed
    # # دومی برای مشخصه ی تابع  = اولی براکلاس 
    # اینم که بجای سلف نوشتیم زلف هم کار میکنه در واقع
    # تابع اینیت اولین آرگومانش اسم آبجکتیه مه میسازه و دومی به بعدش هم
    # اسم چیزایی مه توی اون موقع ساختن میریزه
    # وقتی میگیم سلف دات نام یعنی توی سلف بک نام بساز وقتی میگیم برابر است با نام
    # یعنی اونی که توی سلف هیت با اونی که تابع اینیت میگیره پربشه
    # ----------------------------------------------
    # CLASS LEVEL ATTRIBUTES
    nazhad='PESTANDAR'
    def __init__(self,breed,name):
        self.breed = breed
        # دومی برای مشخصه ی تابع  = اولی براکلاس 
        
my_dog = Dog(breed='lab',name='cuttie')
print(type(my_dog))
print(my_dog.breed)
other_dog = Dog(breed='huskie',name='maxie')
print(other_dog.breed)
print(other_dog.nazhad)


class circle():

    pi = 3.14
    # مقدار دیفالت هم میشه داد
    def __init__(self,radius=1):
        self.radius =radius
    # چرا به متد ها سلف میدهیم چون که این ها نباید توابع شناور آزاد در کلاس باشند بلکه در آبجکت سلف ذخیره شوند
    def area(self):
        # return radius*radius*pi روش غلط
        # روش درست
        return self.radius*self.radius*circle.pi 
    def set_radius(self,new_radius):
        self.radius = new_radius



my_c =circle(3)
print(my_c.area) # چواب <bound method circle.area of <__main__.circle object at 0x03BD0350>>
# درست
my_c.radius = 600
print(my_c.area())
his_c=circle()
his_c.set_radius(new_radius=620)
print(his_c.area) # <bound method circle.area of <__main__.circle object at 0x03BD01F0>>
print(his_c.area())


# ===============================================================================================

# مثال
class employee():
    pass

emp_1 = employee()
emp_2 = employee()

emp_1.name='mamad'
emp_2.name='hasan'
# بجای اینطوری زمان گرفتن از کلاس اسامی رو میدیم
# و دستی نوشتن هر دفعه از متد اینیت استفاده میکنیم

class Employee():
    def __init__(self,first,last,pay):
        self.first =first
        self.last = last
        self.pay = pay
        self.email = self.first + "." + self.last +"@Company.com"
    def full_name(self):
        return f" {self.first} {self.last} gets {self.pay}"
print('===========================================================')
Emp1=Employee( 'mohammad' , 'mohammadian' , '600000')
print(Emp1.email)  # جواب mohammad.mohammadian@Company.com
Emp1.name = "asghr"
print(Emp1.email) # جواب mohammad.mohammadian@Company.com
# جواب مورد انتظار asghr.mohammadian@Company.com
# یک مشکل

# حالا فرضا اگر بخوایم که اسم و فامیل و حقوقشو توی یه ط بنویسیم چی
print(f" {Emp1.first} {Emp1.last} gets {Emp1.pay}")
#  اما چوم هر دفعه نوشن این سخته متد میدیم
# و هر متدی توی کلاس به طور اتوماتیک هضو اولش رو همون اینستنش میگیره که بهش میگن سلف
print(Emp1.full_name())
# که مشابه هست با
print(Employee.full_name(Emp1))
# که در واقع بالایی به پایینی تبدیل میشه بنابراین ما باید در متد سلف رو بذاریم تا با اینستنس جایگذاری بشه
