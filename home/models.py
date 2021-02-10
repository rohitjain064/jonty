from django.db import models

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=100)
    phone_no=models.IntegerField()
    email=models.EmailField()
    subject=models.CharField(max_length=150,blank=True)
    msg=models.TextField()

    def __str__(self):
        return self.name


class Service(models.Model):
    image=models.ImageField(upload_to='service',blank=True)
    title=models.CharField(max_length=100)
    content=models.TextField()

    def __str__(self):
        return self.title

class Gallery(models.Model):
    title=models.CharField(max_length=100)
    image = models.ImageField(upload_to='certification')

    def __str__(self):
        return self.title

class Appointment(models.Model):
    CHOICES=[('Ajmer','Ajmer')]
    TIME_CHOICES=[('Morning','Morning'),('Evening','Evening')]
    AMOUNT_CHOICES=[('100 Rupees',100)]
    order_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    email=models.EmailField()
    date=models.DateField()
    clinic=models.CharField(choices=CHOICES,max_length=100)
    time=models.CharField(max_length=100,choices=TIME_CHOICES)
    amount=models.CharField(choices=AMOUNT_CHOICES,max_length=100)
    date_time=models.DateTimeField(auto_now_add=True)


