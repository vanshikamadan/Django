from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Choice, Question, Name
from .forms import NameForm
from django.shortcuts import render_to_response
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.http import JsonResponse
import json
from django.core.serializers.json import DjangoJSONEncoder


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += selected_choice.votes
	
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            name = Name(Your_name = request.POST["your_name"], Age = request.POST["your_age"], Email = request.POST["your_email"])
            name.save() 
            return HttpResponse("Entry Saved")

            #return render(request, 'polls/name.html', {'form': form})

    # if a GET (or any other method) we'll create a blank form
    else:
         form = NameForm()

    return render(request, 'polls/name.html', {'form': form})

    #info = {"Your_name": "vanshika"}

def more_todo(request):
    if request.is_ajax():
        todo_items = ['Mow Lawn', 'Buy Groceries',]
        data = json.dumps(todo_items)
        return HttpResponse(data, content_type='application/json')
    else:
        raise Http404 

def info(request):
    if request.is_ajax():
        name = Name.objects.values();
        name_list = list(name)
        x = json.dumps(name_list)
        return HttpResponse(x, content_type='application/json')
    else: 
        raise Http404

            
            
    #return render(request, 'polls/name.html', info)
    

