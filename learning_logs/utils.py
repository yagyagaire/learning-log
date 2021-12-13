from django.shortcuts import render
from .models import Topic

def load_topics(request):
    topics = Topic.objects.filter(owner=request.user).order_by('-date_added')
    return render(request, 'learning_logs/topics_dropdown_list_options.html', {'topics': topics})


