from django.contrib import admin

from .models import Categoria, Post, Comment

from .models import Comment


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    prepopulated_fields = {
        'slug': ('titulo',)
    }


admin.site.register(Categoria)

admin.site.register(Comment)