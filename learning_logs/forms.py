from django import forms

from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['text']
        labels = {'text': ''}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text', 'topic']
        labels = {'text': '', 'topic': 'Choose a Topic:'}
        widgets = {'text': forms.Textarea(attrs={'col': 80})}

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        self.fields['topic'].queryset = Topic.objects.filter(owner=self.user)