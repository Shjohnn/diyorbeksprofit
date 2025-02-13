from django.urls import path
from .views import *





urlpatterns = [
    path('',HomeView.as_view(), name='home'),
    path('products/', ProductsView.as_view(), name='products'),
    path('products/<int:pk>/delete',DebtDeleteView.as_view(), name='debts-delete'),
    path('products/<int:pk>/update',DebtUpdateView.as_view(), name='debts-update'),

]