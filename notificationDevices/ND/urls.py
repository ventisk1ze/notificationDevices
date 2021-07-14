from django.urls import path
from .views import DeviceView

app_name = "ND"


urlpatterns = [
    path('', DeviceView.as_view()),
]