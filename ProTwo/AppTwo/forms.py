from django import forms
from django.core import validators
from django.contrib.auth.models import User
from AppTwo.models import Users, ContactMessage, ProjectIdea, UserProfileInfo


#  custom validator - checks that the value passed in begin with the letter a
def name_valid_check(value):
    if value[0].lower() != 'a':
        raise forms.ValidationError('Name must start with an a')


class ProjectsForm(forms.ModelForm):
    class Meta():
        model = ProjectIdea
        fields = '__all__'


# class ProjectIdeaForm(forms.Form):
    # two validators assigned to name - checking for first letter being a (custom) and that min length is greater than 2
    # First_Name = forms.CharField(required=True, validators=[name_valid_check, validators.MinLengthValidator(3)])
    # Last_Name = forms.CharField(required=True, validators=[validators.MinLengthValidator(3)])
    # Email = forms.EmailField(required=True)
    # Verify_Email = forms.EmailField(required=True)
    # Project_Category = forms.CharField(required=True)
    # Project_Name = forms.CharField(required=True)
    # Proj_Description = forms.CharField(widget=forms.Textarea)
    # botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])
    #
    # def clean(self):
    #     cleaned_data = super().clean()
    #     email = cleaned_data['Email']
    #     vmail = cleaned_data['Verify_Email']
    #
    #     if vmail != email:
    #         raise forms.ValidationError('Please ensure both emails match')

    # clean validator function example - built-in validators are more commonly used
    # def clean_botcatcher(self):
    #     botcatcher = self.cleaned_data['botcatcher']
    #     if len(botcatcher) > 0:
    #         raise forms.ValidationError('Gotta Bot')
    #     return botcatcher


class LoginForm(forms.Form):
    Email = forms.EmailField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput())


class RegisterForm(forms.Form):
    fName = forms.CharField(required=True, label='First Name', max_length=20)
    lName = forms.CharField(required=True, label='Last Name', max_length=20)
    email = forms.EmailField(required=True)
    ver_email = forms.EmailField(required=True, label='Verify Email')
    password = forms.CharField(required=True, widget=forms.PasswordInput)
    ver_password = forms.CharField(required=True, widget=forms.PasswordInput, label='Verify Password')

    def clean(self):

        cleaned_data = super().clean()

        email = cleaned_data['email']
        vmail = cleaned_data['ver_email']

        pw = cleaned_data['password']
        v_pw = cleaned_data['ver_password']

        if pw != v_pw and email != vmail:
            raise forms.ValidationError('Error: Please ensure both emails and passwords match!')
        elif email != vmail:
            raise forms.ValidationError('Error: Please make sure that both email match!')
        elif pw != v_pw:
            raise forms.ValidationError('Error: Please make sure both passwords match!')


class ContactForm(forms.ModelForm):
    # first_Name = forms.CharField(required=True, label='First Name')
    # last_Name = forms.CharField(required=True, label='Last Name')
    # Message = forms.CharField(required=True, widget=forms.Textarea, max_length=4000)

    class Meta:
        model = ContactMessage
        fields = '__all__'


class SignUpForm(forms.ModelForm):
    class Meta():
        model = Users
        fields = '__all__'


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    v_pw = forms.CharField(label='Verify Password', widget=forms.PasswordInput())

    def clean(self):
        cleaned_data = super().clean()

        clean_pw = cleaned_data['password']
        clean_vpw = cleaned_data['v_pw']

        if clean_pw != clean_vpw:
            raise forms.ValidationError('Both passwords must match')

    class Meta():
        model = User
        fields = ('username', 'email', 'password', 'v_pw')




class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')
