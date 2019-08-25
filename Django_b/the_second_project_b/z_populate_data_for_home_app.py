import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','the_second_project_b.settings')
#  در اینجا ما تنطیمات پروژه ی جمگو را  آوردیم ونام متعیر ستینگز را به او دادیم
#  حالا ایمپورت خود جنگو
import django
django.setup()
# و حالا ستاپ با آدرس جدید صورت گرفت
import random
from home.models import Webpage,Topic,Accessrecord
from faker import Faker

fakegen = Faker()
# ما تاپیک ها رو به صورت دستی وارد میکنیم چون که خیلی کم هستند
# و در لایبری فیکر ه هیچ چیزی برای تاپیک رندوم ساختن نیست
fake_topics = ['sports','research','social','news', 'games' ]

def add_topic():
    t= Topic.objects.get_or_create(topic_name=random.choice(fake_topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        # get topic for entry
        top = add_topic()
        # create fake data for tha entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()
        # create new wepage entry
        webpg = Webpage.objects.get_or_create(topic=top , name=fake_name ,url=fake_url)[0]
        # create a fake acces record for that web page
        acc_rec = Accessrecord.objects.get_or_create(name=webpg , date=fake_date )[0]

if __name__ == '__main__':
    print('populating script running')
    for i in range(25):
        populate(1)
    print('populating compelete')
