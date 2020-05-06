from django import template
from wines.models import Category, Wine

register = template.Library()


# Вывод категорий
@register.simple_tag()
def get_categories():
    return Category.objects.all()


@register.inclusion_tag('wines/tags/last_wine.html')
def get_last_wine(count=5):
    wines = Wine.objects.order_by("id")[:count]
    return {"last_wines": wines}


