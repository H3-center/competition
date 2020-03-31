from django import forms
from .models import Job, Target_list


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['s_word','media','t_st_date','t_end_date']
    def save(self, commit=True):
        self.instance = Job(**self.cleaned_data)
        if commit:
            self.instance.save()

        return self.instance


class Target_list_Form(forms.ModelForm):
    class Meta:
        model = Target_list
        fields = ['media','crawling_url','input_col']
