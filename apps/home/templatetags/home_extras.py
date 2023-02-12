from django import template

register = template.Library()


@register.filter
def quebra_de_linha(texto):

    text = texto.split('.')

    saida = ""

    for item in text:
        temp = item.rstrip('\n')
        saida += f"{temp}.<br>"
    return saida



quebra_de_linha.is_safe = False
