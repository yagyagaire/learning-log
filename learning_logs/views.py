from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Topic, Entry
from .forms import TopicForm, EntryForm

# Create your views here.
def index(request):
    """The homepage for Learning Log."""
    return render(request, 'learning_logs/index.html')

@login_required
def topics(request):
    """Show topics."""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics, 'count': len(topics)}
    return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_id):
    """Show one specific topic and all entries."""
    topic = get_object_or_404(Topic, pk=topic_id, owner=request.user)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

@login_required
def add_topic(request):
    """Add new topic to the database."""
    if request.method != 'POST':
        # No data submitted, show blank form
        form = TopicForm()
    else:
        # POST data submitted; process data.
        form = TopicForm(data=request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.owner = request.user
            topic.save()
            return redirect("learning_logs:topics")
    # Display a blank form or invalid form. 
    context = {'form': form}
    return render(request, 'learning_logs/add_topic.html', context)

@login_required
def entries(request):
    """Show all entries."""
    entries = Entry.objects.filter(topic__owner=request.user).order_by('-date_added')
    context = {'entries': entries, 'count': len(entries)}
    return render(request, 'learning_logs/entries.html', context)

@login_required
def edit_entry(request, entry_id):
    """Edit an entry."""
    entry = get_object_or_404(Entry, pk=entry_id, topic__owner=request.user)
    if request.method != 'POST':
        form = EntryForm(instance=entry, user=request.user)
    else:
        form = EntryForm(instance=entry, data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
        return redirect('learning_logs:entries')
    context = {'form': form, 'entry': entry}
    return render(request, 'learning_logs/edit_entry.html', context)

@login_required
def add_entry(request):
    topic_id = request.GET.get('topic_id')
    if topic_id:
        topic = Topic.objects.filter(owner=request.user, pk=topic_id)
    else:
        topic = None
    if request.method != 'POST':
        form = EntryForm(initial={'topic': topic}, user=request.user)
    else:
        form = EntryForm(data=request.POST, user=request.user)
        if form.is_valid():
            topic_id = Topic.objects.filter(owner=request.user).get(text=form.cleaned_data.get('topic')).id
            form.save()
            return redirect('learning_logs:topic', topic_id = topic_id)

    context = {'form': form, 'topic': topic}
    return render(request, 'learning_logs/add_entry.html', context)

