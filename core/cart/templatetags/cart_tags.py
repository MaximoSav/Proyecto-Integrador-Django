from django import template

register = template.Library()


@register.filter()
def multiply(value, arg):
    return str(float(value) * float(arg))


@register.filter()
def money_format(value, arg):
    return f"{value}{arg}"
