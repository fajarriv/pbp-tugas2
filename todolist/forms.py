from django import forms

class TaskForm(forms.Form):
    title = forms.CharField(label="Judul Task")
    description = forms.CharField(label="Deskripsi Task", widget=forms.Textarea)