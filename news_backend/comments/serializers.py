from rest_framework import serializers

from comments.models import Comments


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = "__all__"
