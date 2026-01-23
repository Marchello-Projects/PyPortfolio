from django.contrib import admin
from .models import Skill, Cv, CvFile

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['code']
    search_fields = ['code']

@admin.register(Cv)
class CvAdmin(admin.ModelAdmin):
    list_display = ['user', 'work_email', 'phone_number', 'display_skills']

    def display_skills(self, obj):
        return ", ".join([str(skill) for skill in obj.skills.all()])
    
    display_skills.short_description = 'Skills'

@admin.register(CvFile)
class CvFileAdmin(admin.ModelAdmin):
    list_display = ['user', 'cv', 'file', 'created_at']
    list_filter = ['created_at',]
    search_fields = ['user__username', 'cv__work_email']
    readonly_fields = ['created_at',]

    def has_add_permission(self, request):
        return False