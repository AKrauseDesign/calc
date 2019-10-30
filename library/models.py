from django.db import models
from django.urls import reverse
from django.utils.timezone import now
import uuid

# Create your models here.


class Type(models.Model):
    """Model representing calculator types (basic, common, advanced)"""
    name = models.CharField(max_length=200, help_text='Enter a calculator genre (e.g. Basic, Common, Advanced)')

    class Meta:
        verbose_name = "Type"
        verbose_name_plural = "Types"

    def __str__(self):
        """String for representing the Model object"""
        return self.name


# Creates the data to help build a new calculator form
class FieldsBuilder(models.Model):
    custom_input_id = models.CharField(max_length=1000, help_text="Custom input ID")
    name = models.CharField(max_length=200, help_text="Field Name")

    FIELD_TYPES = (
        ('text', 'Text Field'),
        ('number','Number Field'),
        ('email', 'Email Field'),
        ('phone', 'Phone Number Field'),
        ('radio', 'Radio Field'),
        ('checkbox', 'Checkbox Field'),
    )

    type = models.CharField(
        max_length=10,
        choices=FIELD_TYPES,
        blank=True,
        default='text',
        help_text="Specify the type of field you\'d like to use",
    )

    class Meta:
        ordering = ['name']
        verbose_name = "Input Generator"
        verbose_name_plural = "Input Generator"

    def __str__(self):
        return self.name


# FIXME: This model keeps breaking, please work on it a bit.
class Calculator(models.Model):
    """Model representing a calculator (but not a specific copy of a calculator)."""
    title = models.CharField(max_length=200)
    summary = models.TextField(max_length=2000, help_text="Enter a brief description of the calculator")
    calc_id = models.UUIDField("Calculator ID", primary_key=True, default=uuid.uuid4, help_text='Unique ID for this calculator')
    fields = models.ManyToManyField(FieldsBuilder)

    # ManyToManyField used because type can contain many calculators. Calculators can cover many types
    # Genre class has already been defined so we can specify the object above.

    class Meta:
        verbose_name = "Calculator Detail"
        verbose_name_plural = "Calculator Details"

    def __str__(self):
        """String for representing the Model object."""
        return self.title

    def get_absolute_url(self):
        """Returns the url to access a detail record for this calculator."""
        return reverse('calculator-detail', args=[str(self.id)])


class Owner(models.Model):
    """Model representing the calculator owner"""
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email_address = models.EmailField(max_length=200)

    class Meta:
        ordering = ['last_name', 'first_name', 'email_address']
        verbose_name = "Calculator Meta Owner"
        verbose_name_plural = "Calculator Meta Owner"

    def get_absolute_url(self):
        """Returns the url to access a particular owner instance."""
        return reverse('owner-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object"""
        return f'{self.email_address}'


class Company(models.Model):
    name = models.CharField(max_length=500, help_text="Company Name")
    address = models.CharField(max_length=1000, help_text="Company Address")
    phone = models.CharField(max_length=10, help_text="Company Phone Number")

    class Meta:
        ordering = ['name', 'phone', 'address']
        verbose_name = "Company"
        verbose_name_plural = "Companies"

    def get_absolute_url(self):
        return reverse('company-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.name}'


class Client(models.Model):
    """Model for client that owns the license"""
    first_name = models.CharField(max_length=200, help_text="First Name")
    last_name = models.CharField(max_length=200, help_text="Last Name")
    email_address = models.CharField(max_length=300, help_text="Email Address")
    phone_number = models.CharField(max_length=10, help_text="Phone Number")
    position = models.CharField(max_length=200, help_text="Job Position", null=True)
    company = models.ForeignKey('Company', on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['company', 'last_name', 'first_name', 'email_address', 'phone_number']
        verbose_name = "Client"
        verbose_name_plural = "Clients"

    def __str__(self):
        """String for representing the Model object"""
        return f'{self.last_name}, {self.first_name} ({self.company.name}, {self.company.phone})'


class CalculatorLicense(models.Model):
    """Model representing a specific license of a calculator"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text='Unique ID for this particular calculator '
                                    'license')
    license_created_at = models.DateField("Date License Created On", default=now, editable=False)
    license_expiration = models.DateField(null=True, blank=True)
    meta_owner = models.ForeignKey("Owner", on_delete=models.CASCADE, null=True)
    company = models.ForeignKey('Client', on_delete=models.CASCADE, null=True)

    LICENSE_STATUS = (
        ('m', 'Maintenance'),
        ('a', 'Available'),
        ('u', 'Unavailable'),
    )

    status = models.CharField(
        max_length=1,
        choices=LICENSE_STATUS,
        blank=True,
        default='m',
        help_text='License status',
    )

    class Meta:
        ordering = ['license_expiration']
        verbose_name = "Calculator License"
        verbose_name_plural = "Calculator Licenses"

    def __str__(self):
        """String for representing the Model object"""
        return f'{self.id}, Expires: {self.license_expiration}'
