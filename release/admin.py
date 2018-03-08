from django.contrib import admin
from .models import Release, Track, Disc
import nested_admin


class TrackInline(nested_admin.NestedTabularInline):
    model = Track
    min_num = 1
    extra = 1
    fields = ["track", "track_no", "name"]

    # def get_extra (self, request, obj=None, **kwargs):
    #     """Dynamically sets the number of extra forms. 0 if the related object
    #     already exists or the extra configuration otherwise."""
    #     if obj:
    #         # Don't add any extra forms if the related object already exists.
    #         return 0
    #     return self.extra


class DiscInline(nested_admin.NestedTabularInline):
    model = Disc
    extra = 0
    inlines = [TrackInline]


@admin.register(Release)
class ReleaseAdmin(nested_admin.NestedModelAdmin):
    inlines = [DiscInline]

    # def get_inline_instances(self, request, obj=None):
    #     if not obj:
    #         return list()
    #     return super(ReleaseAdmin, self).get_inline_instances(request, obj)









