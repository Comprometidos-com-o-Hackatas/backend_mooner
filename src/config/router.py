from rest_framework.routers import DefaultRouter
from core.mooner import views
from core.usuario.router import router as UserRouter
from core.uploader.router import router as UploaderRouter

router = DefaultRouter()
router.register(r'song',  views.SongViewSet)
router.register(r'genre', views.GenreViewSet)
router.register(r'producer', views.ProducerViewSet)
router.register(r'luna', views.LunaAIViewSet)
router.register(r'history', views.HistoryViewSet)
router.registry.extend(UserRouter.registry)
router.registry.extend(UploaderRouter.registry)
