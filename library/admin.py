from django.contrib import admin
from library.models import Owner, Type, DefaultParameters, CalculatorLicense, FieldsBuilder, Company, Client, Calculator

# Register your models here.
@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    list_display = (
        'last_name',
        'first_name',
        'email_address',
    )
    list_display_links = 'last_name',
    fields = [('first_name', 'last_name'), 'email_address']


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    list_display = 'name',
    list_display_links = 'name',


@admin.register(DefaultParameters)
class DefaultParametersAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'default_rate',
        'default_months',
        'default_principal',
        'id'
    )
    list_display_links = 'title',


@admin.register(CalculatorLicense)
class CalculatorLicenseAdmin(admin.ModelAdmin):
    list_display = (
        'license_created_at',
        'license_expiration',
        'id',
        'meta_owner',
        'status',
    )
    list_display_links = 'id',


@admin.register(FieldsBuilder)
class FieldBuilderAdmin(admin.ModelAdmin):
    pass


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'address',
        'phone',
    )
    list_display_links = 'name',


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = (
        'company',
        'last_name',
        'first_name',
        'email_address',
        'phone_number',
    )
    list_display_links = 'company',
    fields = [('first_name', 'last_name'), 'email_address', 'phone_number', 'company']


@admin.register(Calculator)
class CalculatorAdmin(admin.ModelAdmin):
    list_display = 'title',
