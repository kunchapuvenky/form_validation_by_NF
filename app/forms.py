from django import forms



def check_for_n(value):
    if value[0].lower=='n':
        raise forms.ValidationError('naveen')

def check_for_a(s):
    if s[1]=='a':
        raise forms.ValidationError('venbja')


class studentForm(forms.Form):
    sname=forms.CharField(max_length=50,validators=[check_for_n,check_for_a])
    age=forms.IntegerField()
    email=forms.EmailField()