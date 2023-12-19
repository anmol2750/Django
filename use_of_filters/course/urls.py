from django.urls import path
from . import views

urlpatterns = [
    path('add/',views.add),
    path('addslashes/',views.addslashes),
    path('capfirst/',views.capfirst),
    path('center/',views.center),
    path('first/',views.first),
    path('last/',views.last),
    path('floatformat/',views.floatformat),
    path('length/',views.length),
    path('dictsort/',views.dictsort),
    path('unordered_list/',views.unordered_list),
]