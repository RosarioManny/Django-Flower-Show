from django.db import models

SCENTS = [
    ('NONE', 'No Smell'),
    ('SWEET', 'Sweet'),
    ('STRONG', 'Strong'),
    ('EARTHY', 'Earthy')
]
# Create your models here.
class Flowers(models.Model):
    name = models.CharField()
    color = models.CharField()
    scent = models.CharField(
        choices=SCENTS,
        default=SCENTS[0][0],
    )
    
