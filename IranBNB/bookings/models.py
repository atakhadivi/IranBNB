from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    phone_number = models.CharField(max_length=15, unique=True, blank=True, null=True)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.username


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    airbnb_listing_id = models.CharField(max_length=100)  # Store Airbnb ID
    check_in = models.DateField()
    check_out = models.DateField()
    guests = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.airbnb_listing_id}"
