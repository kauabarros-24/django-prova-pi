from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from alunos.views import EstadoViewSet, AlunoViewSet, CidadeViewSet

router = DefaultRouter()
router.register(r'estados', EstadoViewSet)
router.register(r'cidades', CidadeViewSet)
router.register(r'alunos', AlunoViewSet)



urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
]