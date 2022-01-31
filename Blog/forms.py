from django import forms


class CommentForm(forms.Form):
    comment = forms.CharField(
        max_length=1000,
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Comment here...',
                'required': '',
                'class': 'textarea is-info',
            }
        )
    )

    def clean(self):
        cleaned_data = super(CommentForm, self).clean()
        comment = cleaned_data.get('comment')
        if not comment:
            raise forms.ValidationError("Field cannot be empty")