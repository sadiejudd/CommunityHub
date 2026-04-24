from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Event
from django import forms
from django.urls import reverse_lazy
# Create your views here.


class AllEvents(ListView):
    model = Event
    template_name = "eventapp/events.html"
    context_object_name = "events"


class EventDetail(DetailView):
    model = Event
    template_name = "eventapp/eventdetail.html"
    context_object_name = "event"


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'datetime': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }

class CreateForm(CreateView):
    model = Event
    fields = '__all__'
    template_name = "eventapp/form.html"
    success_url = reverse_lazy('allEvents')







