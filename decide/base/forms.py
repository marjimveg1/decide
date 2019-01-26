# -*- encoding: utf-8 -*-
from clothesLookApp.models import Clothing, Look,Comment
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone



User = get_user_model()


class UserCreateForm(UserCreationForm):
    SEX_OPTIONS = (
        ('M', ('Man')),
        ('W', ('Woman')),
    )
    formato =("Format: dd/mm/YYYY"),

    first_name = forms.CharField(label=('First name'), required=False)
    last_name = forms.CharField(label=('Last name'), required=False)
    year_birth = forms.DateTimeField(label=('Year Birth'), input_formats=['%d/%m/%Y'], help_text=formato, required=False)
    sex = forms.ChoiceField(label=('Sex'), choices=SEX_OPTIONS, required=False)
    nickName = forms.CharField(label=('Nick Name'), max_length=50,required=True)

    class Meta:
        model = User
        fields = ("first_name", "last_name", "year_birth", "sex","nickName", "password1", "password2")

    def save(self):
        user = super(UserCreateForm, self).save(commit=False)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.nickName = self.cleaned_data["nickName"]
        user.year_birth = self.cleaned_data["year_birth"]
        user.sex = self.cleaned_data["sex"]
        user.save()
        return user


    def clean(self, *args, **kwargs):
        cleaned_data = super(UserCreateForm, self).clean(*args, **kwargs)
        nickName = cleaned_data.get('nickName', None)
        #Recorremos todos los usuarios para ver si ya existe
        if nickName is not None:
            users = User.objects.all()
            for u in users:
                if nickName == u.nickName:
                    self.add_error('nickName',('Nick Name alredy exits'))
                    break

        year_birth = cleaned_data.get('year_birth', None)
        # Comprobamos que la fecha de nacimiento sea en pasado
        if year_birth is not None:
            now = timezone.now()
            if year_birth > now:
                self.add_error('year_birth',('Can´t be in future'))


class UserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('nickName','first_name','last_name','sex','year_birth')

    def clean_password(self):
        return self.initial["password"]

#PARA EL MÉTODO CREATESUPERUSER
class UserCreateFormAdmin(UserCreationForm):
    SEX_OPTIONS = (
        ('M', ('Man')),
        ('W', ('Woman')),
    )
    formato =("Format: dd/mm/YYYY"),

    first_name = forms.CharField(label=('First name'), required=False)
    last_name = forms.CharField(label=('Last name'), required=False)
    nickName = forms.EmailField(label=('Nick Name'), required=True)
    year_birth = forms.DateTimeField(label=('Year of Birth'), input_formats=['%d/%m/%Y'], help_text=formato,required=False)
    sex = forms.ChoiceField(label=('Sex'), choices=SEX_OPTIONS, required=False)

    class Meta:
        model = User
        fields = ("first_name", "last_name", "nickName", "year_birth", "sex", "password1", "password2")

    def save(self):
        user = super(UserCreateFormAdmin, self).save(commit=False)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.nickName = self.cleaned_data["nickName"]
        user.year_birth = self.cleaned_data["year_birth"]
        user.sex = self.cleaned_data["sex"]
        user.save()
        return user


    def clean(self, *args, **kwargs):
        cleaned_data = super(UserCreateFormAdmin, self).clean(*args, **kwargs)
        nickName = cleaned_data.get('nickName', None)
        #Recorremos todos los usuarios para ver si ya existe
        if nickName is not None:
            all_users = User.objects.all()
            for u in all_users:
                if nickName == u.nickName:
                    self.add_error('nickName', ('Nickname exits'))
                    break

        year_birth = cleaned_data.get('year_birth', None)
        #Comprobamos que la fecha de nacimiento sea en pasado
        if year_birth is not None:
            now = timezone.now()
            if year_birth > now:
                self.add_error('year_birth', ('Can´t be in future'))


class ClothingForm(forms.ModelForm):
    class Meta:
        model = Clothing
        exclude = {'user',}
        fields = ['name','photo','size','brand', 'link','category',]

        labels = {
            'name': 'Name',
            'photo': 'Photo',
            'size': 'Size',
            'brand': 'Brand',
            'link': 'Link',
            'category': 'Category',
        }

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'photo': forms.TextInput(attrs={'class':'form-control'}),
            'size': forms.TextInput(attrs={'class':'form-control'}),
            'brand': forms.TextInput(attrs={'class':'form-control'}),
            'link': forms.TextInput(attrs={'class':'form-control'}),
            'category': forms.Select(attrs={'class':'form-control'}),
            }
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = {'user','look','moment',}
        fields = ['subject','body',]

        labels = {
            'subject': 'Subject',
            'body': 'Body',
            'moment': 'Moment',
        }

        widgets = {
            'subject': forms.TextInput(attrs={'class':'form-control'}),
            'body': forms.TextInput(attrs={'class':'form-control'}),
            }
        
class createLook(forms.ModelForm):
    class Meta:
        model = Look
        exclude= ('user',)
        fields = [
            'title',
            'description',
            'season',
            'clothes',
        ]

        labels = {
            'title': 'Title',
            'description': 'Description',
            'season': 'Season',
            'clothes': 'Clothes',
        }

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'description': forms.TextInput(attrs={'class':'form-control'}),
            'season': forms.Select(attrs={'class':'form-control'}),
            'clothes': forms.SelectMultiple(attrs={'class':'form-control'}),
            }
        

