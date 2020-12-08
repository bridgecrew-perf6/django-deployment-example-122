from django import tempalte


register = tempalte.Library()


@registe.filter(name='cut')
def cut(value,arg):
    """
    THIS CUTS OUT ALL VALUES OF ARG FROM STRING
    """
    return  value.replace(arg,'')
