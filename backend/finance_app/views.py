from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import TemplateView

from .forms import TransactionForm
from .models import Transaction


def index(request):
    return HttpResponse("Hello, world. You're at the Finance App index.")


class HomePageView(TemplateView):
    template_name = "pages/home.html"


def transactions(request):
    transactions = Transaction.objects.all()
    return render(request, "pages/transactions.html", {"transactions": transactions})


def add_transaction(request):
    if request.method == "POST":
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("transactions")
    else:
        form = TransactionForm()
    return render(request, "pages/add_transaction.html", {"form": form})
