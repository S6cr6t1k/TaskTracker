from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views import View
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Task, Comment
from .forms import UserRegisterForm, TaskForm
from django.contrib.auth import get_user_model, logout
from django.http import HttpResponseRedirect

def simple_logout(request):
    logout(request)
    return redirect('login')

User = get_user_model()

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})

class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'task_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        queryset = Task.objects.all()
        status = self.request.GET.get('status')
        priority = self.request.GET.get('priority')
        due_date = self.request.GET.get('due_date')
        if status:
            queryset = queryset.filter(status=status)
        if priority:
            queryset = queryset.filter(priority=priority)
        if due_date:
            queryset = queryset.filter(due_date=due_date)
        return queryset

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_form.html'
    success_url = reverse_lazy('task-list')

class TaskUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_form.html'
    success_url = reverse_lazy('task-list')

    def test_func(self):
        return self.request.user.is_authenticated

class TaskDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Task
    template_name = 'task_confirm_delete.html'
    success_url = reverse_lazy('task-list')

    def test_func(self):
        return self.request.user.is_authenticated

class CommentCreateView(LoginRequiredMixin, View):
    def post(self, request, pk):
        task = get_object_or_404(Task, pk=pk)
        text = request.POST.get('text')
        if text:
            Comment.objects.create(task=task, text=text, author=request.user)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


from django.contrib.auth.views import LogoutView

class LogoutViewAllowGet(LogoutView):
    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

def simple_logout(request):
    logout(request)
    return redirect('login')