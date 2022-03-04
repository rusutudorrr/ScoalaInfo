from django.forms import ModelForm
from .models import Profile


# This is what we use to create our profile for watching movies
class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['uuid']
