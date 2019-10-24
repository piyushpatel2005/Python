from django import forms
from .models import Comment

class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)

# use forms.ModelForm for Comment
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        # specify which fields should be included in the form. That's it!
        # We can specify which fields to exclude using `exclude` list
        fields = ('name', 'email', 'body')