from rest_framework.routers import DefaultRouter

from usuario.router import router as UserRouter

router = DefaultRouter()
router.registry.extend(UserRouter.registry)