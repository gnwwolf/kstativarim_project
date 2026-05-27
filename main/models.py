from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



class Category(models.Model):
    """Категории работ для галереи"""
    code = models.CharField(max_length=50, unique=True, verbose_name='Код категории')
    name_ru = models.CharField(max_length=100, verbose_name='Название (рус.)')
    sort_order = models.IntegerField(default=0, verbose_name='Порядок сортировки')

    class Meta:
        ordering = ['sort_order', 'id']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name_ru


class GalleryItem(models.Model):
    """Работы в галерее"""
    title = models.CharField(max_length=255, verbose_name='Название работы')
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='gallery_items',
        verbose_name='Категория'
    )
    image = models.ImageField(
        upload_to='gallery/',
        verbose_name='Изображение'
    )
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    sort_order = models.IntegerField(default=0, verbose_name='Порядок сортировки')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    class Meta:
        ordering = ['sort_order', '-created_at']
        verbose_name = 'Работа в галерее'
        verbose_name_plural = 'Работы в галерее'

    def __str__(self):
        return self.title


class Service(models.Model):
    """Услуги компании"""
    title = models.CharField(max_length=200, verbose_name='Название услуги')
    description = models.TextField(verbose_name='Описание')
    icon = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        help_text='Font Awesome иконка (например: fa-car, fa-hammer)',
        verbose_name='Иконка'
    )
    sort_order = models.IntegerField(default=0, verbose_name='Порядок сортировки')
    is_active = models.BooleanField(default=True, verbose_name='Активна')

    class Meta:
        ordering = ['sort_order', 'id']
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return self.title


class Order(models.Model):
    """Заказы клиентов"""
    STATUS_CHOICES = [
        ('new', 'Новая'),
        ('processing', 'В обработке'),
        ('completed', 'Выполнена'),
        ('cancelled', 'Отменена'),
    ]

    name = models.CharField(max_length=150, verbose_name='Имя клиента')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    service = models.ForeignKey(
        Service,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Услуга'
    )
    custom_request = models.TextField(blank=True, null=True, verbose_name='Пожелания')
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='new',
        verbose_name='Статус'
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'{self.name} - {self.created_at.strftime("%d.%m.%Y")}'


class ContactRequest(models.Model):
    """Заявки на консультацию"""
    name = models.CharField(max_length=150, verbose_name='Имя')
    phone = models.CharField(max_length=20, verbose_name='Телефон')
    message = models.TextField(blank=True, null=True, verbose_name='Сообщение')
    is_processed = models.BooleanField(default=False, verbose_name='Обработано')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Заявка на консультацию'
        verbose_name_plural = 'Заявки на консультацию'

    def __str__(self):
        return f'{self.name} - {self.created_at.strftime("%d.%m.%Y")}'