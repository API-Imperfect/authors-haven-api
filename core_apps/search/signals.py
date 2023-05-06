from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from django_elasticsearch_dsl.registries import registry

from core_apps.articles.models import Article


@receiver(post_save, sender=Article)
def update_document(sender, instance=None, created=False, **kwargs):
    """Update the ArticleDocument in Elasticsearch when an article instance is updated or created"""
    registry.update(instance)


@receiver(post_delete, sender=Article)
def delete_document(sender, instance=None, **kwargs):
    """Delete the ArticleDocument in Elasticsearch when an article instance is deleted"""
    registry.delete(instance)
