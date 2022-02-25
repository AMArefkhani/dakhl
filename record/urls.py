from django.urls import path
from . import views

urlpatterns = [
    path('submit_expense/', views.submit_expense, name = 'submit_expense'),
    path('submit_income/', views.submit_income, name = 'submit_income'),
]
