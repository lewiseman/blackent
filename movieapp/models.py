from django.db import models
import os

def update_movie_name(instance, filename):
        path = 'Movies'
        format = instance.title
        return os.path.join(path, format)

def update_movie_poster_name(instance, filename):
        path = 'MoviesPoster'
        format = instance.title
        return os.path.join(path, format)

def update_series_name(instance, filename):
        path = 'series'
        format = instance.title
        return os.path.join(path, format)

def update_series_poster_name(instance, filename):
        path = 'SeriesPoster'
        format = instance.title
        return os.path.join(path, format)

def update_clip_name(instance, filename):
        path = 'Clips'
        format = instance.title
        return os.path.join(path, format)

class Movies(models.Model):
    title = models.CharField(max_length=100)
    upload_date = models.DateTimeField(auto_now_add=True, blank=True)
    slug = models.SlugField(default=None)
    poster_img = models.ImageField(upload_to=update_movie_poster_name, max_length=1000)#MoviesPoster/%y/%m
    movie_file = models.FileField(upload_to=update_movie_name, max_length=1000)
    def __str__(self):
        return self.title

    class Meta: 
        verbose_name = "Movie"
        verbose_name_plural = "Movies"


class Series(models.Model):
    title = models.CharField(max_length=100)
    upload_date = models.DateTimeField(auto_now_add=True, blank=True)
    slug = models.SlugField(default=None)
    poster_img = models.ImageField(upload_to=update_series_poster_name, max_length=1000)
    series_file = models.FileField(upload_to=update_series_name, max_length=1000)
    def __str__(self):
        return self.title

    class Meta: 
        verbose_name = "Series"
        verbose_name_plural = "Series"


class Clips(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(default=None)
    upload_date = models.DateTimeField(auto_now_add=True, blank=True)
    clip_file = models.FileField(upload_to=update_clip_name, max_length=1000)
    def __str__(self):
        return self.title

    class Meta: 
        verbose_name = "Clip"
        verbose_name_plural = "Clips"
