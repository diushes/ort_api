from django.urls import path
from .views import PostListView, SinglePostView, SingleCommentView

urlpatterns = [
    path("posts/", PostListView.as_view(), name="all_posts"),
    path("posts/<int:pk>/", SinglePostView.as_view(), name="post_retrieve_update_destroy"),
    path("comments/<int:pk>/", SingleCommentView.as_view(), name="update_comment"),
]
