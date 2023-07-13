from django.urls import path

from .views import home, result
from .ajax import upload_file


urlpatterns = [
    path('', home, name='home'),
    path('result/', result, name='result'),
    path('ajax/upload-file/', upload_file),
]
