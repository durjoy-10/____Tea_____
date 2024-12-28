from django.db import models

class Review(models.Model):
    name = models.CharField(max_length=100)
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])  # Ratings from 1 to 5
    review = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.rating} Stars"
