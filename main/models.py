from django.db import models


class Result(models.Model):

    RESULT = (
        ('NORMAL', 'Normal'),
        ('PNEUMONIA', 'Pneumonia'),
        ('COVID', "COVID"),
    )

    # user = models.OneToOneField(User, null=True, on_delete=models.CASCADE())
    uploaded_image = models.ImageField()
    processed_image = models.ImageField()
    result = models.CharField(max_length=15, choices=RESULT)
    accuracy = models.DecimalField(max_digits=4, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True)
