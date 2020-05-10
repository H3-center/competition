from django import forms
from .models import Job, Target_list


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['s_word','media','t_st_date','t_end_date']

        widgets = {
            's_word': forms.TextInput(attrs={'placeholder':'검색할 단어를 입력하세요.'}),
            't_st_date': forms.TextInput(attrs={'placeholder':'1990-01-01'}),
            't_end_date': forms.TextInput(attrs={'placeholder':'1990-01-31'})

        }
    def save(self, commit=True):
        self.instance = Job(**self.cleaned_data)
        if commit:
            self.instance.save()

        return self.instance


class Target_list_Form(forms.ModelForm):
    class Meta:
        model = Target_list
        fields = ['media','crawling_url','input_col']
        widgets = {
            'media': forms.TextInput(attrs={'placeholder':'대상 사이트 이름을 입력하세요.'}),
            'crawling_url': forms.TextInput(attrs={'placeholder':'https://www.대상url.co.kr'}),
            'input_col': forms.TextInput(attrs={'placeholder':'col1,col2,col3(영문으로 입력)'})

        }