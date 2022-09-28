from django.contrib import admin

from .models import Book, Review


class ReviewInLine(admin.TabularInline):
    model = Review


class BookAdmin(admin.ModelAdmin):
    inlines = [
        ReviewInLine,
    ]
    list_display = ("title", "price", "author")


admin.site.register(Book, BookAdmin)
