from django.contrib import admin
from .models import PhotoModel, CommentModel
# Register your models here.
admin.site.register(PhotoModel)
admin.site.register(CommentModel)