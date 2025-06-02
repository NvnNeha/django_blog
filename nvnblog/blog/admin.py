from django.contrib import admin
from .models import Post, Tag, Comment

# Register your models here.

class PostAdminForm(admin.ModelAdmin):
    prepopulated_fields = {"slug":("title",)}
    list_display=("title","slug",)


admin.site.register(Post, PostAdminForm)
admin.site.register(Tag)
admin.site.register(Comment)
