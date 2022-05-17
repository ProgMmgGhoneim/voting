from django.urls import path

from .views import RegisterView, VerifyView

urlpatterns = [
   path("register", RegisterView.as_view(), name='register'),
   path("verify_otp", VerifyView.as_view(), name='verify_otp')
]