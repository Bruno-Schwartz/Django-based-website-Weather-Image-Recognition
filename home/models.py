from django.db import models


# Create your models here.

class ImagePrediction(models.Model):
    image = models.ImageField()
    predicted_class = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.predicted_class}"
