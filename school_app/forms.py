from django import forms
from .models import Departments
from .models import Subjects
from .models import HoursperWeek
from .models import SubjectTopics
from .models import SubjectTeacher


class NewDepartments(forms.ModelForm):
    class Meta:
        model = Departments
        fields = ['text']
        labels = {'text': ''}
        widgets = {
            'text': forms.Textarea(attrs={
                'cols': 80,  # width of the box
                'rows': 10,  # height (number of lines)
                'placeholder': 'Type your thoughts here...',  # optional hint
                'style': 'resize: vertical; border-radius: 8px; padding: 10px;',  # optional styling
            })
        }


class NewSubject(forms.ModelForm):
    class Meta:
        model = Subjects
        fields = ['text']
        labels = {'text': ''}
        widgets = {
            'text': forms.Textarea(attrs={
                'cols': 80,  # width of the box
                'rows': 10,  # height (number of lines)
                'placeholder': 'Type your thoughts here...',  # optional hint
                'style': 'resize: vertical; border-radius: 8px; padding: 10px;',  # optional styling
            })
        }


class NewTopics(forms.ModelForm):
    class Meta:
        model = SubjectTopics
        fields = ['text']
        labels = {'text': ''}
        widgets = {
            'text': forms.Textarea(attrs={
                'cols': 80,  # width of the box
                'rows': 10,  # height (number of lines)
                'placeholder': 'Type your thoughts here...',  # optional hint
                'style': 'resize: vertical; border-radius: 8px; padding: 10px;',  # optional styling
            })
        }


class NewSubjectTeacher(forms.ModelForm):
    class Meta:
        model = SubjectTeacher
        fields = ['text']
        labels = {'text': ''}
        widgets = {
            'text': forms.Textarea(attrs={
                'cols': 80,  # width of the box
                'rows': 10,  # height (number of lines)
                'placeholder': 'Type your thoughts here...',  # optional hint
                'style': 'resize: vertical; border-radius: 8px; padding: 10px;',  # optional styling
            })
        }








