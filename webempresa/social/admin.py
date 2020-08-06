from django.contrib import admin
from .models import Link

# Register your models here.
class LinkAdmin(admin.ModelAdmin):
    readonly_fields=('Created','Updated')

    #Sobre escribe a readonly_fields
    def get_readonly_fields(self,request,obj=None):
        if request.user.groups.filter(name='Personal').exists():
            return ('Created','Updated','key','name')
            # De esta manera los campos Created y Updated no se mostrarán
            # return ('key','name')
        else:
            return ('Created','Updated')

admin.site.register(Link,LinkAdmin)
