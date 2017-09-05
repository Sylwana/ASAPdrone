from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class UserFootage(models.Model):
    link = models.URLField()
    author = models.ForeignKey(User)
    description = models.CharField(max_length=2000, null=True)

    def __str__(self):
        return self.link

    def get_delete_url(self):
        return reverse('delete-footage', kwargs={'pk': self.pk})

    def get_absolute_url(self):
        return reverse('console', kwargs={'pk': self.author.pk})

VIDEO_TYPES = [
    ('video', "video"),
    ('photography', "photography"),
    ('video and photography', "video and photography"),
]


class City(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Details(models.Model):
    person = models.OneToOneField(User)
    about_me = models.TextField()
    pricing = models.DecimalField(max_digits=6, decimal_places=2)
    video_type = models.CharField(choices=VIDEO_TYPES, max_length=100)
    cities = models.ManyToManyField(City)

    def __str__(self):
        return self.about_me

    def get_absolute_url(self):
        return reverse('console', kwargs={'pk': self.person.pk})


class Message(models.Model):
    sender = models.ForeignKey(User, related_name="sender")
    receiver = models.ForeignKey(User, related_name="receiver")
    content = models.TextField()

    def get_delete_url(self):
        return reverse('delete-message', kwargs={'pk': self.pk})


class Recommendation(models.Model):
    sender = models.ForeignKey(User, related_name="r_sender")
    receiver = models.ForeignKey(User, related_name="r_receiver")
    content = models.TextField()
