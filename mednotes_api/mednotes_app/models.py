from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator

class Note(models.Model):
    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=30)
    title = models.CharField(max_length=50)
    description = models.TextField()
    #bodyChart = models.ImageField()
    #attachment = models.FileField()
    bodyChart = models.ImageField(
        upload_to='bodycharts/',
        validators=[FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])]
    )
    remarks = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)


class Attachment(models.Model):
    file = models.FileField(
        upload_to='attachments/',
        validators=[FileExtensionValidator(allowed_extensions=['pdf', 'jpg', 'png', 'jpeg'])]
    )
    note = models.ForeignKey(Note, related_name='attachments', on_delete=models.CASCADE)

    def __str__(self):
        return self.file.name


def save(self, *args, **kwargs):
    if not self.slug:
        self.slug = self._generate_unique_slug()
    super().save(*args, **kwargs)

def _generate_unique_slug(self):
    slug_base = slugify(self.tile)
    unique_slug = slug_base

    while Note.objects.filter(slug = unique_slug).exists():
        unique_slug = f"{slug_base}-{get_random_string(5)}"

    return unique_slug
