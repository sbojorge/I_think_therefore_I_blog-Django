from django.contrib import admin
from .models import Post, Comments
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    summernote_fields = ('content',)


@admin.register(Comments)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('name', 'body', 'post', 'approved', 'created_on')
    list_filter = ('approved', 'created_on')
    search_fields = ['name', 'email', 'body']
    actions = ['approved_comment']

    def approved_comment(self, request, queryset):
        queryset.update(approved=True)
        

