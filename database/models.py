from django.db import models

# Create your models here.
class Cities(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Weather(models.Model):
    id = models.AutoField(primary_key=True)
    city_id = models.ForeignKey(Cities, on_delete=models.CASCADE)
    temp = models.FloatField()
    min_temp = models.FloatField()
    max_temp = models.FloatField()
    humidity = models.FloatField()
    date = models.DateTimeField()



