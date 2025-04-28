from django.db import models

class Projects(models.Model):
    title = models.CharField(max_length=70)
    description = models.TextField()
    pic = models.ImageField(default='github.jpg', blank=True)
    date =  models.DateTimeField(auto_now_add=True)
    github_repo_link = models.CharField(max_length=500, default='https://github.com/tethcode')
    live_link = models.CharField(max_length=500, default='https://x.com/tethcode')

    def __str__(self):
        return self.title


class Stack(models.Model):
    logo = models.ImageField(default='github.jpg', blank=True)
    name = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name