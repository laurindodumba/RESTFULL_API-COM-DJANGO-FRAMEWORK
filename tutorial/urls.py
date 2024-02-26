from rest_framework.routers import DefaultRouter
from books.api import viewsets as booksviewsets
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers
from django.urls import path, include
from django.contrib import admin



# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'books/', booksviewsets.BooksViewSet, basename="Book")  # Use 'BooksViewSet' instead of 'BooksViewset'

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

router.urls
