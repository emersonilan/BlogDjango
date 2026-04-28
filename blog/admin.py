from django.contrib import admin

from .models import Categoria, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    prepopulated_fields = {
        'slug': ('titulo',)
    }


admin.site.register(Categoria)