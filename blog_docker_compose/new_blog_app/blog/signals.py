from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from blog.models import Author


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Author.objects.create(user=instance)
