from django.contrib import admin
from .models import Release, Track, Disc
import nested_admin
from django import forms


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

    # def get_inline_instances(self, request, obj=None):
    #     if not obj:
    #         return list()
    #     return super(ReleaseAdmin, self).get_inline_instances(request, obj)









