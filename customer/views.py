from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http import Http404
from products.models import Product
from .forms import SignupForm
from django.shortcuts import render_to_response
from django.template import RequestContext


# Create your views here.

# HTTP Error 400
# def bad_request(request):
#     print ('hello')
#     # response = render_to_response(
#     #     '400.html',
#     #     context_instance=RequestContext(request)
#     # )
#     #
#     # response.status_code = 400
#     #
#     # return response
#     return render_to_response('customers/400.html', RequestContext(request))


def handler404(request):
    response = render_to_response('customers/404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response


def index(request):
    try:
        product = Product.objects.all()
    except Product.DoesNotExist:
        raise Http404("Product does not exist")

    context = {
        'products': product,
    }
    return render(request, 'home.html', context)


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


