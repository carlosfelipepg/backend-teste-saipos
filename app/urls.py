from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from main import views

router = routers.DefaultRouter()
router.register(r'tarefas', views.TarefasViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'api/', include(router.urls)),
]
