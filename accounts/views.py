from django.shortcuts import render, redirect
from .forms import RegistrationForm

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