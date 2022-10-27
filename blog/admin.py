from django.contrib import admin

from .models import Users, Articles, Comments, Response


admin.site.register(Users)
admin.site.register(Articles)
admin.site.register(Comments)
admin.site.register(Response)
