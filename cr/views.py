#coding: utf-8

from django.views.generic.base import TemplateView


class Home(TemplateView):
    """Main page of the site. Displays the greeting."""

    template_name = 'home.html'
