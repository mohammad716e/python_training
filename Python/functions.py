# function
def hello ( name = 'mmd'):
    print('hello'+'name')

def chk_int_add_num(a , b):
    """
    سلام من یک داک استرینگ هستم
    ----------------------------
    hello im a docstring
    this function returns a +b if they are integer
    cuz python can add srings too
    """
    if type(a)==type(b)==type(1):
        return()

# فیلتر 
# عجب فانکشن باحالیه
def function_tht_rtrn_true(a):
    
    return(a%2)

Sequence_inpt =[1 ,23,4,5,6,6,7,8,]

res = filter( function_tht_rtrn_true, Sequence_inpt)

print(list(res))
print(type(res))
# مثال
#  از لامبا 
def ret_boll(num):
    return num%2
print(list (filter(lambda num:num%2,Sequence_inpt)))
# جواب 
# [1, 23, 5, 7]
# <class 'filter'>
# [1, 23, 5, 7]
# فیلتر اگر true بدهد میاندازد بیرون فقط false ها را نشان میدهد
# مثال
tweet =" hello i love sports #sport"
# هم با رگولار اکسپرشن میشه هم با متد اسپلیت پایتون
hashtag1=tweet.split('#')[1]
print(hashtag1)

# in method

print('x' in [1,2,3]) #  جواب False
print('x' in [1,2,3,'x']) #  جواب True
