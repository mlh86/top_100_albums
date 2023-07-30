from rest_framework import permissions, renderers, viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response

from top_albums.models import Artist, Album, Track
from top_albums.serializers import ArtistSerializer, AlbumSerializer, TrackSerializer

class ListRetrieveUpdateViewSet(
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    pass


class ArtistViewSet(ListRetrieveUpdateViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class AlbumViewSet(ListRetrieveUpdateViewSet):

    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class TrackViewSet(ListRetrieveUpdateViewSet):

    queryset = Track.objects.all()
    serializer_class = TrackSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
