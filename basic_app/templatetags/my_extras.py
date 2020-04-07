from django import template

register = template.Library()

# def cutter(value, arg):
#     return value.replace(arg, '')

# register.filter('cutter', cutter)


@register.filter(name="cutter")
def cutter(value, arg):
    return value.replace(arg, '')