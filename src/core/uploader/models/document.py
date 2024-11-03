import mimetypes
import uuid

from django.db import models
from core.uploader.helpers.files import get_content_type


def document_file_path(document, _) -> str:
    content_type = get_content_type(document.file)
    extension: str = mimetypes.guess_extension(content_type)

    return f"Mooner/songs/{document.public_id}{extension or ''}"


class Document(models.Model):
    attachment_key = models.UUIDField(
        max_length=255,
        default=uuid.uuid4,
        unique=True,
        help_text=("Used to attach the document to another object. " "Cannot be used to retrieve the document file."),
    )
    public_id = models.UUIDField(
        max_length=255,
        default=uuid.uuid4,
        unique=True,
        help_text=(
            "Used to retrieve the document file itself. "
            "Should not be readable until the document is attached to another object."
        ),
    )
    file = models.FileField(upload_to=document_file_path)
    description = models.CharField(max_length=255, blank=True)
    uploaded_on = models.DateTimeField(auto_now_add=True)
    url = models.URLField(null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.description} - {self.file.name}"
