from rest_framework import serializers

from booktest.models import BookInfo, HeroInfo


class BookInfoSerializer(serializers.Serializer):
    id = serializers.IntegerField(label='ID', required=False, read_only=True)
    btitle = serializers.CharField(label='书名', max_length=20)
    bpub_date = serializers.DateField(label='发行日期', allow_null=True)
    bread = serializers.IntegerField(label='阅读量', required=False, default=0)
    bcomment = serializers.IntegerField(label='评论量', required=False, default=0)


class HeroInfoSerializer(serializers.Serializer):
    GENDER_CHOICES = (
        ('0', 'female'),
        ('1', 'male')
    )
    id = serializers.IntegerField(label='ID', required=False, read_only=True)
    hname = serializers.CharField(label='名称', max_length=20)
    hcomment = serializers.CharField(label='描述信息', required=False, default=0)
    hgender = serializers.ChoiceField(choices=GENDER_CHOICES, label='性别', required=True)


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


# 模型类序列化器
class BookInfoModelSerializer(serializers.ModelSerializer):
    """图书模型类序列化器"""
    class Meta:
        model = BookInfo
        # fields = '__all__'
        # fields = ('id', 'btitle', 'bpub_date')
        exclude = ('image', )
        read_only_fields = ('id', 'bread', 'bcomment')
        write_only_fields = ('is_delete',)
        depth = 1
        extra_kwargs = {
            'bread': {'min_value': 0, 'required': True},
            'bcomment': {'max_value': 0, 'required': True}
        }

    # model 指明参照哪个模型类
    # fields 指明模型类的哪些字段(__all__为所有字段)
    # exclude 明确排除掉哪些字段
    # read_only_fields 指明只读字段
    # depth 生成嵌套表示，depth应该是整数，表明嵌套的层级数量?????
    # extra_kwargs参数为ModelSerializer添加或修改原有的选项参数


class HeroInfoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroInfo
        # fields = '__all__'
        # fields = ('hname', 'hgender', 'hcomment', 'hbook')
        exclude = ('is_delete', )
        read_only_fields = ('id',)
        write_only_fields = ('is_delete',)
        # depth = 1
