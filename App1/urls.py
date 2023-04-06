from django.urls import path,include
from . import views

urlpatterns = [
    path('user/register/', views.SignUp.as_view(), name="user-register"),
    path('user/login/', views.SignIn.as_view(), name="user-login"),
    path('user/newsletter_subscription',views.Newsletter_Subscription.as_view(),name="user-newsletter"),
    path('user/catalog_subscription',views.Catalog_Subscription.as_view(),name="user-catalog")
    #path('user/change_password',views.ChangePassword.as_view(),name='Change_password')
]



