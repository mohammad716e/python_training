import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE",'class_based_views.settings') # not final.settings.py !!!!
import django 
django.setup()
from faker import Faker 
import random
fa_fake_gen = Faker('fa_IR')
from basic.models import school,student
# en_fake_gen = Faker()
schools = []
all_schools = school.objects.all()
for x in all_schools:
    schools.append(x)
def populate(n=12):
    for entry in range(n):
        fake_name = fa_fake_gen.name().split()

        # قبلا ایندکی ها 
        # fake_fname = fake_name[0]
        # fake_lname = fake_name[1]
        # بودند اما برای اینکه سرکار و خانم و جناب و آقا دارد
        # ما ایندکس ها را به -1 و -2 تغییر میدهیم
        fake_fname = fake_name[-2]
        fake_lname = fake_name[-1]
        full_fake_name = fake_fname +' ' + fake_lname
        # fake_email = fa_fake_gen.email()

        #  create new entry now
        s = student.objects.get_or_create(name=full_fake_name,age =random.randint(8,14),school=schools[0])[0]

if __name__ == "__main__":
    print('populating persian data')
    populate(20)
    print('persian fake data populated')


# ============================================================================
'''
# read the docs
# https://github.com/joke2k/faker

# from faker import Faker
# fake = Faker('it_IT')
# for _ in range(10):
# #     print(fake.name())
# ar_EG - Arabic (Egypt)
# ar_PS - Arabic (Palestine)
# ar_SA - Arabic (Saudi Arabia)
# bg_BG - Bulgarian
# bs_BA - Bosnian
# cs_CZ - Czech
# de_DE - German
# dk_DK - Danish
# el_GR - Greek
# en_AU - English (Australia)
# en_CA - English (Canada)
# en_GB - English (Great Britain)
# en_NZ - English (New Zealand)
# en_US - English (United States)
# es_ES - Spanish (Spain)
# es_MX - Spanish (Mexico)
# et_EE - Estonian
# fa_IR - Persian (Iran)
# fi_FI - Finnish
# fr_FR - French
# hi_IN - Hindi
# hr_HR - Croatian
# hu_HU - Hungarian
# hy_AM - Armenian
# it_IT - Italian
# ja_JP - Japanese
# ka_GE - Georgian (Georgia)
# ko_KR - Korean
# lt_LT - Lithuanian
# lv_LV - Latvian
# ne_NP - Nepali
# nl_NL - Dutch (Netherlands)
# no_NO - Norwegian
# pl_PL - Polish
# pt_BR - Portuguese (Brazil)
# pt_PT - Portuguese (Portugal)
# ro_RO - Romanian
# ru_RU - Russian
# sl_SI - Slovene
# sv_SE - Swedish
# tr_TR - Turkish
# uk_UA - Ukrainian
# zh_CN - Chinese (China)
# zh_TW - Chinese (Taiwan)'''