from django import template

register = template.Library()

@register.simple_tag
def replace(str):
    return str.upper()

    