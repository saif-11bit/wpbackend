from django.contrib import admin
from services.models import (
    Service,
    Location,
    SubService,
    Review,
    Message
)

admin.site.register(Service)
admin.site.register(Location)
admin.site.register(SubService)
admin.site.register(Review)
admin.site.register(Message)