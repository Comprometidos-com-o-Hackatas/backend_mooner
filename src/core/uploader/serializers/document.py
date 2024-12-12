from rest_framework import serializers
import cloudinary.uploader
import uuid
import time
from core.uploader.helpers.files import CONTENT_TYPE_PDF, get_content_type, CONTENT_TYPE_MP3
from core.uploader.models import Document
timestamp = int(time.time())

CLOUD_NAME = "dhft56ct1"
API_KEY = "346858419386854"
API_SECRET = "Dg2bM10W5cFq7WuvCVhnf-1yts4"

cloudinary.config(
    cloud_name=CLOUD_NAME,
    api_key=API_KEY,
    api_secret=API_SECRET
)

class DocumentUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ["attachment_key", "file", "description", "uploaded_on"]
        read_only_fields = ["attachment_key", "uploaded_on"]
        extra_kwargs = {"file": {"write_only": True}}

    def validate_file(self, value):
        valid_content_types = [CONTENT_TYPE_PDF, CONTENT_TYPE_MP3]
        if get_content_type(value) not in valid_content_types:
            raise serializers.ValidationError("Invalid or corrupted document.")
        return value

    def create(self, validated_data):
        file = validated_data.pop('file')
        try:
            response = cloudinary.uploader.upload(
                file,
                resource_type='video',
                folder=f'Mooner/songs/',
            )
            validated_data['url'] = response['secure_url']
            validated_data['public_id'] = response['public_id']
            validated_data['public_id'] = uuid.uuid4()
            document = Document.objects.create(**validated_data)
            return document
        except cloudinary.exceptions.Error as e:
            print("Erro ao fazer upload para o Cloudinary:", str(e))
            raise serializers.ValidationError("Upload falhou.")

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['url'] = instance.url
        return representation

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ["url", "description", "uploaded_on", "attachment_key", "public_id"]
        read_only_fields = ["url", "attachment_key", "uploaded_on"]

    def create(self, validated_data):
        raise NotImplementedError("Use DocumentUploadSerializer to create document files.")
