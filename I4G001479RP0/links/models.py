from django.db import models
from django.contrib.auth import get_user_model
from django.template.defaultfilters import slugify
from .managers import ActiveLinkManager

# Create your models here.
class Link(models.Model):


    target_url = models.URLField(max_length=200)
    description = models.CharField(max_length=200)
    identifier = models.SlugField(max_length=20, blank=True, unique=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    objects = models.Manager()
    public = ActiveLinkManager()


    def save(self, *args, **kwargs):
        self.slug = slugify(self.description)
        super().save(*args, **kwargs)
        pass


    def __str__(self):
        return self.description



# target_url : A url path of maxlength 200, use Django’s models.URLField
# description : A string of maxlength 200, use Django’s models.CharField
# identifier: A string of maxlength 20, use Django’s models.SlugField. Set blank=True and unique=True for the field.
# author : A Foreign Key to the current user model. Make use of Django’s get_user_model function.
# created_date : A date-time column, use Django’s models.DateTimeField.
# active :  A boolean (True or False), determining if the shortened URL is publicly accessible. Make use of Django’s BooleanField. The default should be True.