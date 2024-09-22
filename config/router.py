from rest_framework.routers import DefaultRouter
from mooner import views
from usuario.router import router as UserRouter

router = DefaultRouter()
router.register(r'song',  views.SongViewSet)
router.register(r'genre', views.GenreViewSet)
router.register(r'producer', views.ProducerViewSet)
router.registry.extend(UserRouter.registry)