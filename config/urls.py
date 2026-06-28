from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("api.urls")),
    path("v1/auth/", include("auth.urls")),
    path("v1/", include("statistic.urls")),
    path('api-auth/', include('rest_framework.urls')),
    path("docs/", include("swagger_urls")),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) # این رو اضافه کن
