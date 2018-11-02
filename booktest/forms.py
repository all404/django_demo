from django import forms


# 1.定义表单类
class BookForm(forms.Form):
    title = forms.CharField(label='书名', required=True, max_length=20)
    pub_date = forms.DateField(label='发行日期', required=True)