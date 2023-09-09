from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from .models import Proficiency, PhoneNumber, UserProficiency, BankAccountInformation


class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "password1", "password2", "email")

    # def __init__(self):
    #     super().__init__()
    #     self.fields['username'].widget.attrs.update({'class': 'form-control'})
    #     self.fields['first_name'].widget.attrs.update({'class': 'form-control'})
    #     self.fields['last_name'].widget.attrs.update({'class': 'form-control'})
    #     self.fields['password1'].widget.attrs.update({'class': 'form-control'})
    #     self.fields['password2'].widget.attrs.update({'class': 'form-control'})
    #     self.fields['email'].widget.attrs.update({'class': 'form-control'})

    def save(self, commit=True):
        user = super(SignUpForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class PhoneNumberForm(forms.ModelForm):
    class Meta:
        model = PhoneNumber
        fields = ['phone_number']


class UserProficiencyForm(forms.Form):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(UserProficiencyForm, self).__init__(*args, **kwargs)
        proficiencies = Proficiency.objects.all()
        user_proficiencies = UserProficiency.objects.filter(user=user).values('proficiency')
        u_p = [id for id in user_proficiencies]
        for proficiency in proficiencies:
            proficiency_name = proficiency.name
            proficiency_id = proficiency.id
            if not u_p:
                initial_value = False
            for u_p_id in u_p:
                initial_value = True if proficiency.id == u_p_id['proficiency'] else False
                if initial_value:
                    break
            self.fields[f'proficiency_{proficiency_id}'] = forms.BooleanField(
                required=False, label=proficiency_name, initial=initial_value
            )

class BankAccountForm(forms.ModelForm):
    class Meta:
        model = BankAccountInformation
        fields = ['bank_card', 'shaba_number', 'account_number']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(BankAccountForm, self).__init__(*args, **kwargs)
        bank_account_info = BankAccountInformation.objects.filter(user=user).last()
        card_number =  bank_account_info.bank_card if bank_account_info else ""
        shaba_number = bank_account_info.shaba_number if bank_account_info else ""
        account_number = bank_account_info.account_number if bank_account_info else ""
        self.fields['bank_card'] = forms.CharField(required=True, initial=card_number)
        self.fields['shaba_number'] = forms.CharField(required=False, initial=shaba_number)
        self.fields['account_number'] = forms.CharField(required=False, initial=account_number)