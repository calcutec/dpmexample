from django.contrib import admin
from .models import Release, Track, Disc
import nested_admin


class TrackInline(nested_admin.NestedTabularInline):
    model = Track
    extra = 1
    fields = ["track", "track_no", "name"]
    sortable_field_name = "track_no"


class DiscInline(nested_admin.NestedTabularInline):
    model = Disc
    extra = 0
    inlines = [TrackInline]


@admin.register(Release)
class ReleaseAdmin(nested_admin.NestedModelAdmin):
    inlines = [DiscInline]



