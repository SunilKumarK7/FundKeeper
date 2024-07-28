from django import template

register = template.Library()


@register.filter
def percentage(value,total):
    return 0 if total==0 else round((value/total)*100)