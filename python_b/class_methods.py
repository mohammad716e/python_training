
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
    
    # 1.
    # با این دکوراتور دیگر بجای اینکه متد ها اتوماتیک به اینستنس بروند الآن به کلاس
    # رجوع میکنند و چون class 
    # کلمه ی ملیدی پر شده در پایتون است از cls
    # استفاده میکند
    @classmethod
    def set_raise_amount(cls,amount):
        cls.raise_amount = amount
    # 2.
    @classmethod
    def from_str(cls,str):
        first, last, pay= str.split(' ')
        return cls(first,last,pay)
    
    @staticmethod
    def is_wrk_day(day):
        if day.weekday() == 5 or day.weekday() == 6 :
            return False
        return True

    

emp1=Employee('mohammad','mohammdian',60000)
print(emp1.raise_amount)
emp2 =Employee('hasan','alhijri',5000)
print(emp2.raise_amount)
Employee.set_raise_amount(1.09)
print(emp2.raise_amount)
print(emp1.raise_amount)
print(Employee.raise_amount)
print('===================================')
# ==============================================
# 2. استفاده ی دیگر کلاس متد ها برای ساختن کانستراکتور های دیگست مثلا طرف یه اکسل داره 
# میخواد بافاصله همه ی حط ها رو بده و اینستنس بگیره

# دیتای اکسل
emp1str='hasan akbari 6000'
emp2str='mahmood asghari 5000'
emp3str='mitra heydari 5000'

# نخوه ی ایجاد دیتا
# first , last , pay = emp3str.split(' ')
# نخوه ی ساخت کلاس
# new_employee = Employee( first , last , pay )
#  اما با کلاس متد میشه روشی ساخت که از استریگ گرفتن اینستنش بده

# جالا با متد 2
mitra_acc = Employee.from_str(emp3str)
print(mitra_acc.__dict__)

# 3. بجز کلاس متد ها استاتیک متد ها هم هستند 
# گه با دکوراو staticmethod به کار میروند
#  و معمولن نه به اینستنس نه به کلاس کاری دارند فقط برای دسته بند در آنجا هستند
import datetime
my = datetime.date( 2017 , 7 , 11)
print(Employee.is_wrk_day(my))