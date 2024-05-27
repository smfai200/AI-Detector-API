from django.contrib import admin
from django.urls import path
from Detector.views import TextProcessingView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('classify/', TextProcessingView.as_view()),
]
