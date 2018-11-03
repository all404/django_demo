from rest_framework import serializers


class BookInfoSerializer(serializers.Serializer):
    id = serializers.IntegerField(label='ID', required=False, read_only=True)
    btitle = serializers.CharField(label='书名', max_length=20)
    bpub_date = serializers.DateField(label='发行日期', allow_null=True)
    bread = serializers.IntegerField(label='阅读量', required=False, default=0)
    bcomment = serializers.IntegerField(label='评论量', required=False, default=0)
    is_delete = serializers.BooleanField(label='逻辑删除', required=False, write_only=True)


"""
通用参数:
required	该字段在反序列化时必须输入，默认True
default	反序列化时使用的默认值
allow_null	表明该字段是否允许传入None，默认False
read_only	表明该字段仅用于序列化输出，默认False
write_only	表明该字段仅用于反序列化输入，默认False
allow_null	表明该字段是否允许传入None，默认False
label	用于HTML展示API页面时，显示的字段名称

validators	该字段使用的验证器
error_messages	包含错误编号与错误信息的字典
help_text	用于HTML展示API页面时，显示的字段帮助提示信息

选项参数
max_length	最大长度
min_lenght	最小长度
allow_blank	是否允许为空
trim_whitespace	是否截断空白字符
max_value	最小值
min_value	最大值
"""