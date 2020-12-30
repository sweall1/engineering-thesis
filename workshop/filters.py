import django_filters

from.models import *


class WorkshopFilter(django_filters.FilterSet):
    class Meta:
        model = Workshop
        fields = [
            'City',

        ]
        labels = {
            'City': 'Wpisz miasto',

        }

