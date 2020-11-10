from django import forms
from .models import Employee


# create a ModelForm
class AddEmployee(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Employee
        fields = "__all__"
