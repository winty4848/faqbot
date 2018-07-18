from django.db import models

class Game(models.Model):
    user_key = models.CharField(max_length=255, primary_key=True)
    ## 이긴 횟수
    win = models.IntegerField()
    ## 비긴횟수
    draw = models.IntegerField()
    ## 진 횟수
    lose = models.IntegerField()


