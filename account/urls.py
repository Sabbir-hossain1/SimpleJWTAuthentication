from django.urls import path, include
from account.views import UserRegistrationView, UserLoginView, UserProfileView, UserChangePassword, SendPasswordResetEmailView, UserPasswordResetView

urlpatterns = [   
   path('register/', UserRegistrationView.as_view(), name='registration'),
   path('login/', UserLoginView.as_view(), name='login'),
   path('profile/', UserProfileView.as_view(), name='profile'),
   path('changepassword/', UserChangePassword.as_view(), name='changepassword'),
   path('send-password-rest-email/', SendPasswordResetEmailView.as_view(), name='send_password_reset_email'),
   path('reset-password/<uid>/<token>/', UserPasswordResetView.as_view(), name='reset_password'),
]
