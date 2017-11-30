from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
# from django.contrib.auth.models import User
from django.utils.text import slugify
# from django.conf import settings
# from django.db.models.signals import pre_save
# from django.contrib import auth




class Post(models.Model):
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    author = models.CharField(max_length=30)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    slug = models.SlugField(allow_unicode=True, unique=True)


    def save(self,*args, **kwargs):
        self.slug = slugify(self.title)
        self.published_date = timezone.now()
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("posts:detail", kwargs={"slug": self.slug})

    class Meta:
        ordering = ['created_date']

    def __str__(self):
        return self.title


# class User(auth.models.User, auth.models.PermissionsMixin):
#     def __str__(self):
#         return self.username
