from rest_framework import routers
from news.views import NewsViewSet

router = routers.SimpleRouter()
router.register('news', NewsViewSet)
urlpatterns = router.urls
