from django import forms
from .models import ChaiVariety, PyChaiReview, PyChaiLike, Store 
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User

class PyChaiForm(forms.ModelForm):
   class Meta:
      model = ChaiVariety
      fields = ['name', 'image', 'type', 'description', 'method', 'price']
      
class StoreForm(forms.ModelForm):
   class Meta:
      model = Store
      fields = ['name', 'location', 'chai_varieties', 'Store_image', 'Store_open', 'Store_close']
      

class UserRegistrationForm(UserCreationForm):
   email = forms.EmailField()
   class Meta:
      model = User
      fields = ('username', 'email', 'password1', 'password2')
   
   
