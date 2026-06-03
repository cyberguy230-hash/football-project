from django.contrib import admin
from .models import Football
# Register your models here.
admin.site.site_header = "F.M Admin"
admin.site.site_title = "Organizer Admin"
admin.site.index_title = "Manager Admin"

@admin.register(Football)
class FootballAdmin(admin.ModelAdmin):
    list_display = ["id", "Name", "Age", "Team", "Player"]
    list_editable = ["Name", "Age", "Team", "Player"]
    search_fields = ["Name"]