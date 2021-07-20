from django import forms
 
 
class AddMessageForm(forms.Form):
    text = forms.CharField(
        label='',
        widget=forms.Textarea(
            attrs={
                'placeholder':'Send a message to the world', 
                'rows': 1
            }
        )
    )
