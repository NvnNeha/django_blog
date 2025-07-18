from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage

class StaticFileStorage(S3Boto3Storage):
    # location = "static"
    # default_acl = "public-read"
    location = settings.STATICFILES_FOLDER


class MediaFileStorage(S3Boto3Storage):
    # location = "media"
    # file_overwrite = False
    location = settings.MEDIAFILES_FOLDER