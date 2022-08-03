from django.db import models

# Create your models here.
class IdeaData(models.Model):
    title = models.TextField()
    due = models.TextField()
    link = models.TextField()

    def __str__(self):
        return self.title
    class Meta:
        constraints = [
            models.UniqueConstraint(fields = ['title', 'due', 'link'], name = 'idea_contest')
        ]

class WebData(models.Model):
    title = models.TextField()
    due = models.TextField()
    link = models.TextField()

    def __str__(self):
        return self.title
    class Meta:
        constraints = [
            models.UniqueConstraint(fields = ['title', 'due', 'link'], name = 'web_contest')
        ]

class EngineeringData(models.Model):
    title = models.TextField()
    due = models.TextField()
    link = models.TextField()

    def __str__(self):
        return self.title
    class Meta:
        constraints = [
            models.UniqueConstraint(fields = ['title', 'due', 'link'], name = 'engineering_contest')
        ]

class SwData(models.Model):
    title = models.TextField()
    due = models.TextField()
    link = models.TextField()

    def __str__(self):
        return self.title
    class Meta:
        constraints = [
            models.UniqueConstraint(fields = ['title', 'due', 'link'], name = 'sw_contest')
        ]
    
class SpartanEdu(models.Model):
    title = models.TextField()
    link = models.TextField()
    
    def __str__(self):
        return self.title
    class Meta:
        constraints = [
            models.UniqueConstraint(fields = ['title', 'link'], name = 'spartan_notice')
        ]