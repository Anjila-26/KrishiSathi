from django.urls import path

from .views import vegetable_list

urlpatterns = [
    path('vegetables/', vegetable_list, name='vegetable_list'),
    # Other URL patterns for your application
]
