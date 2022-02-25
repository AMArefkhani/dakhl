from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponse, JsonResponse
from record.models import Expense, Income, Token
from django.contrib.auth.models import User
from json import JSONEncoder
from django.views.decorators.csrf import csrf_exempt
 
# Create your views here.
@csrf_exempt
def submit_expense(request):
#TODO: validate data
    this_user = User.objects.filter(token__token=request.POST['token']).get()
    if 'date' not in request.POST:
        this_date = timezone.now()
    else:
        this_date = request.POST['date']
    Expense.objects.create(text=request.POST['text'], date = this_date, amount=request.POST['amount'], user=this_user)
    return JsonResponse({
        'status':'ok',
        },encoder=JSONEncoder)
@csrf_exempt
def submit_income(request):
    this_user = User.objects.filter(token__token=request.POST['token']).get()
    if 'date' not in request.POST:
        this_date = timezone.now()
    else:
        this_date = request.POST['date']
    Income.objects.create(text=request.POST['text'], date = this_date, amount=request.POST['amount'], user=this_user)
    return JsonResponse({
        'status':'ok',
        },encoder=JSONEncoder)



