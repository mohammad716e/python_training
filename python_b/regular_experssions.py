import re
'''#  ساختن سرچ انجین با استفاده از پترن ها
# که از اسپلیت کردن استرینگ بدست میان
'''
patterns = [ 'term1' , 'term2' ]
string = 'this is a string with term1 but not the other term'

for pat in patterns :
    print('im searching for '+ pat)
    if re.search(pat,string):
        print('match')
    else:
        print('no match')
x = re.search('term1',string) # هم تولین است و هم نوعی آبجکت جداست برای خودش
print(type(x))  # <class 're.Match'>
print(x)  #  <re.Match object; span=(22, 27), match='term1'>
print(x.start)   #   <built-in method start of re.Match object at 0x017AA4F0>
print(x.start()) # 22 
print(x.end()) # 27

print(re.findall('term','hello this expression has term in it and another term in the end'))
#   
# ['term', 'term']
# در کل ماژول رگولار همیشه میخواد تا که اون الفبای ریاضی که خوندیمو
# تداعی کنه
# دنبال همینه
pattern = ['sd*' # یدونه اس و صفرتا یا بینهایت دی
'sd+', # یدونه اس با یدونه تا بینهایت دی
'sd{3}', # یدونه اس با دقیقن 3 تا دی
'sd{1,3}', # یدونه اس با 3 تا دی یا یکی دی
's[sd]+', # این براکت دقیقن مثل پرانتز میمونه که به توان به اضافه برسه
r'\d+' , #  یدونه یا بیشتر عدد باشه در  کل رگولار با کاراکتر اسکیپ فقط توی فرمت راوو استرینگ کار میکنه 
]