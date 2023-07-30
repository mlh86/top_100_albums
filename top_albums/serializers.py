from rest_framework import serializers

from top_albums.models import Artist, Album, Track

class customHyperlinkedRelatedField(serializers.HyperlinkedRelatedField):

    def get_url(self, obj, view_name, request, format):
        resource_url = super().get_url(obj, view_name, request, format)
        display_text = ""
        model_name = view_name.replace("-detail", "").title()
        if model_name == "Artist":
            display_text = Artist.objects.get(id=obj.pk).name
        elif model_name == "Album":
            display_text = Album.objects.get(id=obj.pk).album_name
        elif model_name == "Track":
            display_text = str(Track.objects.get(id=obj.pk))
        return display_text + " (" + resource_url + ")" if display_text else resource_url


class ArtistSerializer(serializers.HyperlinkedModelSerializer):
    albums = customHyperlinkedRelatedField(
        view_name='album-detail', read_only=True, many=True)

    class Meta:
        model = Artist
        fields = ['url', 'name', 'description', 'albums']
        read_only_fields = ['name', 'albums']


class AlbumSerializer(serializers.HyperlinkedModelSerializer):
    album_name = serializers.CharField(read_only=True)
    artist = customHyperlinkedRelatedField(
        view_name='artist-detail', read_only=True)
    tracks = customHyperlinkedRelatedField(
        many=True, view_name='track-detail', read_only=True)

    class Meta:
        model = Album
        fields = '__all__'
        read_only_fields = ['release_year','spotify_id','ranking','millions_of_copies_sold']


class TrackSerializer(serializers.HyperlinkedModelSerializer):
    title = serializers.CharField(read_only=True)
    artist = customHyperlinkedRelatedField(
        view_name='artist-detail', read_only=True, source='album.artist')
    album = customHyperlinkedRelatedField(
        view_name='album-detail', read_only=True)

    class Meta:
        model = Track
        fields = '__all__'
        read_only_fields = ['title', 'album', 'disc', 'order', 'duration', 'spotify_id']
