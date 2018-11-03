from rest_framework import serializers


class BookInfoSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    btitle = serializers.CharField()
    bpub_date = serializers.DateField()
    bread = serializers.IntegerField()
    bcomment = serializers.IntegerField()