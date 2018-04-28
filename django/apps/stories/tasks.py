"""Celery tasks for stories"""

from datetime import timedelta

from celery import shared_task
from celery.task import periodic_task
from celery.utils.log import get_task_logger

from apps.issues.models import current_issue
from apps.photo.tasks import upload_imagefile_to_desken
from django.core.cache import cache
from django.db.models import F, Q
from django.utils import timezone

from .models import Story

logger = get_task_logger(__name__)

# cron timing
UPDATE_SEARCH = timedelta(hours=1)
DEVALUE_HOTNESS = timedelta(hours=1)
PERSIST_STORY_VISITS = timedelta(minutes=1)


@periodic_task(run_every=UPDATE_SEARCH)
def update_search_task():
    """Update database search index for newly modified stories."""
    qs = Story.objects.filter(
        Q(search_vector=None)
        | Q(modified__gt=timezone.now() - UPDATE_SEARCH * 1.5)
    )
    qs.update_search_vector()
    return qs.count()


@shared_task
def upload_storyimages(pk):
    story = Story.objects.get(pk=pk)
    target = f'{current_issue().number}/{story.section}/'
    for im in story.images.all():
        upload_imagefile_to_desken.delay(im.imagefile.pk, target)
    return target


@periodic_task(run_every=PERSIST_STORY_VISITS)
def save_visits_task():
    """Persist visit counts to database and reset cache."""
    cache_keys = cache.keys(f'{Story.VISIT_KEY_PREFIX}*')
    for key in cache_keys:
        val = int(cache.get(key))
        pk = int(key.replace(Story.VISIT_KEY_PREFIX, ''))

        Story.objects.filter(pk=pk).update(
            hit_count=F('hit_count') + val,
            hot_count=F('hot_count') + 100 * val,
        )
        logger.info(f'Story {pk} was visited {val} times')
        cache.delete(key)
    return len(cache_keys)


@periodic_task(run_every=DEVALUE_HOTNESS)
def devalue_hotness_task(chill_percentage=1):
    """Decrease the hotness rating of all stories."""
    factor = (100 - chill_percentage) / 100.0
    logger.info(f'decreasing hotness by {factor}%')
    Story.objects.devalue_hotness(factor)
    return chill_percentage
