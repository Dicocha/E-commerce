from django.urls import path
from users import views

from django.contrib.auth.views import (
    LoginView,
    PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

app_name = 'users'

urlpatterns = [
    path('register/', views.register, name='register'),

    path('login/', LoginView.as_view(template_name='users/log_in.html', ), name='login'),

    path('logout/', views.log_out, name='logout'),

    path('password-reset/', PasswordResetView.as_view(template_name='users/reset_password/reset_password.html', html_email_template_name='users/reset_password/reset_password_email.html'), name='password-reset'),

    path('password-reset/done/', PasswordResetDoneView.as_view(template_name='users/reset_password/password_reset_done.html'), name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='users/reset_password/password_reset_confirm.html'), name='password_reset_confirm'),

    path('password-reset-complete/', PasswordResetCompleteView.as_view(template_name='users/reset_password/password_reset_complete.html'), name='password_reset_complete'),
]