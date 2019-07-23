from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
    path('snippets/', views.home),
]

urlpatterns = format_suffix_patterns(urlpatterns)
