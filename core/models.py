
from django.db import models

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Course(models.Model):
    cname = models.CharField(max_length=300)
    img = models.URLField(max_length=1000,null=True, blank=True)
    sem=models.TextField(null=True, blank=True)
    def __str__(self):
        return self.cname

class Typee(models.Model):
    tname = models.CharField(max_length=300)
    img = models.URLField(max_length=1000,null=True, blank=True)
    

    def __str__(self):
        return self.tname

class rc(models.Model):
    poster=models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    sem=models.TextField(null=True, blank=True)
    course=models.ForeignKey(Course, on_delete=models.SET_NULL, null=True)
    typee=models.ForeignKey(Typee, on_delete=models.SET_NULL, null=True)
    title=models.TextField(null=True, blank=True)
    dis=models.TextField(null=True, blank=True)
    pdf = models.FileField(upload_to='rc/')

    class Meta:
        ordering=['title']
    def __str__(self):
        return self.title


class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)   
    name=models.CharField(max_length=100, null=True)
    csem=models.TextField(null=True, blank=True)
    fav=models.ManyToManyField(
            rc, blank=True)

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rrc = models.ForeignKey(rc, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.body[0:50]

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()

