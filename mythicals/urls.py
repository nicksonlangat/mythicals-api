from rest_framework import routers

from .views import MythicalViewset

router = routers.DefaultRouter()

router.register(r'', MythicalViewset, basename='mythicals')

urlpatterns = router.urls