from django.contrib import admin

# Register your models here.
from app.models import Post, Like, Comment


class CommentInLine(admin.StackedInline):
    model = Comment


class ViewPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'post_name', 'user')

    inlines = (CommentInLine,)


class ViewLikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'user')


class ViewCommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'user')


admin.site.register(Post, ViewPostAdmin)
admin.site.register(Like, ViewLikeAdmin)
admin.site.register(Comment, ViewCommentAdmin)
