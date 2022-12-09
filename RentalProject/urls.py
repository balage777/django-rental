from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('rentals.urls')),
    path('rentals/', include('rentals.urls')),
    path('admin/', admin.site.urls),
]