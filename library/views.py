from django.shortcuts import render
from library.models import Type, FieldsBuilder, Calculator, Owner, Company, Client, CalculatorLicense
from library.math.simple_interest_formula import *


# Create your views here.
def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_clients = Client.objects.all().count()
    num_calculators = Calculator.objects.all().count()
    num_companies = Company.objects.all().count()
    num_type = Type.objects.all().count()

    # Number of licenses available status = 'a'
    num_licenses_available = CalculatorLicense.objects.filter(status__exact='a').count()
    num_licenses_unavailable = CalculatorLicense.objects.filter(status_exact='u').count()

    context = {
        'num_clients': num_clients,
        'num_calculators': num_calculators,
        'num_companies': num_companies,
        'num_type': num_type,
        'num_licenses_available': num_licenses_available,
        'num_licenses_unavailable': num_licenses_unavailable,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
