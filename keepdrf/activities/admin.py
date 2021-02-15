from django.contrib import admin
from .models import Responsible, Tag, Activity


class ActivityAdmin(admin.ModelAdmin):
    list_display = ('title', 'note', 'date', 'deadline', 'status', 'responsible', 'tag')


admin.site.register(Activity, ActivityAdmin)


class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'tag')


admin.site.register(Tag, TagAdmin)


class ResponsibleAdmin(admin.ModelAdmin):
    list_display = ('id', 'responsible')


admin.site.register(Responsible, ResponsibleAdmin)
