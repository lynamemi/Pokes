from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.loginreg),
    url(r'^reg_process$', views.reg_process),
    url(r'^log_process$', views.log_process),
    url(r'^logout$', views.logout),
]
