from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import List
from .forms import ListForm
from django.contrib import messages





def home(request):
    if request.method == 'POST':
        form =ListForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, ('Item has been added to List!'))


    all_items = List.objects.all
    return render(request,'home.html', {'all_items':all_items})

def about(request):
    return render(request,'about.html', {})
  

        
    
