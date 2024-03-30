from django.db import models


class CategoryModel(models.Model):
    category_name = models.CharField(
        max_length=50,
        verbose_name="Категория",
        null=False,
        blank=False
    )

    def __str__(self):
        return f"{self.category_name}"

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        