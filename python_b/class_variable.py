
class Employee():

    num_of_emp = 0
    raise_amount= 1.04

    def __init__(self,first,last,pay):
        self.first =first
        self.last = last
        self.pay = pay
        self.email = self.first + "." + self.last +"@Company.com"
        # چون هر بار فراخوانی میشه در زمان ساخت اینستنس پس کانتر را در همین جا مینهیم
        Employee.num_of_emp +=1
    def full_name(self):
        return f" {self.first} {self.last} gets {self.pay}"
    # روش هارد کد
    def apply_raise(self):
        # 1.
        # روش هارد کد
        # self.pay =int(self.pay*1.04)
        # 2.
        # روش بهتر با دست یابی به خود کلاس
        # self.pay =int(self.pay*Employee.raise_amount)
        # 3.
        # روش دیگر با دستیابی به اینستنس
        self.pay =int(self.pay*self.raise_amount)

# فرض کنیم که باید یک میزان افزایش حقوق در کارکنان قرار بدهیم
# روش هارد کد
emp1=Employee('mohammad','mohammdian',60000)
print(emp1.pay)
emp1.apply_raise()
print(emp1.pay)
# ولی مشکل اینجاست که کاش میشد بدانیم که مقدار افزایش جثدر است برای هر کارمند و یا برای همه کارمندان
# Employee.raise_amount
# emp1.


# 4. اگر از روش 3 استفاده کنیم میفهمیم که اینستنس ها  متغیر ملاس را ندارند
print(emp1.__dict__) # جواب {'first': 'mohammad', 'last': 'mohammdian', 'pay': 62400, 'email': 'mohammad.mohammdian@Company.com'}
# اما در صورتی که از آنها بخواهیم این متغیر را از کلاس بالایی خود میگیرند
print(emp1.raise_amount)
print(Employee.__dict__) #  جواب {'__module__': '__main__', 'raise_amount': 1.04, '.............
# اما خوبی این روش اینه که برای هر کارمند به طور جدا درصد افزایش را تغییر داد بدون تغییر دیگر درصد ها
print("========================================")
emp1.raise_amount =1.06
# و خالا که دستی گذاشتیم توی دیکتش هم هست
print(emp1.raise_amount)
emp2 =Employee('hasan','alhijri',5000)
print(emp2.raise_amount)
print(Employee.raise_amount)

print("========================================")
# 5.
# حالا از روش 2 استفاده میکنیم برای جمع تعداد همه ی کارمند ها
print(Employee.num_of_emp)
print(emp1.num_of_emp)