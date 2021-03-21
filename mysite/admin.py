from django.contrib import admin
from .models import Customer

@admin.register(Customer)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'food_type', 'location', 'quanity', 'lifetime', 'bookingstatus')

    def __str__(self):
        return self.food_type
