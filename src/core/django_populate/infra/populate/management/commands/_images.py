from core.uploader.models import Image
from django.core.files.base import ContentFile
from core.django_populate.media_files import covers
import os
import mimetypes
import cloudinary.uploader
import cloudinary
import uuid

# Configuração do Cloudinary
CLOUD_NAME = "dzdrwmug3"
API_KEY = "565711445643767"
API_SECRET = "IUqLGohAjDObKXWnjV-XJQcbI4c"

cloudinary.config(
    cloud_name=CLOUD_NAME,
    api_key=API_KEY,
    api_secret=API_SECRET
)

def populate_images():
    path = covers.__path__[0]

    for i in range(0, len(os.listdir(path))):
        file = os.listdir(path)[i]
        print(file)
        filename = os.path.join(path, file)

        try:
            if filename:
                with open(filename, 'rb') as f:
                    content = f.read()
                    content_type = mimetypes.guess_type(filename)[0]
                    content_file = ContentFile(content, name=filename)
                    content_file.content_type = content_type
                    response = cloudinary.uploader.upload(
                        content_file,
                        resource_type='raw',
                        folder='Mooner/images/',
                        public_id=str(uuid.uuid4())
                    )


                    # Criar o documento no banco de dados
                    cover = Image.objects.create(
                        description=file.replace(".jpg", ""),
                        file=content_file,
                        url=response['secure_url']
                    )
                    cover.save()
                    print(f"Upload e criação do documento {file} concluído com sucesso.")
        except Exception as e:
            print(f"Erro ao processar o arquivo {file}: {e}")
