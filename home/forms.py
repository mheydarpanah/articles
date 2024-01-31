from django import forms
from home.models import Todo


class register(forms.Form):
    first_name = forms.Field()
    last_name = forms.Field()
    username = forms.Field()
    password = forms.Field()






class TodoUpdateForm(forms.Form):
    class Meta:
        model=Todo
        fields=('first_name','last_name','username','password','country','province','city')


