from Django import template

register = template.Library()

def cut(value, arg):
    # This function cuts out all value of 'arg' from a string(value)
    return value.replace(arg, '')

register.filter('cut', cut)
