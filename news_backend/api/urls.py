from rest_framework import routers
from comments.views import CommentsViewSet
from news.views import NewsViewSet

router = routers.SimpleRouter()
router.register('news', NewsViewSet)
router.register('comments', CommentsViewSet)
urlpatterns = router.urls
