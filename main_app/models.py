from django.db import models
from datetime import date
SCENTS = [
    ('No Smell', 'NONE'),
    ('Sweet', 'SWEET'),
    ('Strong', 'STRONG'),
    ('Earthy', 'EARTHY'),
    ('Woody', 'WOODY'),
    ('Fresh', 'FRESH'),
    ('Aromatic', 'AROMA')

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
    
    # def watered_today(self):
    #     return self.watered.filter(date=date.today()).count() == 1
        # unsure if it should be feeding_set or if I can change name to water_set

class Watering(models.Model):
    date = models.DateField('Watering Date')
    amount = models.CharField(
        choices=WATERAMOUNT,
        default=WATERAMOUNT[0][0]
    )

    flowers = models.ForeignKey(Flowers, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.flowers.name} | {self.get_amount_display()} amount of watering on {self.date.month} / {self.date.day}'
    
    class Meta :
        ordering = ['-date']