from django.contrib import admin
from home.models import Topic,Webpage,Accessrecord
# Register your models here.

admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(Accessrecord)

# the developer super user created by me to test the site and how it is doing
# Username (leave blank to use 'adminone'): developer
# Email address: mmohammadianxdev@gmail.com
# Password: 147741147zxc

# installed faker and iddnt use it then 
# deactivate
