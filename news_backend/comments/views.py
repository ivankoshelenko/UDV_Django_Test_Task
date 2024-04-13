from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet
from comments.models import Comments
from comments.serializers import CommentsSerializer


class CommentsViewSet(ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    http_method_names = ['post', 'get', 'put', 'delete', 'patch']
    permission_classes = (permissions.AllowAny,)
