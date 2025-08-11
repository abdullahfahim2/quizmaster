from django.contrib import admin
from .models import QuizCategory, Quiz, Question, Answer, QuizAttempt, UserAnswer

class QuizAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'difficulty', 'created_by', 'created_at')
    list_filter = ('category', 'difficulty')
    search_fields = ('title', 'category__name')
    
    def save_model(self, request, obj, form, change):
        if not obj.pk:  # Only set created_by during the first save
            obj.created_by = request.user
        super().save_model(request, obj, form, change)

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'quiz', 'order')
    list_filter = ('quiz__category', 'quiz__difficulty')
    search_fields = ('text',)
    ordering = ('quiz', 'order')

class AnswerAdmin(admin.ModelAdmin):
    list_display = ('text', 'question', 'is_correct')
    list_filter = ('question__quiz__category', 'question__quiz__difficulty')
    search_fields = ('text', 'question__text')

class QuizAttemptAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'quiz', 'score', 'completed', 'started_at')
    list_filter = ('quiz__category', 'quiz__difficulty', 'completed')
    readonly_fields = ('started_at', 'finished_at')

class UserAnswerAdmin(admin.ModelAdmin):
    list_display = ('question',)
    list_filter = ('question__quiz',)

admin.site.register(QuizCategory)
admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(QuizAttempt, QuizAttemptAdmin)
admin.site.register(UserAnswer, UserAnswerAdmin)