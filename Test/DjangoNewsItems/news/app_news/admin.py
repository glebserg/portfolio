from django.contrib import admin
from .models import NewsItem, Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ['name_author', 'news', 'text', 'check_admin', 'show_piece_text']
    list_filter = ['name_author']
    search_fields = ['name_author']

    actions = ['switch_to_status_deleted']

    def show_piece_text(self, queryset):
        text = queryset.text

        if len(text) >= 15:
            queryset.text = f'{text[:15]}...'

        return queryset

    def switch_to_status_deleted(self, request, queryset):
        queryset.update(check_admin=False, text='Удалено администратором')

    switch_to_status_deleted.short_description = 'Перевести в статус - Удалено администратором'
    show_piece_text.short_description = 'Текст комментария'


class CommentInLine(admin.TabularInline):
    model = Comment


class NewsItemAdmin(admin.ModelAdmin):
    model = NewsItem

    list_display = ['title', 'create_date', 'edit_date', 'flag_active']
    list_filter = ['flag_active']
    search_fields = ['title']
    inlines = [CommentInLine]

    actions = ['mark_as_active', 'mark_as_inactive']

    def mark_as_active(self, request, queryset):
        queryset.update(flag_active=True)

    def mark_as_inactive(self, request, queryset):
        queryset.update(flag_active=False)

    mark_as_active.short_description = 'Перевести в статус - Активно'
    mark_as_inactive.short_description = 'Перевести в статус - Неактивно'


admin.site.register(NewsItem, NewsItemAdmin)
admin.site.register(Comment, CommentAdmin)
