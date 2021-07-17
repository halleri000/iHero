from django import forms


class AddMessageForm(forms.Form):
    text = forms.CharField(
        widget=forms.Textarea
    )
