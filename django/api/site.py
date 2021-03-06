"""Site data misc"""

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import permissions, response, serializers, views

from apps.contributors.models import Contributor
from apps.issues.models import Issue
from apps.stories.models import Section, StoryType

from .issues import IssueSerializer


class StoryTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoryType
        fields = ['name', 'count']


class SectionSerializer(serializers.ModelSerializer):
    storytypes = StoryTypeSerializer(many=True, read_only=True)

    class Meta:
        model = Section
        fields = ['id', 'title', 'storytypes']


class StaffSerializer(serializers.ModelSerializer):
    thumb = serializers.ImageField(
        source='byline_photo.preview', read_only=True
    )

    class Meta:
        model = Contributor
        fields = [
            'position',
            'display_name',
            'phone',
            'email',
            'thumb',
            'id',
        ]


class SiteData:
    def __init__(self):
        self.staff = Contributor.objects.management().prefetch_related(
            'byline_photo',
        )
        self.sections = Section.objects.all().prefetch_related(
            'storytype_set',
        )
        issues = Issue.objects.prefetch_related('pdfs')
        self.issues = {
            'latest': issues.latest_issue(),
            'next': issues.next_issue(),
        }


class SiteSerializer(serializers.Serializer):
    staff = StaffSerializer(many=True, read_only=True)
    issues = serializers.DictField(child=IssueSerializer())
    sections = SectionSerializer(many=True, read_only=False)


class SiteDataAPIView(views.APIView):
    """Get basic data about site and staff."""
    permission_classes = [permissions.AllowAny]

    @method_decorator(cache_page(60))
    def get(self, request, format=None):
        serializer = SiteSerializer(SiteData(), context={'request': request})
        return response.Response(serializer.data)
