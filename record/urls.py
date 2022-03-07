from django.urls import path
from . import views

urlpatterns = [
    path('record/submit_expense/', views.submit_expense, name = 'submit_expense'),
    path('record/submit_income/', views.submit_income, name = 'submit_income'),
    path('accounts/register/', views.register, name = 'register'),
]
