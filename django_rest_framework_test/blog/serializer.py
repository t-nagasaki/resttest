'''
serializer for User and Entry
'''
# coding: utf-8

from rest_framework import serializers

from .models import User, Entry


class UserSerializer(serializers.ModelSerializer):
    '''
    User serializer
    '''
    class Meta:
        model = User
        fields = ('id', 'name', 'mail')


class EntrySerializer(serializers.ModelSerializer):
    # author = UserSerializer(read_only=True)
    # author = UserSerializer(many=True)
    # title = serializers.CharField(max_length=128)
    #
    # def create(self, validated_data):
    #    author = User.objects.create(title=validated_data['title'])

    #    for item in validated_data['entries']:

    class Meta:
        model = Entry
        fields = ('title', 'body', 'created_at', 'status', 'author')


class UserEntriesSerializer(serializers.ModelSerializer):
    '''
    User serializer with Entries
    '''
    entries = EntrySerializer(many=True)

    class Meta:
        model = User
        fields = ('id', 'name', 'mail', 'entries')

