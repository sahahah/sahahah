from django.contrib import admin
# from .models import *
# # Register your models here.
# admin.site.register(modelname)

from .models import *

admin.site.register(UserEvent)
admin.site.register(Events)
admin.site.register(Tag)
admin.site.register(regEvents)
admin.site.register(partcipateEvents)
admin.site.register(Feedback)