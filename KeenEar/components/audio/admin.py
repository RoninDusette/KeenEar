from django.contrib import admin
from .models import Library
from .models import Recording


admin.site.register(Library)
admin.site.register(Recording)
