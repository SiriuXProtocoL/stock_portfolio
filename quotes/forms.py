from django import forms
from .models import stock_db

class StockForm(forms.ModelForm):
    class Meta:
        #the model class name
        model = stock_db
        #the column filed or fields
        fields = ["ticker"]