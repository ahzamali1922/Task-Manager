from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .forms import LoginForm
from django.contrib.auth import login

# Create your views here.


# View to register a user
def register_view(request):

    if request.method == 'POST': #After filling the form Check/Validation

        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')

    else:
        form = RegistrationForm() #Default : User fills a form

    return render(
        request,
        'accounts/register.html',
        {'form': form}
    )


# Login view

def login_view(request):
    if request.method == 'POST' :
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)

            return redirect('task_list')

    else:
        form = LoginForm()

    return render(
        request,
        'accounts/login.html',
        {'form': form}
    )