from django import forms


class StudentForm(forms.Form):
    firstname = forms.CharField(label="Enter first Name", max_length=50)
    lastname = forms.CharField(label="Enter last Name", max_length=50)
    email = forms.CharField(label="Enter email", max_length=30)
    phonenumber=forms.CharField(label="Enter phonenumber", max_length=10)
    gender=forms.CharField(label="Enter gender",max_length=4)
