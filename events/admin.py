from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Event, Category, Tag


class CustomUserAdmin(UserAdmin):
    list_display = ("username", "email", "role", "is_staff")
    fieldsets = UserAdmin.fieldsets + (("Role", {"fields": ("role",)}),)
    add_fieldsets = UserAdmin.add_fieldsets + (("Role", {"fields": ("role",)}),)



@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("title", "organizer", "status", "start_time", "end_time")
    list_filter = ("status", "is_public", "category", "tags")
    search_fields = ("title", "description", "location")
    raw_id_fields = ("organizer",)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


admin.site.register(User, CustomUserAdmin)
