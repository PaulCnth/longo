from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Article(models.Model):
    """
    Article model
    """
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField(auto_now_add=True)
    url = models.URLField()
    context = models.TextField(max_length=300)
    is_active = models.BooleanField(default=True)


class HashTag(models.Model):
    """
    HashTah model
    """
    name = models.CharField(max_length=64, unique=True)
    article = models.ManyToManyField(Article)

    def __unicode__(self):
        return self.name