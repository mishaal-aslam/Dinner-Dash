from django import template

register = template.Library()

@register.filter(name='multiply')
def multiply(quantity, price):
    return quantity * price
