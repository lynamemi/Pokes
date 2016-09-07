from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^pokes$', views.pokes, name="pokes"),
    url(r'^poke_process$', views.poke_process, name="poke_process"),
]
