from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from stdimage import StdImageField


# Create your models here.



class Product(models.Model):

    TYPE_CHOICES = (
        ('L', 'Laptop'),
        ('D', 'Desktop'),
    )
    type = models.CharField(max_length=1, choices=TYPE_CHOICES)
    productName = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    category = models.CharField(max_length=200)
    image = StdImageField(upload_to='%Y/%m/%d/')
    price = models.IntegerField()
    stock = models.IntegerField()
    description = models.TextField(max_length=1000)
    brand_name = models.CharField(max_length=20)

    def __str__(self):
        return self.productName

    def get_absolute_url(self):
        return reverse("article", kwargs={"slug": self.slug})


def create_slug(instance, new_slug=None):
    slug = slugify(instance.productName)
    if new_slug is not None:
        slug = new_slug
    qs = Product.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)


pre_save.connect(pre_save_post_receiver, sender=Product)

