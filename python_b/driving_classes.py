class animal():

    def __init__(self):
        print('ANIMAL CREATED')
    
    def eat(self):
        print('EATING')

    def who_am_i(self):
        print('ANIMAL')

# mya=animal()
# mya.eat()
# mya.who_am_i()

# حالا درایو کردن کلاس داگ از انیمال

class dog(animal):
    def __init__(self):
        # animal.__init__(self)
        print('dog created')
    def bark(self):
        print('barking')
    def eat(self):
        print('DOG EATING')

myd=dog()

myd.eat()
myd.who_am_i()

# در واقع باید دونست که کلاس ها بسیار مطالب های مفصل تری دارند 
# دو پلی لیست رو در یوتیوب اد کردم که بعدا نگاه کنم و زمانی که نگاه کنم فول میشم
# اولا اینگپسولیشن
# دومن درایو کلاس و اینا که به تدریج پیشرفته تر درآنها خواهم شد

print('===============================================')


class Employee():

    num_of_emp = 0
    raise_amount= 1.04

    def __init__(self,first,last,pay):
        self.first =first
        self.last = last
        self.pay = pay
        self.email = self.first + "." + self.last +"@Company.com"
        Employee.num_of_emp +=1
    
    def full_name(self):
        return f" {self.first} {self.last} gets {self.pay}"

    def apply_raise(self):
        self.pay =int(self.pay)*self.raise_amount
    
    @classmethod
    def set_raise_amount(cls,amount):
        cls.raise_amount = amount
    
    @classmethod
    def from_str(cls,str):
        first, last, pay= str.split(' ')
        return cls(first,last,pay)
    
    @staticmethod
    def is_wrk_day(day):
        if day.weekday() == 5 or day.weekday() == 6 :
            return False
        return True
# ============================================================


class developer(Employee):
    raise_amount =1.10
    # 1. اگر بخواهیم که برای اینت کردن بک متغیر دیگری بهکلاس بدهیم په
    def __init__(self,first,last,pay,programing_lang ):
        super().__init__(first,last,pay)
        # روش دوم
        # Employee.__init__(self,first,last,pay)
        self.programing_lang = programing_lang

dev1=developer('mohammad','mohammdian',60000,'python')
dev2 =developer('hasan','alhijri',5000,'java')

print(dev1.email)
print(dev1.programing_lang)

print('==================================')
class manager(Employee):
    #  همیشه دیتا تایپ ها ی تغییر پذیر مثل آرایه را به طور دیفالت نباید به کلاس یا تابع داد
    def __init__(self,first,last,pay,employees=None ):
        super().__init__(first,last,pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees
    
    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def rem_emp(self,emp):
        if emp in self.employees :
            self.employees.remove(emp)

    def list_emp(self):
        print (self.full_name()+' managers')
        for emp in self.employees :
            print('-->',emp.full_name())

mg1 =manager("mitra",'mohammadi',8000,[dev1,dev2])
mg1.rem_emp(dev2)
print(mg1.list_emp())