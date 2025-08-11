from django.urls import path
from .views import *

app_name = 'quiz'

urlpatterns = [
    path('', home, name='home'),
    path('quizzes/', QuizListView.as_view(), name='quiz_list'),
    path('start/<int:quiz_id>/', start_quiz, name='start_quiz'),
    path('take/<int:question_num>/', take_quiz, name='take_quiz'),
    path('results/<int:attempt_id>/', quiz_results, name='quiz_results'),
]