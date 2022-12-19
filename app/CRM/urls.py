from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('leads/', views.leads_list),
    path('leads/<int:id>/', views.lead_detail),
    path('costumers/', views.costumers_list),
    path('costumers/<int:id>/', views.costumer_detail)
]

urlpatterns = format_suffix_patterns(urlpatterns)