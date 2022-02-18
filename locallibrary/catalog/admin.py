from django.contrib import admin

# Register your models here.
from .models import Author, Genre, Book, BookInstance, Language

# admin.site.register(Book)
# admin.site.register(Author)
admin.site.register(Genre)
# admin.site.register(BookInstance)
admin.site.register(Language)




#—оздаем новый класс, прив€зывавем к нему бук, ставим атрибут TabularInline
class BooksInline(admin.TabularInline):
    model = Book
    extra =0   
# —верху мы закомментировали три объекта и снизу менем их разными способами
# Define the admin class
# «десь мы походу сделали чтобы при выыборе автора выпадал список с годами жизни
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BooksInline]
#inlines добавл€ем доп строчки под авторами

# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)
# Register the Admin classes for Book using the decorator



#здесь мы объ€вили новый класс
class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    extra =0

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]

# Register the Admin classes for BookInstance using the decorator
#не пон€тно почему указываем BOOK а не TITLE
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book','status','borrower', 'due_back','id')
    list_filter = ('status', 'due_back')
    fieldsets = (
        (None, {
            'fields': ('book','imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )