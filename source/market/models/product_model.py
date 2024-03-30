import os

from django.utils import timezone
from django.db import models
from django.core.validators import MinValueValidator

from market.models import CategoryModel


def directory_path(instance, filename):
    product_name = instance.product_name.lower()
    return os.path.join(f'product_images', f'{product_name}_image_{filename}')


class ProductModel(models.Model):
    product_name = models.CharField(
        max_length=50,
        verbose_name="Продукт",
        null=False,
        blank=False
    )

    product_categories = models.ManyToManyField(
        to=CategoryModel,
        verbose_name="Категория",
        blank=True,
        null=True
    )

    product_image = models.ImageField(
        upload_to=directory_path,
        null=False,
        blank=False,
        verbose_name="Картинка продукта"
    )

    product_description = models.CharField(
        max_length=500,
        verbose_name="Описание",
        null=False,
        blank=False
    )

    product_qty = models.PositiveIntegerField(
        verbose_name="Количество",
        null=False,
        blank=False
    )

    product_price = models.FloatField(
        validators=[MinValueValidator(0)],
        verbose_name="Цена",
        null=False,
        blank=False
    )

    is_deleted = models.BooleanField(
        verbose_name='удалено',
        null=False,
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата и время создания"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата и время обновления"
    )
    deleted_at = models.DateTimeField(
        verbose_name='Дата и время удаления',
        blank=True,
        null=True,
        default=None
    )

    def __str__(self):
        return f"{self.product_name}"

    @property
    def as_dict(self):
        return {
            'id': self.pk,
            'product_name': self.product_name,
            'product_categories': self.product_categories,
            'product_image': self.product_image,
            'product_description': self.product_description,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'deleted_at': self.deleted_at,
            'is_deleted': self.is_deleted,
        }

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
    
    def delete(self, *args, **kwargs):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save(update_fields=['is_deleted', 'deleted_at'])
