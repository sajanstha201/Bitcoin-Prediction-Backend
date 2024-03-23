from django.urls import path
from .views import Register,Login,getUserDetail
urlpatterns = [
    path('register/',Register.as_view(),name='register_url'),
    path('login/',Login.as_view(),name='login_url')
]
