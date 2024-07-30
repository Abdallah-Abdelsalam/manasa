from django.contrib import admin
from .models import *

class what_you_learn_TabularInline(admin.TabularInline):
    model = What_you_learn

class Requirments_TabularInline(admin.TabularInline):
    model = Requirments

class Video_TabularInline(admin.TabularInline):
    model = Video

class course_admin(admin.ModelAdmin):
    inlines = [what_you_learn_TabularInline,Requirments_TabularInline,Video_TabularInline]

admin.site.register(Author)
admin.site.register(Categories)
admin.site.register(Course,course_admin)
admin.site.register(What_you_learn)
admin.site.register(Requirments)
admin.site.register(Lesson)