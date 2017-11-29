from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.db.models.signals import pre_save


class Post(models.Model):
    author = models.CharField(max_length=30)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    slug = models.SlugField(unique=True)


    def publish(self, *args, **kwargs):
        self.slug = slugify(self.title)
        self.published_date = timezone.now()
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("posts:detail", kwargs={"slug": self.slug})

    class Meta:
        ordering = ['created_date']

    def __str__(self):
        return self.title
