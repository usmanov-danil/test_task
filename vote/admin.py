from django.contrib import admin

from .models import Question, Answer, Vote

admin.site.site_header = "Vote Admin"
admin.site.site_title = "Vote Admin"
admin.site.index_title = "Welcome to the Vote Admin"


class VoteAdmin(admin.ModelAdmin):
    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ["start_date"]
        else:
            return []


admin.site.register(Vote, VoteAdmin)
admin.site.register(Question)
admin.site.register(Answer)
