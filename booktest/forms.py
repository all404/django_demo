from django import forms


# # 1.定义表单类
# class BookForm(forms.Form):
#     title = forms.CharField(label='书名', required=True, max_length=20)
#     pub_date = forms.DateField(label='发行日期', required=True)


from booktest.models import BookInfo
"""如果表单中的数据与模型类对应，可以通过继承forms.ModelForm更快速的创建表单"""
# 定义模型类表单
class BookForm(forms.ModelForm):
    class Meta:
        model = BookInfo  # 指明从属哪个模型
        fields = ('btitle', 'bpub_date')  # 表单中添加模型的哪些字段
