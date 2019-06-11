import csv

from django.shortcuts import render
from django.views.generic import TemplateView


class InflationView(TemplateView):
    template_name = 'inflation.html'

    # чтение csv-файла и заполнение контекста
    def get(self, request, *args, **kwargs):
        with open('inflation_russia.csv', encoding='utf-8') as f:
            reader = csv.reader(f, delimiter=';')
            rows = list(reader)
            context = {'head': rows[0],
                       'table': rows[1:]}
            return render(request, self.template_name,
                          context)
