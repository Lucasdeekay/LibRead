import os

from django import forms

from DU_E_Library import settings


class LoginForm(forms.Form):
    user_id = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter Matric No/Staff No',
                'required': '',
                'class': 'input',
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Enter Password',
                'required': '',
                'class': 'input',
            }
        )
    )

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        user_id = cleaned_data.get('user_id')
        password = cleaned_data.get('password')
        if not user_id or not password:
            raise forms.ValidationError("Field cannot be empty")


class RegistrationForm(forms.Form):
    last_name = forms.CharField(
        max_length=50,
        help_text="Characters must be between 2-50",
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter Last Name/Surname',
                'required': '',
                'class': 'input',
            }
        )
    )
    first_name = forms.CharField(
        max_length=50,
        help_text="Characters must be between 2-50",
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter First Name',
                'required': '',
                'class': 'input',
            }
        )
    )
    user_id = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter Matric No/Staff No',
                'required': '',
                'class': 'input',
            }
        )
    )
    sex = forms.CharField(
        max_length=10,
        widget=forms.Select(
            choices=[('', 'Select Sex...'), ('Male', 'Male'), ('Female', 'Female')],
            attrs={
                'required': '',
                'class': 'input',
            }
        )
    )
    phone_number = forms.CharField(
        max_length=20,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter Phone Number',
                'required': '',
                'class': 'input',
            }
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'Enter Email',
                'required': '',
                'class': 'input',
            }
        )
    )
    role = forms.CharField(
        max_length=10,
        widget=forms.Select(
            choices=[('', 'Select Role...'), ('Student', 'Student'), ('Staff', 'Staff'), ('Admin', 'Admin')],
            attrs={
                'required': '',
                'class': 'input',
            }
        )
    )

    def clean(self):
        cleaned_data = super(RegistrationForm, self).clean()
        last_name = cleaned_data.get('last_name')
        first_name = cleaned_data.get('first_name')
        user_id = cleaned_data.get('user_id')
        sex = cleaned_data.get('sex')
        phone_number = cleaned_data.get('phone_number')
        email = cleaned_data.get('email')
        role = cleaned_data.get('role')
        if not last_name or not first_name or not user_id or not sex or not phone_number or not email or not role:
            raise forms.ValidationError("Field cannot be empty")
        elif len(last_name) < 2 or len(last_name) > 50:
            raise forms.ValidationError("Last Name must be between 2-50")
        elif len(first_name) < 2 or len(first_name) > 50:
            raise forms.ValidationError("First Name must be between 2-50")


class ForgotPasswordForm(forms.Form):
    user_id = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter Matric No/Staff No',
                'required': '',
                'class': 'input',
            }
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'Enter Email',
                'required': '',
                'class': 'input',
            }
        )
    )

    def clean(self):
        cleaned_data = super(ForgotPasswordForm, self).clean()
        user_id = cleaned_data.get('user_id')
        email = cleaned_data.get('email')
        if not user_id or not email:
            raise forms.ValidationError("Field cannot be empty")


class PasswordRetrievalForm(forms.Form):
    password = forms.CharField(
        max_length=12,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Enter Password',
                'required': '',
                'class': 'input',
            }
        )
    )

    def clean(self):
        cleaned_data = super(PasswordRetrievalForm, self).clean()
        password = cleaned_data.get('password')
        if not password:
            raise forms.ValidationError("Field cannot be empty")


