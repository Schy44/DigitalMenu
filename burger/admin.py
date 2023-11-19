from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Userprofile, Member, MenuItem, ChefSpecial, BurgerMenu

# Register your models here.


class MemberAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname", "joined_date",)


class UserProfileInline(admin.StackedInline):
    model = Userprofile


admin.site.register(Userprofile)
admin.site.register(Member, MemberAdmin)
admin.site.register(MenuItem)
admin.site.register(ChefSpecial)
admin.site.register( BurgerMenu)