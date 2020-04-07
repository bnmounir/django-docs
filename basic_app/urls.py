from django.conf.urls import url
from . import views

app_name = 'basic_app'

urlpatterns = [
    # url(r'^base/', views.base, name="base"),
    # url(r'^about/', views.about, name="about"),
    url(r'^register/', views.register, name="register"),
    url(r'^login/', views.login, name="login"),
    url(r'^logout/', views.logout, name="logout"),
]