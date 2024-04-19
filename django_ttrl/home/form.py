from django.forms import ModelForm
from .models import Departments

class depform(ModelForm):
    class meta:
        model=Departments
        fields='__all__'