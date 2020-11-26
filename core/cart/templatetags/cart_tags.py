from django import template

register = template.Library()


@register.filter()
def multiply(value, arg):
    return str(float(value) * float(arg))


@register.filter()
def money_format(value, arg):
    return f"{value}{arg}"

@register.filter()
def dolar(value, arg):
    return str(float(value / 85.75) * float(arg))

@register.filter()
def euro(value, arg):
    return str(float(value / 96.5) * float(arg))
