from django.db import models

# Create your models here.

class Mythical(models.Model):
    title = models.CharField(
        max_length=255
    )
    first_description = models.TextField(
        null=True,
        blank=True
    )
    second_description = models.TextField(
        null=True,
        blank=True
    )
    third_description = models.TextField(
        null=True,
        blank=True
    )
    first_image = models.ImageField(
        upload_to='mythicals_images'
    )
    second_image = models.ImageField(
        upload_to='mythicals_images',
        null=True,
        blank=True
    )
    third_image = models.ImageField(
        upload_to='mythicals_images',
        null=True,
        blank=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    is_trending = models.BooleanField(
        default=False
    )

    def __str__(self) -> str:
        return str(self.title)
