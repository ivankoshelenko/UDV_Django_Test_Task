from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from comments.models import Comments
from comments.serializers import CommentsSerializer


class CommentsViewSet(ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    http_method_names = ['post', 'get', 'put', 'delete', 'patch']

    def list(self, request):
        comments = Comments.objects.all().values()
        return Response(data={"comments": comments, "comments_count": len(comments)})
