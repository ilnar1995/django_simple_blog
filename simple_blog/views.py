from . import models
from rest_framework import generics, mixins, viewsets
from .serializers import PageListSerializer, PageDetailSerializer
from django.db.models import F


class PageList(generics.ListAPIView):
    queryset = models.Page.objects.all().prefetch_related('content_blocks')
    serializer_class = PageListSerializer


class PageDetail(generics.RetrieveAPIView):
    queryset = models.Page.objects.all().prefetch_related('content_blocks')
    serializer_class = PageDetailSerializer
    lookup_field = "slug"

    def get_object(self):
        obj = super().get_object()
        # увеличиваем количество просморов у блоков
        obj.content_blocks.all().update(views_count=F('views_count') + 1)
        return obj
