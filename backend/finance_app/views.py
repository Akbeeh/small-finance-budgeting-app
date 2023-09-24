from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

from .forms import RegisterForm, TransactionForm
from .models import Transaction


@method_decorator(login_required, name="dispatch")
class HomePageView(TemplateView):
    template_name = "pages/home.html"


class RegisterPageView(TemplateView):
    template_name = "pages/register.html"

    def get(self, request, *args, **kwargs):
        form = RegisterForm()
        return render(request, "pages/register.html", {"register_form": form})

    def post(self, request, *args, **kwargs):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user:
                messages.success(request, "Account created successfully")
                return redirect("login")
        messages.error(request, "Account creation failed")
        return redirect("register")


class LoginPageView(TemplateView):
    template_name = "pages/login.html"

    def get(self, request, *args, **kwargs):
        form = AuthenticationForm()
        return render(request, "pages/login.html", {"login_form": form})

    def post(self, request, *args, **kwargs):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                messages.info(request, f"Logged in successfully as {username}")
                return redirect("home")
        messages.error(request, "Invalid username or password")
        return redirect("login")


def logout_view(request):
    logout(request)
    return redirect("login")


@login_required
def dashboard(request):
    transactions = Transaction.objects.all()
    return render(request, "pages/home.html", {"transactions": transactions})


@login_required
def transactions(request):
    transactions = Transaction.objects.all()
    return render(request, "pages/transactions.html", {"transactions": transactions})


@login_required
def add_transaction(request):
    if request.method == "POST":
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("transactions")
    else:
        form = TransactionForm()
    return render(request, "pages/add_transaction.html", {"form": form})
