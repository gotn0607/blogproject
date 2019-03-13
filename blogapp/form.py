from django import forms
from .models import Blog

# 모델을 기반으로 한 입력공간 -> .ModelForm/ 
#                              여기선 Blog객체를 기반으로 만들거임
class BlogPost(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'body']

# 임의의 입력공간 -> .Form
# class BlogPost(forms.Form):
#     email = forms.EmailField()
#     files = forms.FileField()
#     url = forms.URLField()
#     words = forms.CharField(max_length=200)
#     max_number = forms.ChoiceField(choices=[('1','one'),('2','two'),('3','three')])