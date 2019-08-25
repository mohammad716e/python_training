from django import template

register = template.Library() # register بود یا reg فرق نداره

@register.filter(name='cut')
def cut_the(value,arg):
    return value.replace(arg,'')

# register.filter('cut',cut_the) 
# معادل با دگوراتور