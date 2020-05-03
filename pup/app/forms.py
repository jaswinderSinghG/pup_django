from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db import models
from .models import *




class UserForm(UserCreationForm):
	first_name = forms.CharField(required=True)
	email=forms.EmailField(required=True)
	#password2 = None       #its for hide password 2
	class Meta:
		model = User
		fields = ("first_name", "email", "username","password1","password2")
		#fields ='__all__'
	def save(self, commit=True):
		user = super(UserForm, self).save(commit=False)
		user.email = self.cleaned_data.get('email')
		user.first_name = self.cleaned_data.get('first_name')
		user.password1 = self.cleaned_data.get('password1')

		if commit:
			user.save()
			return user

class Social_Notice_Form(forms.ModelForm):
	class Meta:
		model = social_notice_data
		fields = '__all__'
		# widgets = {
		# 'public_notice' : forms.Textarea(attrs={
		# 	'rows' : '8',
		# 	'cols' : '60',
		# 	'maxlength' : '500',
		# 	})
		# }


class User_Data_Form(forms.ModelForm):
	class Meta:
		model = user_form
		fields = '__all__'
		widgets = {
		 'Message' : forms.TextInput(attrs={'class' : 'form-control'}
			)
		}



class Run_Activity_Form(forms.ModelForm):
	class Meta:
		model = running_activities
		fields = '__all__'
		widgets = {
		'explanation' : forms.Textarea(attrs={
			'rows' : '2',
			'cols' : '60',
			'maxlength' : '100',
			})
		}


class School_Admission_Form(forms.ModelForm):
	
	class Meta:
		model = School_admission
		fields = ['mentor_name', 'mobile_Number', 'notice']
		widgets = {
		'notice' : forms.Textarea(attrs={
			'rows' : '2',
			'cols' : '60',
			'maxlength' : '100',
			}),
		}

 
class SchoolForm(forms.ModelForm):

	class Meta:
		model = School_Data
		fields = ['name_of_student', 'quote', 'image_of_year']
		widgets = {
		'quote' : forms.Textarea(attrs={
			'rows' : '2',
			'cols' : '60',
			'maxlength' : '100',
			}),
		}
		

class AdminForm(forms.ModelForm):

	class Meta:
		model = Sarpanch_Name_Pic
		fields = '__all__'
		

class BaseHomeForm(forms.ModelForm):

	class Meta:
		model = Home_Page_Pics_Article
		fields = ['home_fixed_image', 'best_article']
		widgets = {
		'best_article' : forms.Textarea(attrs={
			'rows' : '10',
			'cols' : '90',
			'maxlength' : '2000',
			}),
		}


class HomeDynamicPicsForm(forms.ModelForm):

	class Meta:
		model = Home_Dynamic_Pics
		fields = '__all__'


class AdminNamePicForm(forms.ModelForm):

	class Meta:
		model = Admin_Name_Pic
		fields = '__all__'



