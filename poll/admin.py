from django.contrib import admin

# Register your models here.
from .models import Question,Question_choice
# choice inline foreignkey use garda 
# where one to many relationship are used
class ChoiceInline(admin.TabularInline):
   model= Question_choice

class QuestionAdmin(admin.ModelAdmin):
   list_display = ['question_text','created_date']
   search_fields = ['question_text','choice_text']
   list_filter =['created_date']
   fields = ['question_text'] # thing to display 
   inlines= [ChoiceInline] # must be inherit from above class while using one to many relation 

# registering this model
admin.site.register(Question,QuestionAdmin)
admin.site.register(Question_choice)