from django.db import models

class Move(models.Model):
    value = models.CharField(max_length=140)
    game = models.ForeignKey('Game')

    def __str__(self):
        return self.value

class Game(models.Model):
    title = models.CharField(max_length=140, primary_key=True)

    def __str__(self):
        return self.title