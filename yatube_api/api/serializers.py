from rest_framework import serializers

from posts.models import Comment, Group, Post


class PostSerializer(serializers.ModelSerializer):
    group = serializers.StringRelatedField(read_only=True)
    comments = serializers.StringRelatedField(
        many=True,
        read_only=True,
        required=False
    )
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        model = Post
        fields = (
            'id', 'text', 'author', 'pub_date', 'image', 'group', 'comments'
        )


class GroupSerializer(serializers.ModelSerializer):
    posts = serializers.StringRelatedField(
        many=True,
        read_only=True,
        required=False
    )

    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description', 'posts')


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        model = Comment
        fields = ('id', 'post', 'created', 'author', 'text')
        read_only_fields = ('post',)
