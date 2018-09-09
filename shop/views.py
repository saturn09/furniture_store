from django.shortcuts import render
from .models import Cloth

# Create your views here.


from django.views import generic


class IndexView(generic.TemplateView):
    template_name = '../templates/shop/index.html'


class ShopView(generic.ListView):
    template_name = '../templates/shop/shop.html'
    context_object_name = 'clothes'
    model = Cloth


class ShopDetailView(generic.DetailView):
    template_name = '../templates/shop/single.html'
    model = Cloth
    context_object_name = 'cloth'


class ContactsView(generic.View):
    template_name = '../templates/shop/contact.html'

    def get(self, request, *args, **kwargs):
        return render(request, template_name=self.template_name)
