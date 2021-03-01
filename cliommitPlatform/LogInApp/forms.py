from django import forms

COUNTRIES = (
    ('', 'choose country'),
    ('DE', 'Germany'),
    ('US', 'United States'),
    ('UK', 'United Kingdom'),
    ('AU', 'Australia'),
    ('CD', 'Canada'),
    ('IN', 'India'),
)
SECTOR = (
    ('', 'choose sector'),
    ('Agriculture', 'Agriculture'),
    ('IT Services', 'IT Services'),
    ('Manufacturing', 'Manufacturing'),
    ('Food and Beverage', 'Food and Beverage'),
    ('Finance', 'Finance'),
    ('Health Care', 'Health Care'),
)


class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'type': 'text', 'class': 'input100', 'name': 'username', 'placeholder': 'Username'
    }))
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={
        'type': 'password', 'class': 'input100', 'name': 'pass', 'placeholder': 'Password'
    }))
    email = forms.CharField(max_length=100, widget=forms.EmailInput(attrs={
        'type': 'email', 'class': 'input100', 'name': 'email', 'placeholder': 'Email'
    }))
    phone = forms.CharField(max_length=100, widget=forms.NumberInput(attrs={
        'type': 'tel', 'class': 'input100', 'name': 'phone', 'placeholder': '0123456789'
    }))
    company = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'type': 'text', 'class': 'input100', 'name': 'company', 'placeholder': 'Name of Company'
    }))
    country = forms.ChoiceField(choices=COUNTRIES, widget=forms.Select(attrs={
        'type': 'text', 'class': 'input100', 'name': 'country', 'placeholder': 'Country'
    }))
    address = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'type': 'text', 'class': 'input100', 'name': 'address', 'placeholder': 'Address of the Company'
    }))
    reg_no = forms.CharField(max_length=100, widget=forms.NumberInput(attrs={
        'type': 'tel', 'class': 'input100', 'name': 'reg_no', 'placeholder': 'Registration number'
    }))
    employees = forms.CharField(max_length=100, widget=forms.NumberInput(attrs={
        'type': 'number', 'class': 'input100', 'name': 'employees', 'placeholder': 'Number of employees'
    }))
    sector = forms.ChoiceField(choices=SECTOR, widget=forms.Select(attrs={
        'type': 'text', 'class': 'input100', 'name': 'sector', 'placeholder': 'Sector of the company'
    }))
    turnover = forms.CharField(max_length=100, widget=forms.NumberInput(attrs={
        'type': 'number', 'class': 'input100', 'name': 'turnover', 'placeholder': 'Annual turnover (in Euros)'
    }))
    electricity = forms.CharField(max_length=100, widget=forms.NumberInput(attrs={
        'type': 'number', 'class': 'input100', 'name': 'electricity', 'placeholder': 'Electricity (in KWh)'
    }))
    air_travel = forms.CharField(max_length=100, widget=forms.NumberInput(attrs={
        'type': 'number', 'class': 'input100', 'name': 'air_travel', 'placeholder': 'Air travel (in Kms)'
    }))
    automobile = forms.CharField(max_length=100, widget=forms.NumberInput(attrs={
        'type': 'number', 'class': 'input100', 'name': 'automobile', 'placeholder': 'Car usage (in Kms)'
    }))
    public_transport = forms.CharField(max_length=100, widget=forms.NumberInput(attrs={
        'type': 'number', 'class': 'input100', 'name': 'public_transport', 'placeholder': 'Public transport (in Kms)'
    }))
    travel_accommodation = forms.CharField(max_length=100, widget=forms.NumberInput(attrs={
        'type': 'number', 'class': 'input100', 'name': 'travel_accommodation', 'placeholder': 'Travel accommodation ('
                                                                                              'days) '
    }))
    waste = forms.CharField(max_length=100, widget=forms.NumberInput(attrs={
        'type': 'number', 'class': 'input100', 'name': 'waste', 'placeholder': 'Waste generated (in Litres)'
    }))
    water = forms.CharField(max_length=100, widget=forms.NumberInput(attrs={
        'type': 'number', 'class': 'input100', 'name': 'water', 'placeholder': 'Water consumption (in Litres)'
    }))
