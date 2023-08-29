from django import template

register=template.Library()

@register.filter(name='currency')
def currency(price):
   return "Rs./- "+str(price) 

@register.filter(name='multiply')
def multiply(price1 , price2):
   return price1 * price2 

