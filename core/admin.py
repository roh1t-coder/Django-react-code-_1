from django.contrib import admin
from .models import Employee, Idea, Vote, Collaboration, Reward

admin.site.register(Employee)
admin.site.register(Idea)
admin.site.register(Vote)
admin.site.register(Collaboration)
admin.site.register(Reward)