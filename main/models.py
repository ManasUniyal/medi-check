from django.db import models


class Prediction(models.Model):

    NORMAL = 0
    PNEUMONIA = 1
    COVID = 2

    OPTIONS = (
        (NORMAL, 'Normal'),
        (PNEUMONIA, 'Pneumonia'),
        (COVID, "COVID"),
    )

    # user = models.OneToOneField(User, null=True, on_delete=models.CASCADE())
    uploaded_image_url = models.URLField(null=True)
    processed_image_url = models.URLField(null=True)
    diagnosis = models.CharField(max_length=15, choices=OPTIONS)
    accuracy = models.DecimalField(max_digits=4, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True)