class UpdatePasswordForm(forms.Form):
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Enter Password',
                'required': '',
                'class': 'input',
            }
        )
    )
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Enter Password',
                'required': '',
                'class': 'input',
            }
        )
    )

    def clean(self):
        cleaned_data = super(UpdatePasswordForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if not password or not confirm_password:
            raise forms.ValidationError("Field cannot be empty")


class UpdateImageForm(forms.Form):
    image = forms.ImageField(
        help_text="Image must not be more than 10mb",
        widget=forms.FileInput(
            attrs={
                'required': '',
                'class': 'input',
            }
        )
    )

    def clean(self):
        cleaned_data = super(UpdateImageForm, self).clean()
        image = cleaned_data.get('image')

        if not image:
            raise forms.ValidationError("Field cannot be empty")


class EbookForm(forms.Form):
    title = forms.CharField(
        max_length=250,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter title',
                'required': '',
                'class': 'input',
            }
        )
    )
    authors = forms.CharField(
        max_length=200,
        help_text='Name of authors should be separated with a comma',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter authors',
                'required': '',
                'class': 'input',
            }
        )
    )
    description = forms.CharField(
        max_length=250,
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Enter description',
                'required': '',
                'class': 'textarea is-info',
            }
        )
    )
    programme = forms.CharField(
        max_length=250,
        widget=forms.Select(
            choices=[
                ('Computer Science', 'Computer Science'),
                ('Software Engineering', 'Software Engineering'),
                ('Cyber Security', 'Cyber Security'),
                ('Biochemistry', 'Biochemistry'),
                ('Industrial Chemistry', 'Industrial Chemistry'),
                ('Business Administration', 'Business Administration'),
                ('Mass Communication', 'Mass Communication'),
                ('Criminology', 'Criminology'),
                ('Microbiology', 'Microbiology'),
                ('Economics', 'Economics'),
                ('Accounting', 'Accounting'),
            ],
            attrs={
                'required': '',
                'class': 'input',
            }
        )
    )
    file = forms.FileField(
        max_length=250,
        help_text="File must not be more than 50mb",
        widget=forms.FileInput(
            attrs={
                'required': '',
                'class': 'input',
            }
        )
    )

    def clean(self):
        cleaned_data = super(EbookForm, self).clean()
        title = cleaned_data.get('title')
        authors = cleaned_data.get('authors')
        description = cleaned_data.get('description')
        programme = cleaned_data.get('programme')
        file = cleaned_data.get('file')
        if not title or not authors or not description or not programme or not file:
            raise forms.ValidationError("Field cannot be empty")
        elif not file.name.endswith('.pdf'):
            raise forms.ValidationError("File must be a pdf")


class JournalForm(forms.Form):
    title = forms.CharField(
        max_length=250,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter title',
                'required': '',
                'class': 'input',
            }
        )
    )
    authors = forms.CharField(
        max_length=200,
        help_text='Name of authors should be separated with a comma',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter authors',
                'required': '',
                'class': 'input',
            }
        )
    )
    description = forms.CharField(
        max_length=250,
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Enter description',
                'required': '',
                'class': 'textarea is-info',
            }
        )
    )
    programme = forms.CharField(
        max_length=250,
        widget=forms.Select(
            choices=[
                ('Computer Science', 'Computer Science'),
                ('Software Engineering', 'Software Engineering'),
                ('Cyber Security', 'Cyber Security'),
                ('Biochemistry', 'Biochemistry'),
                ('Industrial Chemistry', 'Industrial Chemistry'),
                ('Business Administration', 'Business Administration'),
                ('Mass Communication', 'Mass Communication'),
                ('Criminology', 'Criminology'),
                ('Microbiology', 'Microbiology'),
                ('Economics', 'Economics'),
                ('Accounting', 'Accounting'),
            ],
            attrs={
                'required': '',
                'class': 'input',
            }
        )
    )
    file = forms.FileField(
        max_length=250,
        help_text="File must not be more than 50mb",
        widget=forms.FileInput(
            attrs={
                'required': '',
                'class': 'input',
            }
        )
    )

    def clean(self):
        cleaned_data = super(JournalForm, self).clean()
        title = cleaned_data.get('title')
        authors = cleaned_data.get('authors')
        description = cleaned_data.get('description')
        programme = cleaned_data.get('programme')
        file = cleaned_data.get('file')
        if not title or not authors or not description or not file:
            raise forms.ValidationError("Field cannot be empty")
        elif not file.name.endswith('.pdf'):
            raise forms.ValidationError("File must be a pdf")


class BlogForm(forms.Form):
    title = forms.CharField(
        max_length=250,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter title',
                'required': '',
                'class': 'input',
            }
        )
    )
    article = forms.CharField(
        max_length=1000,
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Enter article',
                'required': '',
                'class': 'textarea is-info',
            }
        )
    )
    image = forms.ImageField(
        max_length=250,
        help_text="Image must not be more than 10mb",
        widget=forms.FileInput(
            attrs={
                'required': '',
                'class': 'input',
            }
        )
    )

    def clean(self):
        cleaned_data = super(BlogForm, self).clean()
        title = cleaned_data.get('title')
        article = cleaned_data.get('article')
        image = cleaned_data.get('image')
        if not title or not article or not image:
            raise forms.ValidationError("Field cannot be empty")
