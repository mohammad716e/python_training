from django.conf.urls import url
from user_show import views
urlpatterns=[
    url(r'^$',views.users,name='index')
]