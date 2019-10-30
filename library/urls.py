from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('calculators/', views.CalculatorListView.as_view(), name='calculators'),
    # path('calculators/<int:pk>', views.CalculatorDetailView.as_view(), name='calculator-detail'),
]
