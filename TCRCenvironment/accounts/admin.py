from django.contrib import admin
from accounts.models import UserProfile 

admin.site.site_header = "Admininstration"

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("ID","name","current_project")

    def ID(self,obj):
        return obj.userID
    
    def get_queryset(self,request):
         queryset = super(UserProfileAdmin,self).get_queryset(request)
         queryset = queryset.order_by('name')
         return queryset

admin.site.register(UserProfile,UserProfileAdmin)