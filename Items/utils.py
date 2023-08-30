
from Items.Models.customer import Customer


def emailexists(email):
    return Customer.objects.filter(email=email).exists()


def validate_password(password, confirm_password):
    if (password != confirm_password):
        return 'Password and Confirm Password must be same'
    elif (not password):
        return 'Please enter password'
    elif len(password) < 8:
        return 'Password must be atleast 8 characters long'
    elif not any(char.isdigit() for char in password):
        return 'Password must contain at least 1 digit'
    elif not any(char.isalpha() for char in password):
        return 'Password must contain at least 1 letter'
    else:
        return False
