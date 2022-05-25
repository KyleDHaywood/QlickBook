from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.views.generic.edit import CreateView

from .models import Project, Ticket

# Create your views here.
class DashboardPageView(TemplateView):
    template_name = 'dashboard.html'

class ProjectListView(ListView):
    template_name = 'projects/list.html'
    model = Project

class ProjectDetailView(DetailView):
    template_name = 'projects/detail.html'
    model = Project
    field = ['ticket']    

class ProjectCreateView(LoginRequiredMixin, CreateView):
    template_name = "projects/new.html"
    model = Project
    fields = ['title', 'description']

class TicketCreateView(LoginRequiredMixin, CreateView):
    template_name = "tickets/new.html"
    model = Ticket
    fields = ['title', 'author', 'dateCreated', 'dateResolved', 'difficulty', 'status', 'project', 'commentary']

class TicketListView(ListView):
    template_name = 'tickets/ticket-list.html'
    model = Ticket