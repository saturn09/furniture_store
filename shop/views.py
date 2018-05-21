from django.shortcuts import render

# Create your views here.


from django.views import generic


class IndexView(generic.TemplateView):
    template_name = '../templates/shop/index.html'


class ShopView(generic.TemplateView):
    template_name = '../templates/shop/shop.html'


class FurnitureView(generic.DetailView):
    pass
