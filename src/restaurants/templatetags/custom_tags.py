from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

censored_words = ["fuck", "asshole", "pidaras"]


@register.simple_tag
def censor(value):
    for item in censored_words:
        value = value.replace(item, "***")
    return value



