from django.db import models

# Create your models here.
class MusicBand(models.Model):
    name = models.CharField(max_length=255)
    creation_year = models.CharField(max_length=4)
    style = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}'

class Album(models.Model):
    name = models.CharField(max_length=255)
    issue_year = models.CharField(max_length=4)
    band = models.ForeignKey('MusicBand', null=True,on_delete=models.SET_NULL, related_name= 'albums')

    def __str__(self):
        return f'{self.name}'

class Track(models.Model):
    name = models.CharField(max_length=255)
    track_length = models.CharField(max_length=255)
    album = models.ForeignKey('Album', null=True,on_delete=models.SET_NULL, related_name= 'songs')

    def __str__(self):
        return f'{self.name}'