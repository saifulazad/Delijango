from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import SignupForm
# Create your views here.


def index(request):
    return render(request, 'home.html', None)


def signup(request):
    if request.POST:
        form = SignupForm(request.POST)
        
        if form.is_valid():
            form.save()
            url = reverse('index')
            return HttpResponseRedirect(url)

    else:
        form = SignupForm()
    return render(request, 'customers/signup.html', {
        'form': form,
    })


def login(request):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': 'Hello saddi '}
    return render(request, 'login.html', context)


def single_product(request):
    return render(request, 'single_product.html', context=None)