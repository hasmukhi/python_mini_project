from django import forms
from .models import Topic

class NewTopicForm(forms.ModelForm):
    subject = forms.CharField(
        widget=forms.TextInput(),
    )
    message = forms.CharField(
        widget=forms.Textarea(),
        max_length=4000,
        help_text='The max length of the text is 4000.'
    )

    class Meta:
        model = Topic
        fields = ['subject', 'message']