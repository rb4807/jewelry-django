from django.db import models

class Staff(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Staff')
    def __str__(self):
        return self.name

class Working(models.Model):
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Working')
    def __str__(self):
        return self.name + ' - ' + self.department    

class Appointment(models.Model):
    staff = models.ForeignKey(Working, on_delete=models.CASCADE)
    date = models.DateField()
    customer = models.CharField(max_length=100)
    canceled = models.BooleanField(default=False)

