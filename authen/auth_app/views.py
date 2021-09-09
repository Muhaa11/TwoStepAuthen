import django
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from codes.forms import CodeForm
from users.models import CustomUser
from . utils import send_msg
from . forms import UserRegisterForm



@login_required
def home(request):
    return render(request, 'home.html')





def fst_login(request):
    form = AuthenticationForm()
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            request.session['pk'] = user.pk
            return redirect('verify-log')
    return render(request, 'fstLogin.html', {'form': form})





def scd_login(request):
    form = CodeForm(request.POST or None)
    pk = request.session.get('pk')
    if pk:
        user = CustomUser.objects.get(pk=pk)
        code= user.code
        code_user = f"{user.username}: {user.code}"
        if not request.POST:
            send_msg(code_user, user.phone_number)
        if form.is_valid():
            num = form.cleaned_data.get('number')

            if str(code) == num:
                code.save()
                login(request, user)
                return redirect('home')
            else:
                return redirect('fst-log')
    return render(request, 'scdLogin.html', {'form': form})






def register(request):
    if request.method == "POST": 
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hello {username}, your account has been created')
            return redirect('home')
    
    else:
        form = UserRegisterForm()

                
    
    return render(request, 'register.html', {'form':form} )
