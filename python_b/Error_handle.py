# فرم کلی حل ارور اینگونه است
'''
try :
    some block of code
except exception I :
    if exception I then execute some other code
except exception II :
    if exeption II thewn this block of code
finally :
    always does execute
'''
try :
    ''' 
    simple.text fie was created in one leve upper root folder
    '''
    f=open('simple.txt','r')
    f.write('test write here man')
except IOError :
    print('Error : could- - not- - find- - what- - you- - wanted')
# else:
#     print('success')
#     f.close()
# print('hello world') # این هلو وراد به این علت اجرا میشه که با try 
finally:
    print(' i always work man')
# سریع ارور رو رفع کردیم والا اجرا نمیشد 
#  و finallly  همیشه اجرا میشه و ربطی به ارور دادن یا ندادن نداره و
#  توی بلاک try  قرار میگیره
