from django.urls import include, path
from pirates.views import ListaTesourosView


urlpatterns = [
    path('lista_tesouros/', ListaTesourosView.as_view()),
]