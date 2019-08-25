from django.conf.urls import url 
from basic_opr_app import views

app_name = 'basic_opr_app'

urlpatterns = [
    url(r'^register$',views.register,name='register'),
    url(r'^uzr_login',views.uzr_login,name='uzr_login')
]