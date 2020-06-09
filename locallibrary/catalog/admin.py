from django.contrib import admin
from .models import (Book,
                     Author,
                     Genre,
                     BookInstance,
                     Language,)

# Register your models here.

class BookInstanceInline(admin.StackedInline):
    model = BookInstance

    extra = 0

    fieldsets = (
        ('General', {
            'fields': ('book','imprint','id')
        }),
        ('Availability', {
            'fields': ('status','due_back','borrower',)
        })
    )

class BookInline(admin.StackedInline):
    model = Book
    extra = 0
    fieldsets = (
        ('General', {
            'fields': ('author','language','isbn','genre')
        }),
        ('Summary', {
            'fields': ('summary',)
        })
    )


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    field = ['last_name',
              'first_name',
              ('date_of_birth',
                'date_of_death')
              ]
    inlines = [BookInline,
               ]


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BookInstanceInline]


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'due_back', 'borrower',)
    list_filter = ('status', 'due_back')

    fieldsets = (
        ('General', {
            'fields': ('book','imprint','id')
        }),
        ('Availability', {
            'fields': ('status','due_back','borrower',)
        })
    )


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    pass
