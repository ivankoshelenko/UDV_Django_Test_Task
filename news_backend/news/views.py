from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from comments.models import Comments
from news.models import News
from news.serializers import NewsSerializer


class NewsViewSet(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    http_method_names = ['post', 'get', 'put', 'delete', 'patch']

    def list(self,request):
        news = News.objects.filter(deleted=False).values()
        for article in news:
            article['comments_count'] = len(Comments.objects.filter(news_id=article["id"]).values())
        return Response(data={"news":news,"news_count":len(news)})

    def retrieve(self, request, *args, **kwargs):
        try:
            news_data = News.objects.filter(pk=self.kwargs["pk"]).values()[0]
        except:
            raise Http404("Article does not exist")
        if news_data["deleted"] == True:
            raise Http404("Article was deleted")
        comments =Comments.objects.filter(news_id=self.kwargs["pk"]).values()
        news_data['comments'] = comments
        news_data['comments_count'] = len(comments)
        return Response(data=news_data)

    def destroy(self, request, *args, **kwargs):
        try:
            article = self.get_object()
        except:
            raise Http404("Article does no exist")
        if (article.deleted == True):
            raise Http404("Article already deleted")
        article.deleted = True
        article.save()
        return Response(data={"detail": "Article successfuly deleted"})

