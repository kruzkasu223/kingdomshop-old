from django.dispatch import receiver
from django.contrib.auth.models import User
from django.db.models.signals import ( post_save, )
from userprofile.models import UserDetail, UserAddress

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserDetail.objects.create(
            user = instance
        )
        UserAddress.objects.create(
            user = instance
        )
        