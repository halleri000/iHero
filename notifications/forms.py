from django import forms


class AddMessageForm(forms.Form):
    text = forms.CharField(
        widget=forms.Textarea,
        help_text='Use @ to mention a coach.'
    )
