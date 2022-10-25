
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from apps.cadastrar_eventos.views import EventoViewSet, InscritoViewSet

router = routers.DefaultRouter()
router.register('eventos', EventoViewSet)
router.register('inscritos', InscritoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include('apps.usuarios.urls')),
    path('api', include(router.urls)),
    path('', include('apps.cadastrar_eventos.urls')),
    path('enviar/', include('apps.enviar.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
