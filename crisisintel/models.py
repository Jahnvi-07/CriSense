from django.db import models


class Prediction(models.Model):
    tweet = models.TextField()
    category = models.CharField(max_length=100)
    confidence = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.category 