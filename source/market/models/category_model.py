from django.db import models


class CategoryModel(models.Model):
    category_name = models.CharField(
        max_length=50,
        verbose_name="Категория",
        null=False,
        blank=False
    )
