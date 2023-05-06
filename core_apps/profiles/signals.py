import logging

from django.db.models.signals import post_save
from django.dispatch import receiver

from authors_api.settings.base import AUTH_USER_MODEL
from core_apps.profiles.models import Profile

logger = logging.getLogger(__name__)


@receiver(post_save, sender=AUTH_USER_MODEL)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        logger.info(f"{instance}'s profile has been created.")
