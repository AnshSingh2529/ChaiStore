from django import forms
from .models import ChaiVariety, PyChaiReview, PyChaiLike, Store 

class PyChaiForm(forms.ModelForm):
   class Meta:
      model = ChaiVariety
      fields = ['name', 'image', 'type', 'description', 'method', 'price']
      
class StoreForm(forms.ModelForm):
   class Meta:
      model = Store
      fields = ['name', 'location', 'chai_varieties', 'Store_image', 'Store_open', 'Store_close']
      

      
   
   
