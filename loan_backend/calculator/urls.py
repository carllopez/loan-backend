from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('records/<int:pk>/', views.RecordList.as_view()),
    path('operation/', views.OperationRequest.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
