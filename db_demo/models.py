from django.db import models

# The built-in User model already has secure handling for things like
# username, password, email address, and so on.
from django.contrib.auth.models import User


class Roles(models.Model):
    title = models.CharField(max_length=50)
    user = models.ManyToManyField(User)


class Permissions(models.Model):
    title = models.CharField(max_length=50)
    role = models.ManyToManyField(Roles,)


class Profile(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)


class Contributors(models.Model):
    title = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    role = models.ManyToManyField(Roles)


class Categories(models.Model):
    title = models.CharField(max_length=50)
    is_subgenre = models.BooleanField()


class Pages(models.Model):
    title = models.CharField(max_length=50)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    is_published = models.BooleanField()
    is_flagged = models.BooleanField()


class Tags(models.Model):
    title = models.CharField(max_length=50)
    page = models.ManyToManyField(Pages)
