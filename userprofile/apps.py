from django.apps import AppConfig


class UserprofileConfig(AppConfig):
    name = 'userprofile'
    
    def ready(self):
        from userprofile import signals