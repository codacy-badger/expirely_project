from django.urls import path
from expirely import views

app_name = 'expirely'

urlpatterns = [
    path('', views.index, name='index'),
]