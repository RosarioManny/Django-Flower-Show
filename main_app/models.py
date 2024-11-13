from django.db import models

SCENTS = [
    ('NONE', 'No Smell'),
    ('SWEET', 'Sweet'),
    ('STRONG', 'Strong'),
    ('EARTHY', 'Earthy')
]

WATERAMOUNT = [
    ('L', 'Light'),
    ('M', 'Moderate'),
    ('H', 'Heavy'),
]
# Create your models here.
class Flowers(models.Model):
    name = models.CharField()
    color = models.CharField()
    scent = models.CharField(
        choices=SCENTS,
        default=SCENTS[0][0],
    )
    
    def __str__(self) :
        return self.name

class Watering(models.Model):
    date = models.DateField()
    amount = models.CharField(
        choices=WATERAMOUNT,
        default=WATERAMOUNT[0][0]
    )

    flowers = models.ForeignKey(Flowers, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.get_amount_display()} amount of watering on {self.date}'