from django.contrib import admin
from polls.models import Choice, Question, Client, Task, RateCard, Rate, Project

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)

# class ClientAdmin(admin.ModelAdmin):
#     fieldsets = [
#         ()
#     ]

admin.site.register(Client)
admin.site.register(Task)
admin.site.register(RateCard)
admin.site.register(Rate)
admin.site.register(Project)