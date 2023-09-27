from django.urls import path
from .views import EmailAPIView


urlpatterns = [
    path('', EmailAPIView.as_view({'post':'send'})),
]