from django.shortcuts import redirect, get_object_or_404
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from user_host.forms import HostForm
from user_host.models import Host


class ViewHost(DetailView):
    model = Host
    context_object_name = 'host_item'


class Home(ListView):
    model = Host
    template_name = 'user_host/home.html'
    context_object_name = 'host'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Host.objects.filter(author=self.request.user)
        else:
            return redirect('login')


def add_host(request):
    if request.method == 'POST':
        form = HostForm(request.POST)
        if form.is_valid():
            response = form.save(commit=False)
            response.author = request.user
            response.save()
            form.author = request.user
            form = form.save()
            return redirect('home')
        else:
            return render(request, 'user_host/add_host.html', {'form': form})
    else:
        form = HostForm()
        return render(request, 'user_host/add_host.html', {'form': form})


def edit_host(request, id):
    host = get_object_or_404(Host, id=id)
    if request.method == 'POST':
        form = HostForm(request.POST, instance=host)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('home')
        return redirect('edit_host', id=host.id)
    else:
        form = HostForm(instance=host)
    return render(request, 'user_host/edit_host.html', {'form': form, 'host': host})
