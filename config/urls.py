from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from pedidos.views import ClienteViewSet, PedidoViewSet, ItensPedidoViewSet

router = DefaultRouter()
router.register(r'clientes', ClienteViewSet)
router.register(r'pedidos', PedidoViewSet)
router.register(r'itens_pedido', ItensPedidoViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
]