from django import forms
from .models import Topic, Member

class NewTopicForm(forms.ModelForm):
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'row': 5, 'placeholder': 'What is on your mind?'}
        ),
        max_length=4000,
        help_text='The max length of the text is 4000.')

    subject = forms.CharField(
        widget=forms.TextInput (
            attrs={'class': 'form-control'}
        )
        )

    class Meta:
        model = Topic
        fields = ['subject', 'message']


    def clean_subject(self):
        subject = self.cleaned_data['subject']
        if subject=="test":
            raise forms.ValidationError('subjectにtestは使用できません')
            
class MemberModelForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control"
