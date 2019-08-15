#  ما میتوانیم یک فانکشن را در درون فانکش دیگری کال کنیم و در داخل همان قانکشن آن را صدا کنیم
name = 'jackiee'
def greet():
    name ='sammy'
    def hello():
        print('hello ' + name)
    hello()

#  دقیقن همان طوریکه داخل فانکشن مین 
# main آنها را صدا میکنیم
greet()
# ----------------------
X = 50
# global X
def func():
    global X
    X =1000

#  تذکر از گلوبال استفاده نکنید جون باعث میشود name_spacing شما خراب شود
# بهتره که با ریترن از بیرون x را عوض کنیم

print('before calling func X is ' ,X)

func()

print('after calling func X is ' ,X)
