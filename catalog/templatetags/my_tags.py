from django import template

register = template.Library()



@register.simple_tag
def media_path(data):
    # if data:
    return '/media/' + str(data)



@register.filter
def media_path(value):
    # if value:
    return '/media/' + str(value)