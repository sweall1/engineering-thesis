from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



class Comment(models.Model):
    STATUS = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )
    Comment = models.CharField(max_length=200, null=True)
    Quality = models.IntegerField(null=True, choices=STATUS)
    Price = models.IntegerField(null=True, choices=STATUS)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.Comment


class Category(models.Model):
    Name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.Name


class Task(models.Model):
    Description = models.CharField(max_length=200, null=True)
    Phone = models.FloatField(null=True)

    def __str__(self):
        return self.Description

class NewCategory(models.Model):
    Description = models.CharField(max_length=200, null=True)


    def __str__(self):
        return self.Description



class Workshop(models.Model):
    Name = models.CharField(max_length=200, null=True)
    Category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    Description = models.CharField(max_length=200, null=True)
    Comment = models.ManyToManyField(Comment, blank=True)
    City = models.CharField(max_length=200, null=True)
    StreetName = models.CharField(max_length=200, null=True)
    ZipCode = models.CharField(max_length=200, null=True)
    NIP = models.CharField(max_length=200, null=True)
    Task = models.ManyToManyField(Task, blank=True)
    Quality = models.IntegerField(null=True)
    Price = models.IntegerField(null=True)

    def __str__(self):
        return self.Name










