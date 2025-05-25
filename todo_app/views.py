from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User

def home(request):
    data = User.objects.all()
    context = {
        'data': data
    }
    return render(request, 'home.html', context)

def add_data(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        age = request.POST.get('age')
        isMaried = request.POST.get('isMaried') == 'on'  # checkbox returns 'on' if checked

        user_data = User(
            name=name,
            email=email,
            address=address,
            age=age,
            isMaried=isMaried
        )

        user_data.save()
        messages.success(request, 'Data sent successfully!')
        return redirect('add_data')

    return render(request, 'add_data.html')
