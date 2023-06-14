from django.shortcuts import render, redirect
from django.contrib import auth



def loadIndexPage(request):
    return render(request, 'pages/index.html')



def logout(request):
    
    if request.method == 'POST':
        auth.logout(request)
    return redirect('login')
