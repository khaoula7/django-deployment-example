from django import template

register = template.Library()

#Register filter: method 1: using decorators
@register.filter(name='cutting')
def cut(value, arg):
    """
        This cuts out all values of args from the string!
    """
    return value.replace(arg, '')

#Register filter: method 2
#The first arg is the name of the filter, the second is the calling of cut function
#register.filter('cutting', cut)
