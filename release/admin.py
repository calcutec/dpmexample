from django.contrib import admin
from .models import Release, Track, Disc
import boto3
import os
from django.urls import reverse
from django.utils.encoding import force_text
from django.utils.html import format_html


class DiscInline(admin.TabularInline):
    model = Disc
    extra = 1
    fields = ['get_edit_link', 'release', 'number']
    readonly_fields = ["get_edit_link"]

    def get_edit_link(self, obj=None):
        if obj.pk:  # if object has already been saved and has a primary key, show link to it
            url = reverse('admin:%s_%s_change' % (obj._meta.app_label, obj._meta.model_name), args=[force_text(obj.pk)])
            return format_html('<a href="%s">%s</a>' % (url, "Click to add tracks to this %s" % obj._meta.verbose_name))
        return "save and continue editing to create a link"
    get_edit_link.short_description = "Edit link"


@admin.register(Release)
class ReleaseAdmin(admin.ModelAdmin):
    inlines = [DiscInline]

    # def download_release(self, request, queryset):
    #
    #     file_dict = {}
    #     image_file_name = os.path.basename(queryset[0].image)
    #     image_path, ext = os.path.splitext(image_file_name)
    #     file_dict[image_file_name] = "%s%s" % (queryset[0].cat_no, ext)
    #     for item in queryset[0].kitten_set.model.objects.all():
    #         sound_file_name = os.path.basename(item.track)
    #         file_path, ext = os.path.splitext(sound_file_name)
    #         if ext == ".wav":
    #             file_dict[sound_file_name] = "%s_%s_%s%s" % (queryset[0].cat_no,
    #                                                          str(item.disc_no).zfill(2),
    #                                                          str(item.track_no).zfill(2), ext)
    #
    #     s3 = boto3.resource('s3')
    #     s3_client = boto3.client('s3')
    #
    #     prefix = queryset[0].cat_no + "/"
    #     download_location_path = os.path.expanduser("~") + "/s3-backup/" + prefix
    #
    #     if not os.path.exists(download_location_path):
    #         os.mkdir(download_location_path)
    #
    #     bucket = s3.Bucket(name="dpm-upload")
    #     for l in bucket.objects.filter(Prefix=prefix):
    #         file_base = os.path.basename(l.key)
    #         if file_base in file_dict:
    #             s3_client.download_file('dpm-upload', l.key, "%s%s" % (download_location_path, file_dict[file_base]))
    #
    # download_release.short_description = "Download Release"
    #
    # actions = [download_release]


class TrackInline(admin.TabularInline):
    model = Track
    extra = 1
    fields = ['track', 'track_no', 'name']


@admin.register(Disc)
class DiscAdmin(admin.ModelAdmin):
    fields = ["get_edit_link", "release", "number"]
    inlines = [TrackInline]
    readonly_fields = ["get_edit_link"]

    def get_edit_link(self, obj=None):
        if obj.pk:  # if object has already been saved and has a primary key, show link to it
            url = reverse('admin:%s_%s_change' % (obj._meta.app_label, obj.release._meta.model_name), args=[force_text(obj.release.id)])
            return format_html('<a href="%s">%s</a>' % (url, "Click to go to release %s" % obj.release.cat_no))
        return "save and continue editing to create a link"
    get_edit_link.short_description = "Edit link"
