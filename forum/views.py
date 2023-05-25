from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListAPIView
from .serializers import PostSerializer
from .models import Post, Comment

class PostListView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class SinglePostView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class SingleCommentView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

