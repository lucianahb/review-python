from django.db import models
from django.utils import timezone


class Responsible(models.Model):
    responsible = models.CharField(max_length=250, null=False, blank=False, default='')

    def __str__(self):
        return self.responsible


class Tag(models.Model):
    tag = models.CharField(max_length=30, null=False, blank=False, default='')

    def __str__(self):
        return self.tag


class Activity(models.Model):

    status_choice = [("TODO", "To do"), ("DOING", "Doing"), ("DONE", "Done")]

    title = models.CharField(max_length=50)
    note = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    deadline = models.DateField()
    status = models.CharField(max_length=50, choices=status_choice)
    responsible = models.ForeignKey(Responsible, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} | Status: {self.status}"
