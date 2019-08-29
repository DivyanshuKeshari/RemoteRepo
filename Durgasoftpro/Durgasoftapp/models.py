from django.db import models
from multiselectfield import MultiSelectField
# Create your models here.
# contact model
# services model
# feedback model
class ServicesData(models.Model):
    course_id=models.IntegerField(primary_key=True)
    course_name=models.CharField(max_length=100,unique=True)
    course_duration=models.CharField(max_length=100)
    course_start_date=models.DateField(max_length=100)
    course_start_time=models.TimeField(max_length=100)
    course_trainer_name=models.CharField(max_length=100)
    course_trainer_exp=models.CharField(max_length=100)

class FeedbackData(models.Model):
    name=models.CharField(max_length=100)
    rating=models.IntegerField()
    date=models.DateField(max_length=100)
    feedback=models.CharField(max_length=500)

class EnquiryData(models.Model):
    name=models.CharField(max_length=100)
    mobile=models.BigIntegerField()
    email=models.EmailField(max_length=100)
    gender=models.CharField(max_length=10)

    COURSES_CHOICES=(
        ('Py','Python'),
        ('Dj','Django'),
        ('Ra','RestApi'),
        ('Fl','Flask'),
        ('UI','UI')
    )
    courses=MultiSelectField(choices=COURSES_CHOICES)

    SHIFTS_CHOICES=(
        ('Morning','Morning Shifts'),
        ('Afternoon','Afternoon Shifts'),
        ('Evening','Evening Shifts'),
        ('Night','Night Shifts')
    )
    shifts=MultiSelectField(choices=SHIFTS_CHOICES)

    start_date=models.DateTimeField(max_length=100)








