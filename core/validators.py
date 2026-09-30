from django.core.validators import ValidationError
from country_list import countries_for_language

countries = dict(countries_for_language('en'))

def validate_country(country):
    if country not in list(countries.values()):
        raise ValidationError("Country is not available for shipping")
    
def validate_email(email):
    if '@gmail.com' not in email:
        raise ValidationError("Email should ends with \'@gmail.com\'")