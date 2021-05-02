from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class NewuserForm(UserCreationForm):

    class Meta:
        model=User
        fields=("username","password1","password2")

        def save(self,commit=True):
            user =super(NewuserForm,self).save(commit=False)
            user.password=self.cleaned_data['password']
            if commit:
                user.save()

            return user