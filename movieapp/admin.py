from django.contrib import admin

from .models import Movies, Series, Clips


admin.site.site_header = 'WISEMAN'

class MoviesAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('upload_date',)
    prepopulated_fields = {'slug': ('title',)}

class SeriesAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('upload_date',)
    prepopulated_fields = {'slug': ('title',)}

class ClipsAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('upload_date',)
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Movies, MoviesAdmin)

admin.site.register(Series, SeriesAdmin)

admin.site.register(Clips, ClipsAdmin)