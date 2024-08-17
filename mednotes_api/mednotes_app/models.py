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
