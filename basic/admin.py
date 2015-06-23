from django.contrib import admin
from .models import Test
from .models import Single_choice
from .models import Multiple_choice
from .models import Choice

admin.site.register(Test)
admin.site.register(Single_choice)
admin.site.register(Multiple_choice)
admin.site.register(Choice)

# Register your models here.
