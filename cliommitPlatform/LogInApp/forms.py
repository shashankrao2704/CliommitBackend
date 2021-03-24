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


YES_NO = (('yes', 'YES'), ('no', 'NO'))
E_PROVIDER = (
    ('', 'Select Provider'),
    ('eprimo', 'Eprimo'), ('QCells', 'Q-Cells'),
    ('lekker', 'Lekker'), ('lew', 'LEW'),
    ('vattenfall', 'Vattenfall')
)
E_TYPE = (
    ('', 'Select Type'),
    ('Natural Gas', 'Natural Gas'), ('Coal', 'Coal'),
    ('Wind', 'Wind'), ('Nuclear', 'Nuclear'),
    ('Bio-mass', 'Bio-mass')
)


class CarbonRegistration(forms.Form):
    electricity_amount = forms.CharField(max_length=100, widget=forms.NumberInput(attrs={
        'type': 'number', 'class': 'input100', 'name': 'electricity_amount', 'placeholder': 'Electricity (in KWh)'
    }))
    electricity_renewable = forms.ChoiceField(choices=YES_NO, widget=forms.RadioSelect(attrs={
        'type': 'text', 'name': 'electricity_renewable'
    }))
    electricity_provider = forms.ChoiceField(choices=E_PROVIDER, widget=forms.Select(attrs={
        'type': 'text', 'class': 'input100', 'name': 'electricity_provider',
        'placeholder': 'Select Electricity Provider'
    }))
    electricity_type = forms.ChoiceField(choices=E_TYPE, widget=forms.Select(attrs={
        'type': 'text', 'class': 'input100', 'name': 'electricity_type', 'placeholder': 'Select Electricity Type'
    }))
    electricity_heating = forms.CharField(max_length=100, widget=forms.NumberInput(attrs={
        'type': 'number', 'class': 'input100', 'name': 'electricity_heating', 'placeholder': 'Heating (in KJ)'
    }))
    electricity_gas = forms.CharField(max_length=100, widget=forms.NumberInput(attrs={
        'type': 'number', 'class': 'input100', 'name': 'electricity_gas', 'placeholder': 'Gas (in Kg)'
    }))
    travel_air_travel = forms.CharField(max_length=100, widget=forms.NumberInput(attrs={
        'type': 'number', 'class': 'input100', 'name': 'travel_air_travel', 'placeholder': 'Number of flights'
    }))
    travel_automobile_mileage = forms.CharField(max_length=100, widget=forms.NumberInput(attrs={
        'type': 'number', 'class': 'input100', 'name': 'travel_automobile_mileage', 'placeholder': 'Mileage (in Km)'
    }))
    travel_automobile_commute = forms.CharField(max_length=100, widget=forms.NumberInput(attrs={
        'type': 'number', 'class': 'input100', 'name': 'travel_automobile_commute', 'placeholder': 'Daily commute (in '
                                                                                                   'Km) '
    }))
    travel_bus = forms.CharField(max_length=100, widget=forms.NumberInput(attrs={
        'type': 'number', 'class': 'input100', 'name': 'travel_bus', 'placeholder': 'Bus (in Km) '
    }))
    travel_coach = forms.CharField(max_length=100, widget=forms.NumberInput(attrs={
        'type': 'number', 'class': 'input100', 'name': 'travel_coach', 'placeholder': 'Coach (in Km) '
    }))
    travel_train = forms.CharField(max_length=100, widget=forms.NumberInput(attrs={
        'type': 'number', 'class': 'input100', 'name': 'travel_train', 'placeholder': 'National Train (in Km) '
    }))
    travel_int_train = forms.CharField(max_length=100, widget=forms.NumberInput(attrs={
        'type': 'number', 'class': 'input100', 'name': 'travel_int_train', 'placeholder': 'International Train (in Km) '
    }))
    travel_subway = forms.CharField(max_length=100, widget=forms.NumberInput(attrs={
        'type': 'number', 'class': 'input100', 'name': 'travel_subway', 'placeholder': 'Subway (in Km)'
    }))
    travel_tram = forms.CharField(max_length=100, widget=forms.NumberInput(attrs={
        'type': 'number', 'class': 'input100', 'name': 'travel_tram', 'placeholder': 'Tram(in Km)'
    }))
    travel_taxi = forms.CharField(max_length=100, widget=forms.NumberInput(attrs={
        'type': 'number', 'class': 'input100', 'name': 'travel_taxi', 'placeholder': 'Taxi (in Km)'
    }))
    travel_accommodation_hotel = forms.CharField(max_length=100, widget=forms.NumberInput(attrs={
        'type': 'number', 'class': 'input100', 'name': 'travel_accommodation_hotel', 'placeholder': 'Hotel (in days)'
    }))
    travel_accommodation_motel = forms.CharField(max_length=100, widget=forms.NumberInput(attrs={
        'type': 'number', 'class': 'input100', 'name': 'travel_accommodation_motel', 'placeholder': 'Motel (in days)'
    }))
    travel_accommodation_airbnb = forms.CharField(max_length=100, widget=forms.NumberInput(attrs={
        'type': 'number', 'class': 'input100', 'name': 'travel_accommodation_airbnb', 'placeholder': 'Airbnb (in days)'
    }))
    travel_accommodation_hostel = forms.CharField(max_length=100, widget=forms.NumberInput(attrs={
        'type': 'number', 'class': 'input100', 'name': 'travel_accommodation_hostel', 'placeholder': 'Hostel (in days)'
    }))
    office_utilities_desktop = forms.CharField(max_length=100, widget=forms.NumberInput(attrs={
        'type': 'number', 'class': 'input100', 'name': 'office_utilities_desktop', 'placeholder': 'Number of Desktops'
    }))
    office_utilities_laptop = forms.CharField(max_length=100, widget=forms.NumberInput(attrs={
        'type': 'number', 'class': 'input100', 'name': 'office_utilities_laptop', 'placeholder': 'Number of Desktops'
    }))
    office_waste_bio = forms.CharField(max_length=100, widget=forms.NumberInput(attrs={
        'type': 'number', 'class': 'input100', 'name': 'office_waste_bio', 'placeholder': 'Bio-waste (in Litres)'
    }))
    office_waste_battery = forms.CharField(max_length=100, widget=forms.NumberInput(attrs={
        'type': 'number', 'class': 'input100', 'name': 'office_waste_battery', 'placeholder': 'Batteries'
    }))
    office_waste_plastic = forms.CharField(max_length=100, widget=forms.NumberInput(attrs={
        'type': 'number', 'class': 'input100', 'name': 'office_waste_plastic', 'placeholder': 'Plastics/Packaging'
    }))
    office_waste_glass = forms.CharField(max_length=100, widget=forms.NumberInput(attrs={
        'type': 'number', 'class': 'input100', 'name': 'office_waste_glass', 'placeholder': 'Glass'
    }))
    office_waste_paper = forms.CharField(max_length=100, widget=forms.NumberInput(attrs={
        'type': 'number', 'class': 'input100', 'name': 'office_waste_paper', 'placeholder': 'Paper/Board'
    }))
    office_waste_hardware = forms.CharField(max_length=100, widget=forms.NumberInput(attrs={
        'type': 'number', 'class': 'input100', 'name': 'office_waste_hardware', 'placeholder': 'Hardware'
    }))
    office_water = forms.CharField(max_length=100, widget=forms.NumberInput(attrs={
        'type': 'number', 'class': 'input100', 'name': 'office_water', 'placeholder': 'Water (in Litres)'
    }))


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'type': 'text', 'class': 'input100', 'name': 'username', 'placeholder': 'Enter Username'
    }))
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={
        'type': 'password', 'class': 'input100', 'name': 'pass', 'placeholder': ' Enter Password'
    }))
