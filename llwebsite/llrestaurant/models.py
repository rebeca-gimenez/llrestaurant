from django.db import models

# Create your models here.
class Reservation(models.Model):
    first_name = models.CharField(max_length = 100, verbose_name = "First name")
    last_name = models.CharField(max_length = 100, verbose_name = "Last name")
    day = models.DateField(help_text="format (yyyy-mm-dd)", verbose_name = "Day")
    seats = models.IntegerField(verbose_name = "Number of seats")
    comments = models.CharField(max_length = 200, verbose_name = "Additional information (phone number, email, comments)")

    def __str__(self):
        return self.first_name + ' ' + self.last_name

class Menu(models.Model):
    dish = models.CharField(max_length = 100)
    price = models.IntegerField()
    ingredients = models.CharField(max_length = 200)
    slug = models.SlugField(default="", null=False)

    def __str__(self):
        return self.dish