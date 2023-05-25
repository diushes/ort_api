import datetime
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.content


class Comment(models.Model):
    comment_text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"Comment by {self.user.username} on {self.post.title}"

    

