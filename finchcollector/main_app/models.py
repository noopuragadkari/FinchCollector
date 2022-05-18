from django.db import models
from django.urls import reverse

MEALS = (
    ('B', 'Breakfast'),
    ('L', 'Lunch'),
    ('D', 'Dinner')
)

class Toy(models.Model):
    name = models.CharField(max_length=50)
    color= models.CharField(max_length=20)

    def get_absolute_url(self):
        return reverse('toys_detail', kwargs={'pk': self.id})

    def __str__(self):
        return self.name


class Finch(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    lifespan = models.IntegerField()
    toys = models.ManyToManyField(Toy,blank=True)

    def __str__(self):
        return self.name


class Feeding(models.Model):
    date = models.DateField("feeding date")
    meal = models.CharField(
        max_length=1,
        choices=MEALS,
        default=MEALS[0][0]
    )

    finch = models.ForeignKey(Finch, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_meal_display()} on {self.date}"

    class Meta:
        ordering = ['-date']