from django.conf.urls import url 
from . import views

app_name = 'basic'
urlpatterns=[
    url(r'^$',views.school_list_view.as_view(),name = 'list'),
    url(r'^(?P<pk>[-\w]+)/$',views.school_detail_view.as_view(),name='detail'),
    # url(r'^(?P<pk>[-\w]+)/$)',views.students_list_view.as_view(),name='students'),
    # سوال خیلی جالب اینه که چطوری میشه بریم یه ویوی دیگه برای دانش آموزای این مدرسه درست 
    # کردس
    url(r'^create/$',views.create_school_view.as_view(),name='create'),
]