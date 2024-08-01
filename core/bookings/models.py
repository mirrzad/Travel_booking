from django.db import models
from django.core.validators import MinValueValidator


class Trip(models.Model):
    destination = models.CharField(max_length=100)
    departure_date = models.DateField()
    return_date = models.DateField()
    number_of_travelers = models.IntegerField(default=1, validators=[MinValueValidator(1)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return f'{self.destination}: ({self.departure_date} - {self.return_date})'

