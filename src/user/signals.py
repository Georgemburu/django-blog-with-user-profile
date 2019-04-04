from django.db.models.signals import post_save
from .models import UserProfile
from django.contrib.auth.models import User
from django.dispatch import receiver



@receiver(post_save, sender=User)
def create_Profile_For_User(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_Created_Profile_For_User(sender, instance, **kwargs):
    instance.userprofile.save()