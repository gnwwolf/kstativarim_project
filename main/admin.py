from django.contrib import admin
from .models import Category, GalleryItem, Service, Order, ContactRequest


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['code', 'name_ru', 'sort_order']
    list_editable = ['sort_order']
    search_fields = ['name_ru', 'code']
    ordering = ['sort_order']


@admin.register(GalleryItem)
class GalleryItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'sort_order', 'created_at']
    list_filter = ['category']
    list_editable = ['sort_order']
    search_fields = ['title', 'description']
    list_select_related = ['category']
    fieldsets = (
        ('Основная информация', {
            'fields': ('title', 'category', 'description', 'sort_order')
        }),
        ('Изображение', {
            'fields': ('image',),
            'classes': ('collapse',)
        }),
    )


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'sort_order', 'is_active']
    list_filter = ['is_active']
    list_editable = ['sort_order', 'is_active']
    search_fields = ['title', 'description']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'service', 'status', 'created_at']
    list_filter = ['status', 'service', 'created_at']
    list_editable = ['status']
    search_fields = ['name', 'phone']
    readonly_fields = ['created_at']
    actions = ['mark_as_processing', 'mark_as_completed']

    def mark_as_processing(self, request, queryset):
        queryset.update(status='processing')
        self.message_user(request, 'Заказы отмечены как "В обработке"')

    mark_as_processing.short_description = 'Отметить как "В обработке"'

    def mark_as_completed(self, request, queryset):
        queryset.update(status='completed')
        self.message_user(request, 'Заказы отмечены как "Выполнены"')

    mark_as_completed.short_description = 'Отметить как "Выполнены"'


@admin.register(ContactRequest)
class ContactRequestAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'is_processed', 'created_at']
    list_filter = ['is_processed', 'created_at']
    list_editable = ['is_processed']
    search_fields = ['name', 'phone', 'message']
    readonly_fields = ['created_at']