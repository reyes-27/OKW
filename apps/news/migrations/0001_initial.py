# Generated by Django 4.2.7 on 2024-03-21 22:45

import apps.news.utils
import ckeditor.fields
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('categories', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('likes', models.PositiveIntegerField(default=0)),
                ('text', models.TextField()),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('edited', models.BooleanField(default=False)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='news.comment')),
            ],
        ),
        migrations.CreateModel(
            name='Dislike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('already_disliked', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('already_liked', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('header', models.CharField(max_length=255)),
                ('description', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('likes', models.PositiveIntegerField(default=0)),
                ('dislikes', models.PositiveIntegerField(default=0)),
                ('edited', models.BooleanField(default=False)),
                ('categories', models.ManyToManyField(related_name='posts', to='categories.category')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post_parent', to='news.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_posts', to='accounts.customer')),
                ('user_dislikes', models.ManyToManyField(related_name='user_disliked_posts', through='news.Dislike', to=settings.AUTH_USER_MODEL)),
                ('user_likes', models.ManyToManyField(related_name='user_liked_posts', through='news.Like', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PostImage',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('image', django_resized.forms.ResizedImageField(crop=None, force_format='JPEG', keep_meta=True, quality=100, scale=1, size=[1920, 1080], upload_to=apps.news.utils.image_path)),
                ('level', models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(10)])),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image_set', to='news.post')),
            ],
        ),
        migrations.AddField(
            model_name='like',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts_likes', to='news.post'),
        ),
        migrations.AddField(
            model_name='like',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users_likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='dislike',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts_dislikes', to='news.post'),
        ),
        migrations.AddField(
            model_name='dislike',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users_dislikes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='CommentLike',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('already_liked', models.BooleanField(default=False)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_likes', to='news.comment')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users_comment_likes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='news.post'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_comments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='user_likes',
            field=models.ManyToManyField(through='news.CommentLike', to=settings.AUTH_USER_MODEL),
        ),
    ]
