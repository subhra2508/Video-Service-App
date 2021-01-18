from django.contrib import admin

from .models import Usermembership,Subscription,Membership
# Register your models here.

admin.site.register(Membership)
admin.site.register(Usermembership)
admin.site.register(Subscription)

