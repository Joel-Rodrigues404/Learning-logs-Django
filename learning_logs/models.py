from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Topic(models.Model):
    """Um assunto que o usuario esta aprendendo"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Topics'

    def __str__(self) -> str:
        """Devolve uma representaçao em string do model"""
        return self.text

class Entry(models.Model):
    """Algo especifico aprendido sobre um assunto"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'Entries'

    def __str__(self) -> str:
        """Devolve uma representação em string do modelo"""
        return self.text[:50] + "..."