from django.db import models
from ckeditor.fields import RichTextField
import uuid
from apps.categories.models import Category
from apps.accounts.models import Customer, CustomUser
from django_resized import ResizedImageField
from django.core.validators import MaxValueValidator
from .utils import image_path


# Create your models here.
class Like(models.Model):
    user =                      models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="users_likes")
    post =                      models.ForeignKey("Post", on_delete=models.CASCADE, related_name="posts_likes")
    already_liked =             models.BooleanField(default=False)
    def save(self, *args, **kwargs):
        print("pene")
        if not self.already_liked:
            self.post.likes += 1
            self.already_liked = True
            self.post.save()
        super(Like, self).save(*args, **kwargs)
    def delete(self, *args, **kwargs):
        self.post.likes -= 1
        self.post.save()
        super(Like, self).delete(*args, **kwargs)
class Dislike(models.Model):
    user =                      models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="users_dislikes")
    post =                      models.ForeignKey("Post", on_delete=models.CASCADE, related_name="posts_dislikes")
    already_disliked =          models.BooleanField(default=False)
    def save(self, *args, **kwargs):
        if not self.already_disliked:
            self.post.dislikes += 1
            self.already_disliked = True
            self.post.save()
        super(Dislike, self).save(*args, **kwargs)
    def delete(self, *args, **kwargs):
        self.post.dislikes -= 1
        self.post.save()
        super(Dislike, self).delete(*args, **kwargs)

class CommentLike(models.Model):
    user =                          models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="users_comment_likes")
    comment =                       models.ForeignKey("Comment", on_delete=models.CASCADE, related_name="comment_likes")
    already_liked =                 models.BooleanField(default=False)
    def save(self, *args, **kwargs):
        if not self.already_liked:
            self.comment.likes += 1
            self.already_liked = True
            self.comment.save()
        super(CommentLike, self).save(*args, **kwargs)
    def delete(self, *args, **kwargs):
        self.comment.likes -= 1
        self.comment.save()
        super(CommentLike, self).delete(*args, **kwargs)

class Post(models.Model):
    parent =                models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name="post_parent")
    id =                    models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user =                  models.ForeignKey(Customer, on_delete=models.CASCADE, related_name="user_posts")
    header =                models.CharField(max_length=255)
    description =           RichTextField(blank=True, null=True)
    pub_date =              models.DateTimeField(auto_now_add=True)
    category =              models.ManyToManyField(Category, related_name="posts")
    likes =                 models.PositiveIntegerField(default=0)
    dislikes =              models.PositiveIntegerField(default=0)
    user_dislikes =         models.ManyToManyField(
                                                    CustomUser,
                                                    through=Dislike,
                                                    through_fields=(
                                                        "post",
                                                        "user",
                                                    ),
                                                    related_name="user_disliked_posts"
                                                    )
    user_likes =            models.ManyToManyField(
                                                    CustomUser,
                                                    through=Like,
                                                    through_fields=(
                                                        "post",
                                                        "user",
                                                    ),
                                                    related_name="user_liked_posts"
                                                    )
    edited =                models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.pk:
            self.edited = True
        super(Post, self).save(*args, **kwargs)
        

class PostImage(models.Model):
    id =                models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    image =             ResizedImageField(upload_to=image_path)
    post =              models.ForeignKey(Post, on_delete=models.CASCADE, related_name="image_set")
    level =             models.PositiveSmallIntegerField(validators=[MaxValueValidator(10)])     
     
class Comment(models.Model):
    id =                models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    parent =            models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True)
    user =              models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="user_comments")
    post =              models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    user_likes =        models.ManyToManyField(
                                                CustomUser,
                                                through=CommentLike,
                                                through_fields=(
                                                    "comment",
                                                    "user",
                                                    ),
                                                )
    likes =             models.PositiveIntegerField(default=0)
    text =              models.TextField()
    pub_date =          models.DateTimeField(auto_now_add=True)
    edited =            models.BooleanField(default=False)
    

