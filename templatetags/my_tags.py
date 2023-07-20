from django import template
from config import settings
register = template.Library()



@register.simple_tag
def media_path(data):
    # if data:
    return '/media/' + str(data)



# @register.filter
# def media_path(value):
#     # if value:
#     return '/media/' + str(value)


@register.filter(name='media_path')
def media_path(value):
    if value:
        return f"{settings.MEDIA_URL}{value}"
    return "No image yet"