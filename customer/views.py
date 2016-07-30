from django.shortcuts import render

# Create your views here.

def index(request):
    #latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': 'Hello saddi '}
    return render(request, 'customers/signup.html', context)