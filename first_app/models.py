from django.db import models

# Create your models here.
class Student(models.Model):
    roll = models.AutoField(primary_key=True)
    Name=models.CharField(max_length=50)
    phone_number = models.BigIntegerField()
    email= models.EmailField()
    address=models.TextField()
    boolean_field = models.BooleanField()
    date_field = models.DateField()
    date_time_field = models.DateTimeField()
    cls_duration = models.DurationField()
    file_uplode = models.FileField(upload_to='files/')
    image= models.ImageField(upload_to='images/')

    def __str__(self):
        return self.Name
    
