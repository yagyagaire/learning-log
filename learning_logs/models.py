from django.db import models
from django.db.models.fields.related import ForeignKey
from django.contrib.auth.models import User
from django.forms.widgets import Widget

class Topic(models.Model):
    """A topic the user is learning about."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text

class Entry(models.Model):
    """An entry about learnings related to a topic."""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField(help_text="Describe your entry.")
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return f'"{self.text[:50]}..." in {self.topic.text}'
        