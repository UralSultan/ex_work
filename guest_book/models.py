from django.db import models

class Guestbook(models.Model):
    STATUS_CHOICES = [
        ('active', 'Активно'),
        ('blocked', 'Заблокировано'),
    ]

    author_name = models.CharField(max_length=100, verbose_name='Имя автора')
    author_email = models.EmailField(verbose_name='Email автора')
    content = models.TextField(verbose_name='Текст записи')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='active',
        verbose_name='Статус'
    )
