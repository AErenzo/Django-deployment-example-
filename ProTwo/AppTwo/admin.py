from django.contrib import admin
from AppTwo.models import Users, ContactMessage, ProjectIdea, UserProfileInfo

# Register your models here.
admin.site.register(Users)
admin.site.register(ContactMessage)
admin.site.register(ProjectIdea)
admin.site.register(UserProfileInfo)