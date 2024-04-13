from rest_framework import routers

from comments.views import CommentsViewSet
router = routers.SimpleRouter()
router.register('comments', CommentsViewSet)
urlpatterns = router.urls
