from django.shortcuts import render
from django.http import HttpResponse
from .models import Food
from .forms import fooditemform
def index(request):
    return HttpResponse('you are a maderchod')
def add_fooditem(request):
    if request.method=='POST':
        forms=fooditemform(request.POST)
        if forms.is_valid():
           type2=forms.cleaned_data['type2']
           name1=forms.cleaned_data['name1']
           vitaminpresent=forms.cleaned_data['vitaminpresent']
           new_food=Food(vitaminpresent=vitaminpresent,type2=type2)
           
           new_food.save()
           return HttpResponse('MY NAME ID PRIYANSHU')
        else:
            forms=fooditemform(request.POST)
            return render(request,'add_fooditem.html',{'form':forms})
    else:
        forms=fooditemform()
        return render(request,'add_fooditem.html',{'form':forms})

def update(request):
    try:
        word='priyanshu'
        new_food=Food.objects.get(name1=word)
        new_food.delete()
    except Exception as e:
        return render(request,e.message())
    return HttpResponse('the object has been deleted')

