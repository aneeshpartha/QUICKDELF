from django.contrib import admin

# Register your models here.


from mainapp.models import UserProfile,hotels,items,cardvalidation


# Registering models to view in admin portal

admin.site.register(UserProfile)
admin.site.register(hotels)
admin.site.register(items)
admin.site.register(cardvalidation)