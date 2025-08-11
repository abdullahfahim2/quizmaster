from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, TemplateView
from django.core.paginator import Paginator
from .models import *
from .forms import *

def home(request):
    categories = QuizCategory.objects.all()
    return render(request, 'quiz/home.html', {'categories': categories})

class QuizListView(ListView):
    model = Quiz
    template_name = 'quiz/quiz_list.html'
    context_object_name = 'quizzes'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        category = self.request.GET.get('category')
        difficulty = self.request.GET.get('difficulty')
        
        if category:
            queryset = queryset.filter(category__name=category)
        if difficulty:
            queryset = queryset.filter(difficulty=difficulty)
            
        return queryset

def start_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    
    if request.method == 'POST':
        form = QuizStartForm(request.POST)
        if form.is_valid():
            # Create quiz attempt
            attempt = QuizAttempt.objects.create(
                user_name=form.cleaned_data['user_name'],
                quiz=quiz
            )
            request.session['attempt_id'] = attempt.id
            return redirect('quiz:take_quiz', question_num=1)
    else:
        form = QuizStartForm()
    
    return render(request, 'quiz/start_quiz.html', {
        'quiz': quiz,
        'form': form
    })

def take_quiz(request, question_num):
    attempt_id = request.session.get('attempt_id')
    if not attempt_id:
        return redirect('quiz:home')
    
    attempt = get_object_or_404(QuizAttempt, pk=attempt_id)
    questions = attempt.quiz.questions.all()
    
    # Paginate questions
    paginator = Paginator(questions, 1)
    page_obj = paginator.get_page(question_num)
    question = page_obj.object_list[0]
    
    if request.method == 'POST':
        answer_id = request.POST.get('answer')
        if answer_id:
            answer = get_object_or_404(Answer, pk=answer_id)
            
            # Save user's answer
            UserAnswer.objects.create(
                attempt=attempt,
                question=question,
                answer=answer,
                is_correct=answer.is_correct
            )
            
            # Update score if correct
            if answer.is_correct:
                attempt.score += 1
                attempt.save()
            
            # Check if this was the last question
            if page_obj.has_next():
                return redirect('quiz:take_quiz', question_num=question_num+1)
            else:
                # Quiz completed
                attempt.completed = True
                attempt.save()
                return redirect('quiz:quiz_results', attempt_id=attempt.id)
    
    # Get all answers for the current question
    answers = question.answers.all()
    
    return render(request, 'quiz/take_quiz.html', {
        'quiz': attempt.quiz,
        'question': question,
        'answers': answers,
        'page_obj': page_obj,
        'current_question_num': question_num,
        'total_questions': len(questions)
    })

def quiz_results(request, attempt_id):
    attempt = get_object_or_404(QuizAttempt, pk=attempt_id)
    return render(request, 'quiz/results.html', {'attempt': attempt})