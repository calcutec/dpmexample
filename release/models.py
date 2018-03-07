from django.db import models
from s3direct.fields import S3DirectField


class Release(models.Model):
    cat_no = models.CharField(max_length=30)
    image = S3DirectField(dest='images', blank=True, null=True)

    def __str__(self):
        return self.cat_no


class Disc(models.Model):
    DISC_NO_CHOICES = (
        (1, 'One'),
        (2, 'Two'),
        (3, 'Three'),
        (4, 'Four'),
    )

    release = models.ForeignKey('Release', on_delete=models.CASCADE)
    number = models.IntegerField(choices=DISC_NO_CHOICES,default=1)

    def __str__(self):
        return "%s_Disc_%s" % (self.release.cat_no, str(self.number))


class Track(models.Model):
    disc = models.ForeignKey('Disc', on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=128, blank=True, null=True)
    track = S3DirectField(dest='wavs', blank=True, null=True)
    track_no = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

