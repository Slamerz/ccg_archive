from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class IndexView(TemplateView):
    """
    Template view of the homepage
    """

    template_name = "index.html"
