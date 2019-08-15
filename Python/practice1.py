# ------------------------------------------------------
#  تمرین یک

# تابعی بنویسید که اگر در آن 1 و2و3 پشت هم بیایند در یک آرایه ی داده شده ی ما
# درست برگرداند 
def has_one_two_three(seq):
    # منهای 2 میکنیم چون باید سه تا هدد پشت هم ببینیم پس دو تای آخر رو چک نمیکنیم
    for i in range(len(seq)-2):
        if seq[i]==1 and seq[i+1]==2 and seq[i+2]==3:
            return True
    return False
# ======================================================
# امتحان
a = [7,6,5,4,3,2,1,2,3] 
print(has_one_two_three(a)) # true جواب
b=[3,8,4,0,8,4,8,4,0] # جواب false
print(has_one_two_three(b)) # true جواب
#     ok    !
print("-------------------------------------")
# ------------------------------------------------------
#  تمرین دو
# تابعی بنویسید که رشته ای را ریافت کند و یکی در میان آن را چاپ کند
def string_bit(str):
    res=""
    for i in range(len(str)):
        if i%2 == 0:
            res = res + str[i]
    return res
#  یا اینکه
def string_bit_B(str):
    return str[ :: 2]
b = "hello" # جواب hlo
a="hi" # جواب h
print(string_bit(b))
print(string_bit(a))
print(string_bit_B(b))
print(string_bit_B(a))
#     ok    !
print("-------------------------------------")
# ------------------------------------------------------
#  تمرین سه
# تابعی بتویسید که مشخص کند آیا رشته ای با رشته  ی دیگری تمام میشود یا نه
def end_other(a,b) :
    return a.endswith(b) or b.endswith(a)

def end_other_B(a,b):
    return a[-(len(b)):] == b or b[-(len(a)):] == a
a1 = 'abc hi'
b1 = 'hi'
print(end_other(a1,b1)) # true
print(end_other_B(a1,b1)) # true
a2 = 'hello man'
b2 = 'hell'
print(end_other(a2,b2)) # false
print(end_other_B(a2,b2)) # false
a3 = 'kajaki'
b3= 'shakoor'
print(end_other(a3,b3)) # false
print(end_other_B(a3,b3)) # false
#     ok    !
print("-------------------------------------")
# ------------------------------------------------------
#  تمرین چهار
#  تابعی بنویسید که هر کدام از حروف یک رشته را دو بار بنویسد
def duplex(str):
    k=""
    for i in str:
        k +=i*2
    return k
a = 'abc'
b = 'cdef'
print(duplex(b)) # جواب ccddeeff
print(duplex(a)) # جواب aabbcc
#     ok    !
print("-------------------------------------")
# ------------------------------------------------------
#  تمرین پنج
# تابعی بنویسید که اعداد تین دار را 13و14و15و116و17و18و19 جدا کند
def no_teen(seq):
    k=[]
    for i in range(len(seq)):
        if not (seq[i] in range(13,20)):
            # print(seq[i]) دیباگ
            k.append(seq[i])
    return k
a =[13 , 14 ,33,55,4]
b= [4,5,6,19]
print(no_teen(a)) # [33, 55, 4] جواب
print(no_teen(b)) # [4, 5, 6] جواب
#     ok    !
print("-------------------------------------")
# ------------------------------------------------------
#  تمرین شش
# تعداد اعضای زوج را حساب کند در یک لیست