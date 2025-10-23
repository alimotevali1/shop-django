from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login ,logout
from django.views import View

from cart.models import Order
from .forms import LoginForm, RegisterForm ,AddressForm
from .models import User


class Login(View):
    def get(self, request):
        login_form = LoginForm()
        register_form = RegisterForm()  # 👈 اضافه شد
        return render(request, 'acount_app/register.html', {
            'login_form': login_form,
            'register_form': register_form
        })

    def post(self, request):
        login_form = LoginForm(request.POST)
        register_form = RegisterForm()  # 👈 همیشه خالی باشد
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                next_page = request.GET.get('next')
                if next_page:
                    return redirect(next_page)
                return redirect('Home:home')
            else:
                login_form.add_error("username", "نام کاربری یا رمز اشتباه است")
        else:
            login_form.add_error("username", "لطفا فیلدها را درست پر کنید")

        return render(request, 'acount_app/register.html', {
            'login_form': login_form,
            'register_form': register_form
        })


class Register(View):
    def get(self, request):
        register_form = RegisterForm()
        login_form = LoginForm()  # 👈 اضافه شد
        return render(request, 'acount_app/register.html', {
            'register_form': register_form,
            'login_form': login_form
        })

    def post(self, request):
        register_form = RegisterForm(request.POST)
        login_form = LoginForm()  # 👈 همیشه خالی باشد
        if register_form.is_valid():
            cd = register_form.cleaned_data
            user = User.objects.create_user(
                username=cd['username'],
                password=cd['password1']
            )
            login(request, user)
            return redirect('Home:home')

        return render(request, 'acount_app/register.html', {
            'register_form': register_form,
            'login_form': login_form
        })



def logout_view(request):
    logout(request)
    return redirect('Home:home')

class Addessview(View):
    def get(self, request):
        form = AddressForm()
        return render(request, 'acount_app/address.html', {'form': form})

    def post(self, request):
        form = AddressForm(request.POST)
        if form.is_valid():
            address=form.save(commit=False)
            address.user=request.user
            address.save()
            next_page=request.GET.get('next')
            if next_page:
                return redirect(next_page)

            return redirect('acount_app:address')
        return render(request, 'acount_app/address.html', {'form': form})





