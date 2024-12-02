from django.forms import ModelForm
from django import forms
from .models import GroupMessage, ChatGroup

class ChatmessageCreateForm(ModelForm):
    class Meta:
        model = GroupMessage
        fields = ['body']
        widgets = {
            'body': forms.TextInput(attrs={
                'placeholder': 'Add message ...',
                'class': 'form-control p-3 text-dark',
                'maxlength': '300',
                'autofocus': True
            })
        }

class NewGroupForm(ModelForm):
    class Meta:
        model = ChatGroup
        fields = ['groupchat_name']
        widgets = {
            'groupchat_name': forms.TextInput(attrs = {
                'placeholder':'Add name...',
                'class': 'form-control p-3 text-black',
                'maxlength': '300',
                'autofocus': True,
            }),
        }

class ChatRoomEditForm(ModelForm):
    class Meta:
        model = ChatGroup
        fields = ['groupchat_name']
        widgets={
            'groupchat_name': forms.TextInput(attrs={
                'class':'form-control p-3 mb-3 text-xl font-weight-bold',
                'maxlength': '300',
            }),
        }