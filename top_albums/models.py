from django.db import models

# Data-source: https://davesmusicdatabase.blogspot.com/2012/02/worlds-top-100-all-time-best-selling.html

class Artist(models.Model):
    name = models.CharField(max_length=500)
    description = models.TextField()

    def __str__(self):
        return self.name


class Album(models.Model):
    album_name = models.CharField(max_length=500)
    artist = models.ForeignKey(Artist, related_name='albums', on_delete=models.CASCADE)
    release_year = models.CharField(max_length=4)
    millions_of_copies_sold = models.FloatField()
    ranking = models.IntegerField()
    spotify_id = models.CharField(max_length=100)

    def __str__(self):
        return self.album_name


class Track(models.Model):
    album = models.ForeignKey(Album, related_name='tracks', on_delete=models.CASCADE)
    disc = models.IntegerField()
    order = models.IntegerField()
    title = models.CharField(max_length=500)
    duration = models.DurationField()
    spotify_id = models.CharField(max_length=100)
    rating = models.PositiveSmallIntegerField(choices=[(i,i) for i in range(0,11)], null=True)
    comments = models.TextField(null=True, blank=True)

    class Meta:
        unique_together = ['album', 'disc', 'order']
        ordering = ['album_id', 'disc', 'order']

    def __str__(self):
        return "D{} - {:02}: {}".format(self.disc, self.order, self.title)
