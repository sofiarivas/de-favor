from django.shortcuts import render
from .forms import UserRegistrationForm


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(
                user_form.cleaned_data['password']
            )
            new_user.save()
            template = 'cuentas/register_done.html'
            ctx = {'new_user': new_user}
            return render(request, template, ctx)
    else:
        user_form = UserRegistrationForm()
    return render(request, 'cuentas/register.html', {'user_form': user_form})
