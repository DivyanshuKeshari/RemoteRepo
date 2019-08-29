from django import forms
from .models import FeedbackData,EnquiryData
from multiselectfield import MultiSelectFormField

class FeedbackForm(forms.Form):

    name=forms.CharField(
        label="Enter Your Name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter Your Name'
            }
        )
    )

    rating=forms.IntegerField(
        label="Enter Your Rating",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter Rating'
            }
        )
    )

    feedback=forms.CharField(
        label="Enter Your Feedback",
        widget=forms.Textarea(
            attrs={
                'class':'forms-control',
                'placeholder':'Enter Your feedback'
            }
        )
    )

class EnquiryForm(forms.Form):
    name=forms.CharField(
        label="Enter Your name",
        widget=forms.TextInput(
            attrs={
            'class' : 'form-control',
            'placeholder' :'Enter your name'
        }
        )
    )

    email=forms.CharField(
        label="Enter your Email",
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter your email'
            }
        )
    )

    mobile=forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter your mobile no'
            }
        )
    )

    GENDER_CHOICES=(
        ('F','Female'),
        ('M','Male')
    )
    gender=forms.ChoiceField(
        label='Select gender',
        widget=forms.RadioSelect,choices=GENDER_CHOICES
    )

    COURSES_CHOICES = (
        ('Py', 'Python'),
        ('Dj', 'Django'),
        ('Ra', 'RestApi'),
        ('Fl', 'Flask'),
        ('UI', 'UI')
    )
    courses=MultiSelectFormField(choices=COURSES_CHOICES)

    SHIFTS_CHOICES = (
        ('Morning', 'Morning Shifts'),
        ('Afternoon', 'Afternoon Shifts'),
        ('Evening', 'Evening Shifts'),
        ('Night', 'Night Shifts')
    )
    shifts=MultiSelectFormField(choices=SHIFTS_CHOICES)

    start_date=forms.DateTimeField(
        label='Select Date and Time',
        widget=forms.SelectDateWidget()
    )