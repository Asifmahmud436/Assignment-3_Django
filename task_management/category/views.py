from django.shortcuts import render,redirect
from .import form

def add_category(request):
    if request.method=='POST':
        category_form = form.CategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            return redirect('homepage')
    else:
        category_form = form.CategoryForm()
    return render(request,'add_category.html',{'form':category_form})
