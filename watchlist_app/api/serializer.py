from rest_framework import serializers
from .. models import Movie

# def name_len(value):
#     if len(value)<2:
#         raise serializers.ValidationError("name is too short")        



class MovieSerializer(serializers.ModelSerializer):
    len_name = serializers.SerializerMethodField()
    len_desc = serializers.SerializerMethodField()
    diff_len  = serializers.SerializerMethodField()
    class Meta:
        model=Movie
        fields='__all__'

    def get_len_name(self,object):
        length = len(object.name)
        return length

    def get_len_desc(self,object):
        length_desc = len(object.description)
        return length_desc
    
    def get_diff_len(self,object):
        length2 = len(object.description)
        length1 = len(object.name)
        diff = (length2-length1)
        return diff

    #field level validation
    def validate_name(self, value):
        if len(value) < 2:
            raise serializers.ValidationError("name is too short")
        # {"mgs":"name is too short"}
        else:
            return value

    ## object level validation
    def validate(self, data):
        if data['name'] == data['description']:
            raise serializers.ValidationError("name and description should not be same")
        return data
