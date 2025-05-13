# blog/models.py

from django.db import models
from django.conf import settings

class BlogPost(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="posts")
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to="blog_images/", blank=True, null=True)
    attachment = models.FileField(upload_to="blog_files/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    views = models.PositiveIntegerField(default=0)
    is_blocked = models.BooleanField(default=False)    

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_blocked = models.BooleanField(default=False)   

    def __str__(self):
        return f"Comment by {self.user.email} on {self.blog_post.title}"

class Reaction(models.Model):
    LIKE = 'like'
    UNLIKE = 'unlike'
    REACTION_CHOICES = [
        (LIKE, 'Like'),
        (UNLIKE, 'Unlike'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='reactions')
    type = models.CharField(max_length=10, choices=REACTION_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'blog_post') 

    def __str__(self):
        return f"{self.user.email} - {self.type} on {self.blog_post.title}"

