from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField() 
    profile_picture = models.ImageField(upload_to='profile_pictures/')
    birth_data = models.DateField()
    location = models.CharField(max_length=30) 


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content= models.TextField() 
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField()
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    image = models.ImageField(upload_to='post_images/')
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    dislikes = models.ManyToManyField(User, related_name='dislikes', blank=True)
    def __str__(self):
        return self.title


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.TextField() 
    created_at = models.DateTimeField(auto_now_add=True)


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50) 
    description = models.TextField()


class PostCategory(models.Model):
    id = models.AutoField(primary_key=True);
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
