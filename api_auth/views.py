from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.urls import reverse
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages, auth
from django.conf import settings

from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site

from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str, DjangoUnicodeDecodeError
from .utils import generator_token

from django.core.mail import EmailMessage


from .models import Profile, Users
from .forms import UserForm, LoginForm, TokenForm

import random
import time


user_model = get_user_model()

def activate_token(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = Users.objects.get(pk=uid)
    except (ValueError, Users.DoesNotExist):
        user = None
    
    if user is not None and generator_token.check_token(user, token):
        user.is_email_verified = True
        user.save()
        messages.success(request, 'Successfully verified email')
        return redirect(reverse('login'))
    else:
        messages.error(request, 'Verification link was invalid')
        return redirect(reverse('home'))




def sendActivationMail(user, request):
    current_site = get_current_site(request)
    email_subject = 'Verify your account'
    # context = {
    #     'click_action': 'showDomainLink',
    # }
    email_body = render_to_string(
        'pages/confirm.html',
        {
        'user': user,
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': generator_token.make_token(user),
        }, 
        # context 
    )

    email = EmailMessage(
        subject=email_subject,
        body=email_body,
        from_email=settings.EMAIL_HOST_USER,
        to=[user.email]
    )
    email.content_subtype = 'html'
    email.send()




def loadSignupPage(request):
    form = UserForm()
    context = {
        'form': form,
    }
    if request.method == 'POST':
        print(request.POST)
        form = UserForm(request.POST)
        

        if form.is_valid():
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            fullname = form.cleaned_data['fullname']
            birthday = form.cleaned_data['birthday']
            location = form.cleaned_data['location']
            if Users.objects.filter(email=email).exists():
                messages.error(request, 'email already exists')
            else:
                print(email, username, fullname, birthday, location)
                user = Users.objects.create_user(email=email)
                profile = Profile.objects.create(user=user, username=username, fullname=fullname, birthday=birthday, location=location, slug=username)
                profile.save()
                messages.success(request, 'registration sucessful!')
                time.sleep(3)
                sendActivationMail(user, request)
                

    return render(request, 'pages/signup.html', context)



def randomTokens():
    tokens = ''
    for i in range(6):
        val = str(random.randint(1, 9))
        tokens += val
    return tokens
        # print(val)
        # print(tokens)

code = randomTokens()


def sendToken(user, request):
    current_site = get_current_site(request)
    
    email_subject = 'Account Token'
    email_body = render_to_string(
        'pages/mail_token.html', 
        {
        'email': user,
        'domain': current_site.domain,
        'token': code,
        }
    )
    print(code)

    try:
        email = EmailMessage(
            subject=email_subject,
            body=email_body,
            from_email=settings.EMAIL_HOST_USER,
            to=[user.email]
        )
        email.content_subtype = 'html'
        email.send()

    except Exception as e:
        print('did not work')





def loadLoginPage(request):

    form = LoginForm()
    context={
        'form': form,
    }
    if request.method == 'POST':
        form = LoginForm(request.POST)
        print('hey')
        if form.is_valid():
            email = form.cleaned_data['email']
            
            if Users.objects.filter(email=email).exists():
                
                # em = Users.objects.filter(email=email)
                
                user = authenticate(request, username=email)
                
                if user is not None:
                    login(request, user)
                    messages.info(request, 'check email for token')
                    sendToken(user, request)
                    time.sleep(1.5)
                    return redirect('token')
            else:
                messages.warning(request, 'email does not exist')
                time.sleep(1)
                return redirect('signup')    
            

    return render(request, 'pages/login.html', context)



def loadTokenPage(request):
    check_token = code 
    form = TokenForm()
    context = {
        'form': form,
    }
    if request.method == 'POST':
        form = TokenForm(request.POST)
        if form.is_valid():
            token = form.cleaned_data['token']
            if token == check_token:
                messages.success(request, 'Successful!')
                return redirect('home')
            else:
                messages.error(request, 'Invalid token')
                logout(request)
                return redirect(reverse('login'))
        else:
            messages.error(request, 'invalid form')
            return render(request, 'pages/token.html', context)
            
    return render(request, 'pages/token.html', context)




