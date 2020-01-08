from django.shortcuts import render,redirect
from .models import entry
from .forms import EntryForm


def index(request):
    context=entry.objects.order_by('-date_posted')
    return render(request,'base.html',{'context':context})

def add(request):
    if request.method=='POST':
        form= EntryForm(request.POST)
        
        if form.is_valid():
            form.save()
        return redirect('/')
    form= EntryForm()
    context={'form':form}
    return render(request,'add.html',context)