
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import  HeroUser

class CustomHeroAdmin(UserAdmin):
  model = HeroUser
  fieldsets = (
    *UserAdmin.fieldsets, (
      'custom', 
      {
        'fields': (
          'age', 'interests', 'website', 'bio', 'is_coach'
        )
      }
    )
  )


admin.site.register(HeroUser, CustomHeroAdmin)
