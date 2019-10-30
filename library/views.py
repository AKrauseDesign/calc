import numpy as np
from django.shortcuts import render
from library.models import Type, DefaultParameters, FieldsBuilder, Calculator, Owner, Company, Client, CalculatorLicense
from library.math.simple_interest_formula import *

from django.views import generic


# Create your views here.
def index(request):
    """View function for home page of site."""

    # Test math
    pmt_test = np.ipmt(0.6 / 12, 2 * 12, 1 * 12, 10000)

    # Generate counts of some of the main objects
    num_clients = Client.objects.all().count()
    num_calculators = Calculator.objects.all().count()
    num_companies = Company.objects.all().count()
    num_type = Type.objects.all().count()

    # get default rates
    num_rates = DefaultParameters.objects.all()

    # Generate list of calculators
    calculator_list = Calculator.objects.all()

    # Number of licenses available status = 'a'
    num_licenses_available = CalculatorLicense.objects.filter(status__exact='a').count()
    num_licenses_unavailable = CalculatorLicense.objects.filter(status__exact='u').count()

    context = {
        'pmt_test': pmt_test,
        'num_clients': num_clients,
        'num_calculators': num_calculators,
        'num_companies': num_companies,
        'num_type': num_type,
        'num_licenses_available': num_licenses_available,
        'num_licenses_unavailable': num_licenses_unavailable,
        'calculator_list': calculator_list,
        'num_rates': num_rates,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


class CalculatorListView(generic.ListView):
    model = Calculator
    context_object_name = 'calculator_list'
    # queryset = Calculator.objects.all()
    template_name = 'calculators/list.html'


class CalculatorDetailView(generic.ListView):
    model = Calculator
