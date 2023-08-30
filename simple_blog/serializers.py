from rest_framework import serializers
from .models import Page, ContentBlock


class ContentBlockSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentBlock
        fields = ('title', 'video_link', 'sort_order', 'views_count')


class PageListSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='page-detail',
        lookup_field='slug'
    )

    class Meta:
        model = Page
        fields = ['title', 'url']


class PageDetailSerializer(serializers.ModelSerializer):
    content_blocks = ContentBlockSerializer(many=True, read_only=True)

    class Meta:
        model = Page
        fields = ('title', 'content_blocks')
