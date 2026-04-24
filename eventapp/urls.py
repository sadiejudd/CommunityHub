from django.urls import path
from .views import EventDetail, AllEvents, EventForm, CreateForm
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
    path("", AllEvents.as_view(), name = "allEvents" ),
    path("<int:pk>/", EventDetail.as_view(), name = "details"),
    path("form/", CreateForm.as_view(), name = "form")
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)