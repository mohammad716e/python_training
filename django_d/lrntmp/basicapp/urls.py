from django.conf.urls import url 
from basicapp import views

# template tagging

app_name = 'basicapp' # name is for templat tagging

urlpatterns=[
    url(r'^relative/$',views.relative,name='relative'), # name is for templat tagging
    url(r'^other/$',views.other,name='other'),
]
