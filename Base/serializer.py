from rest_framework import serializers
from .models import Center,TicketTech,TicketCenter,FeedBack

class get_centers(serializers.ModelSerializer):
    class Meta:
        model = Center
        fields = ['id','name']

class TechPost(serializers.ModelSerializer):
    class Meta:
        model = TicketTech
        fields = ['id','Title','Description','first_name','last_name','phone_number','address']

class CenterTicketPost(serializers.ModelSerializer):
    center = serializers.CharField(write_only=True)
    class Meta:
        model = TicketCenter
        fields = ['Title','Description','center']

class Get_Ticket_center(serializers.ModelSerializer):
    class Meta:
        model = TicketCenter
        fields = ['id','Title','Description','Center','place']


class Post_FeedBack(serializers.ModelSerializer):
    class Meta:
        model = FeedBack
        fields = ['Title','Description','center']

class Get_Feedback(serializers.ModelSerializer):
    class Meta:
        model = FeedBack
        fields = ['id','Title','Description','center']