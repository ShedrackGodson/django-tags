from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from .utils import get_read_time, unique_slug_generator
from django.db.models.signals import pre_save
from taggit.managers import TaggableManager # This will handle tags for this Post
# Tags can be more than 1 and they will be comma-separated values i.e (technology,sports,news)


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    message = models.TextField(max_length=2048,null=True,blank=True)
    tags = TaggableManager()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """ Object Return """
        return "{}-{}".format(self.id, self.title)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    """ Slugify """
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

    if instance.message:
        read_time_var = get_read_time(instance.message)
        instance.read_time = read_time_var


pre_save.connect(pre_save_post_receiver, sender=Post)