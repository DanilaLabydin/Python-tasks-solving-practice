from django.db.models import Count

from .models import *


menu = [{'title': 'home page', 'url_name': 'home'},
        {'title': 'about us', 'url_name': 'about'},
        {'title': 'add an article', 'url_name': 'add_article'},
        {'title': 'contacts', 'url_name': 'contacts'},
]


class DataMixin:
    paginate_by = 3

    def get_user_context(self, **kwargs):

        context = kwargs
        cats = Category.objects.all()

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(2)

        context['menu'] = user_menu
        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context
