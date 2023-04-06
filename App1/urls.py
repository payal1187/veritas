from django.urls import path,include
from . import views

urlpatterns = [
    path('user/register/', views.SignUp.as_view(), name="user-register"),
    path('user/login/', views.SignIn.as_view(), name="user-login"),
    path('user/change_password',views.ChangePassword.as_view(),name='Change_password')
]



