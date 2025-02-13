from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.views import *
from .models import *
from datetime import datetime
from user.models import *


class HomeView(TemplateView):
    template_name = "bo'limlar.html"


class ProductsView(View):

    def get(self, request):
        if request.user.is_authenticated:
            debts = Debt.objects.all()
            total_debt = f"{sum(debt.debt for debt in debts):,.1f} So'm".replace(",", ".")
            context = {
                'debts': debts,
                'today': datetime.today(),
                'total_debt': total_debt}
            return render(request, 'mahsulotlar.html', context)
        return redirect('login')

    def post(self, request):
        if request.user.is_authenticated:
            Debt.objects.create(
                customer = request.POST.get('customer'),
                customer_birth_date = request.POST.get('customer_birth_date'),
                date = request.POST.get('date'),
                products = request.POST.get('products'),
                debt = request.POST.get('debt'),
            )
            return redirect('products')
        return redirect('login')

    




class DebtDeleteView(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            debt = get_object_or_404(Debt, pk=pk)
            context = {
                'debt': debt
            }
            return render(request, 'mahsulot_ochirish.html', context)
        return redirect('login')

    def post(self, request, pk):
        debt = get_object_or_404(Debt, pk=pk)
        debt.delete()
        return redirect('products')

class DebtUpdateView(View):
    def get(self, request, pk):
        if request.user.is_authenticated:
            debt = get_object_or_404(Debt, pk=pk)
            context = {
                'debt': debt
            }
            return render(request, 'mahsulot-tahrirlash.html', context)
        return redirect('login')

    def post(self, request, pk):
        if request.user.is_authenticated:
            debt= Debt.objects.filter(pk=pk)
            if debt.exists():
                debt.update(
                    customer = request.POST.get('customer'),
                    customer_birth_date = request.POST.get('customer_birth_date'),
                    date = request.POST.get('date'),
                    products = request.POST.get('products'),
                    debt = request.POST.get('debt'),
                )
                return redirect('products')
            return redirect('login')