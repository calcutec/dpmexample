from django.contrib import admin
from .models import Release, Track, Disc
import nested_admin
from django import forms
import boto3
import io
from . import zipfile as zipstream
from django.conf import settings
import sys
from django.http import StreamingHttpResponse


def iterable_to_stream(iterable, buffer_size=io.DEFAULT_BUFFER_SIZE):
    """
    Lets you use an iterable (e.g. a generator) that yields bytestrings as a
    read-only input stream.

    The stream implements Python 3's newer I/O API (available in Python 2's io
    module).  For efficiency, the stream is buffered.

    From: https://stackoverflow.com/a/20260030/729491
    """
    class IterStream(io.RawIOBase):
        def __init__(self):
            self.leftover = None

        def readable(self):
            return True

        def readinto(self, b):
            try:
                l = len(b)  # We're supposed to return at most this much
                chunk = self.leftover or next(iterable)
                output, self.leftover = chunk[:l], chunk[l:]
                b[:len(output)] = output
                return len(output)
            except StopIteration:
                return 0    # indicate EOF
    return io.BufferedReader(IterStream(), buffer_size=buffer_size)


def iterate_key(l):
    yield l.get()["Body"].read()


def download_releases(self, request, queryset):
    s3_resource = boto3.resource('s3', aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
                                 aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY)
    prefix = "DTD023DI"
    bucket = s3_resource.Bucket(name="%s" % settings.AWS_STORAGE_BUCKET_NAME)
    with open('/tmp/foo2.zip', 'wb') as f:
        z = zipstream.ZipFile(mode='w')
        counter = 0
        for l in bucket.objects.filter(Prefix=prefix):
            z.write(iterable_to_stream(iterate_key(l)), arcname='foo%s.wav' % str(counter))
            counter += 1

        # for chunk in z:
        #     print("CHUNK", len(chunk))
        #     f.write(chunk)
        response = StreamingHttpResponse(z, content_type='application/zip')
        response['Content-Disposition'] = 'attachment; filename={}'.format('files.zip')
        return response


class TrackForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(TrackForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields['track_no'].widget.attrs['readonly'] = True
            self.fields['track_no'].widget.attrs['data-input-type'] = "track"

    class Meta:
        model = Track
        fields = ['name', 'track', 'track_no']


class TrackInline(nested_admin.NestedTabularInline):
    model = Track
    extra = 0
    form = TrackForm
    fields = ["track", "track_no", "name"]
    sortable_field_name = "track_no"


class DiscForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(DiscForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.pk:
            self.fields['number'].widget.attrs['readonly'] = True
            self.fields['number'].widget.attrs['data-input-type'] = "disc"

    class Meta:
        model = Disc
        fields = ['number']


class DiscInline(nested_admin.NestedTabularInline):
    model = Disc
    extra = 0
    form = DiscForm
    inlines = [TrackInline]
    sortable_field_name = "number"


@admin.register(Release)
class ReleaseAdmin(nested_admin.NestedModelAdmin):
    inlines = [DiscInline]
    download_releases.short_description = "Download Releases"
    actions = [download_releases]

    # def get_inline_instances(self, request, obj=None):
    #     if not obj:
    #         return list()
    #     return super(ReleaseAdmin, self).get_inline_instances(request, obj)












