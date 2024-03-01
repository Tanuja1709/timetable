from django import forms
from django.core.validators import MinLengthValidator, MaxLengthValidator

class CourseForm(forms.Form):
    course_id = forms.CharField(
        validators=[
            MinLengthValidator(limit_value=7, message="Course id is less than 7 characters"),
            MaxLengthValidator(limit_value=7, message="Course id is more than 7 characters"),
        ]
    )
    course_name = forms.CharField( max_length=100 )

class FacultyForm(forms.Form):
    faculty_id = forms.IntegerField()
    faculty_name = forms.CharField()
