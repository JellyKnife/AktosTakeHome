from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Q
from accounts.models import Account


def get_accounts(request):
  min_balance = request.GET.get('min_balance', None)
  max_balance = request.GET.get('max_balance', None)
  consumer_name = request.GET.get('consumer_name', None)
  status = request.GET.get('status', None)

  accounts = Account.objects.all()

  if min_balance is not None:
    accounts = accounts.filter(balance__gte=min_balance)
  if max_balance is not None:
    accounts = accounts.filter(balance__lte=max_balance)
  if consumer_name is not None:
    accounts = accounts.filter(consumer_name__icontains=consumer_name)
  if status is not None:
    accounts = accounts.filter(status=status)

  data = list(accounts.values())

  return JsonResponse(data, safe=False)
