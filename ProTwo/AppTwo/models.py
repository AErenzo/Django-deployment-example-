from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Users(models.Model):
    first_name = models.CharField(max_length=264)
    last_name = models.CharField(max_length=264)
    email = models.EmailField(max_length=264, unique=True)
    # password = models.CharField(max_length=50)


    def __str__(self):
        return self.email


class ContactMessage(models.Model):
    first_name = models.CharField(max_length=125)
    last_name = models.CharField(max_length=125)
    email = models.EmailField(max_length=150)
    subject = models.CharField(max_length=150)
    message = models.CharField(max_length=2500)

    def __str__(self):
        return self.first_name, self.last_name, self.email, self.subject, self.message


class ProjectIdea(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    subject_genre = models.CharField(max_length=150)
    project_name = models.CharField(max_length=150)
    project_description = models.CharField(max_length=4000)


class UserProfileInfo(models.Model):

    # this create a one to one relationship to the Users class
    # we do this as we should not inherit from the User class
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # here we can add additional fields to our model
    # When creating a model from Users, we auto generate attributes for first and second name, email,
    # password and username
    portfolio_site = models.URLField(blank=True)

    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username