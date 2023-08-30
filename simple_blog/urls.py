from django.urls import path, include
from .views import PageList, PageDetail

urlpatterns = [
    path('pages/', PageList.as_view(), name='page-list'),
    path('pages/<slug:slug>/', PageDetail.as_view(), name='page-detail'),
]
