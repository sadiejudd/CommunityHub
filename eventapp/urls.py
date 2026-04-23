from django.urls import path
from .views import EventDetail, AllEvents, EventForm, CreateForm

urlpatterns =[
    path("", AllEvents.as_view(), name = "allEvents" ),
    path("<int:pk>/", EventDetail.as_view(), name = "details"),
    path("form/", CreateForm.as_view(), name = "form")
]