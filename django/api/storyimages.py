from apps.stories.models import StoryImage
from rest_framework import serializers, viewsets
from url_filter.integrations.drf import DjangoFilterBackend
from utils.serializers import AbsoluteURLField


class StoryImageSerializer(serializers.ModelSerializer):
    """ModelSerializer for StoryImage"""

    filename = serializers.CharField(
        read_only=True, source='imagefile.filename'
    )

    thumb = AbsoluteURLField(source='imagefile.large.url')

    class Meta:
        model = StoryImage
        fields = [
            'url',
            'id',
            'caption',
            'parent_story',
            'imagefile',
            'creditline',
            'index',
            'thumb',
            'filename',
            'size',
        ]


class StoryImageViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows StoryImage to be viewed or updated.
    """

    queryset = StoryImage.objects.prefetch_related(
        'imagefile',
    ).order_by(
        '-modified',
    )
    serializer_class = StoryImageSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ['parent_story']