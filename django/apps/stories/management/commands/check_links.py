import logging
import re

from django.core.management.base import BaseCommand
from django.db.models import Count

from apps.stories.models import InlineLink

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = ''

    def add_arguments(self, parser):
        parser.add_argument(
            '--new',
            '-n',
            action='store_true',
            dest='new links',
            default=False,
            help='Only check new links'
        )
        parser.add_argument(
            '--status',
            '-s',
            action='append',
            dest='status in',
            default=[],
            help='Check links with these status codes'
        )
        parser.add_argument(
            '--timeout',
            '-t',
            type=float,
            action='store',
            dest='timeout',
            default=1,
            help='Seconds to wait for a http response'
        )

    def handle(self, *args, **options):

        status_in = options['status in']

        if options['new links']:
            status_in = ['']

        if status_in:
            links_to_check = InlineLink.objects.filter(
                status_code__in=status_in
            )
        else:
            links_to_check = InlineLink.objects.all()

        self._check_links(links_to_check, timeout=options['timeout'])

    def _check_links(self, links_to_check, timeout):
        """ Check and update status code for inline links in articles. """

        self.stdout.write('Checking {} links'.format(links_to_check.count()))

        for link in links_to_check:
            link.check_link(save_if_changed=True, timeout=timeout)

        self.stdout.write('Checked {} links'.format(links_to_check.count()))
        link_statuses = InlineLink.objects.values('status_code').annotate(
            count=Count('status_code')
        )
        for status in link_statuses:
            self.stdout.write('{count} - {status_code}'.format(**status))
