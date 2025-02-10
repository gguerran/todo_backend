import filetype
import io

from rest_framework.fields import FileField
from rest_framework.serializers import ValidationError
from drf_extra_fields.fields import Base64FieldMixin


class Base64VideoFileField(Base64FieldMixin, FileField):
    ALLOWED_TYPES = ["mp4", "webm", "ogg", "avi", "flv", "mov", "wmv", "mkv"]

    INVALID_FILE_MESSAGE = "Por favor carregue um documento válido."
    INVALID_TYPE_MESSAGE = "O tipo do documento não pôde ser determinado."

    def get_file_extension(self, filename, decoded_file):
        extension = filetype.guess_extension(decoded_file)
        if extension is None:
            try:
                from PIL import Image

                image = Image.open(io.BytesIO(decoded_file))
            except (ImportError, OSError):
                raise ValidationError(self.INVALID_FILE_MESSAGE)
            else:
                extension = image.format.lower()

        return "jpg" if extension == "jpeg" else extension
