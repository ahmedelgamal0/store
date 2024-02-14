from multiprocessing import context
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from store.models import Product

def say_hello(request):
    products = Product.objects.all()
    data = serializers.serialize('json', products)
    return HttpResponse(data, content_type='application/json')