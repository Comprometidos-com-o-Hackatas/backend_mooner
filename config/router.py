from rest_framework.routers import DefaultRouter
from mooner import views
from usuario.router import router as UserRouter

router = DefaultRouter()
router.register(r'song',  views.SongViewSet)
router.registry.extend(UserRouter.registry)