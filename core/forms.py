from django.forms import ModelForm
from . models import Submission, User, Event

class SubmissionForm(ModelForm):
    class Meta:
        model = Submission
        fields = ['details']