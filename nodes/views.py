from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Node


class TitleListView(ListView):
    model = Node
    template_name = 'nodes/title_list.html'

    def get_context_data(self, **kwargs):
        context = super(TitleListView, self).get_context_data(**kwargs)
        context['unique']= Node.new.all()
        return context


class NodeListView(ListView):
    model = Node
