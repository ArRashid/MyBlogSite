from django import template
register = template.Library()


@register.filter
def sub(value,arg):
    result = value - arg
    return result



@register.filter
def like_dislike_count(value,arg):
    result = 'error from funsation'
    if arg == 0 or arg == 'like':
        result =  value.filter(is_like=True).count()
    elif arg == 1  or arg == 'dislike':
        result = value.filter(is_like=False).count()
    else:
        result = "error from funsation else"
    return result
