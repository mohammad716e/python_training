"""class_based_views URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from basic import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^$',views.index, name = 'index' ),
    # url(r'^$',views.CBV_idx.as_view()), # برای نرمال ویوها بود
    url(r'^$',views.temp_cbv_idx.as_view(),name = 'index'),
     # همون تمپلیت اولی رو ریترن کرد 
    url(r'^basic/', include('basic.urls',namespace = 'basic')),
     # نکته ی جدید برای این اینه که از namespace استفاده میکنیم
]
