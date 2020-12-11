from django.contrib.auth.models import User
from django.db import models


class Prediction(models.Model):

    COVID = 0
    NORMAL = 1
    PNEUMONIA = 2

    OPTIONS = (
        (COVID, "COVID"),
        (NORMAL, 'Normal'),
        (PNEUMONIA, 'Pneumonia'),
    )

    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    uploaded_image_url = models.URLField(null=True)
    processed_image_url = models.URLField(null=True)
    diagnosis = models.CharField(max_length=15, choices=OPTIONS)
    date_created = models.DateTimeField(auto_now_add=True)
