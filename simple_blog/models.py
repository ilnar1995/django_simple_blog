from django.db import models



class Page(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    sort_order = models.IntegerField()

    class Meta:
        db_table = "blog_page"
        ordering = ["id"]


class ContentBlock(models.Model):
    title = models.CharField(max_length=255)
    video_link = models.URLField()
    sort_order = models.IntegerField()
    views_count = models.IntegerField(default=0)
    pages = models.ManyToManyField(Page, related_name='content_blocks')


    class Meta:
        db_table = "blog_content_block"
        ordering = ["id"]
