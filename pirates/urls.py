from django.urls import include, path
from pirates.views import ListaTesourosView


urlpatterns = [
    path('/', ListaTesourosView.as_view()),
]