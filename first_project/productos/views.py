from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product

# Create your views here.
class ProductView(ListView):
    """
    Vista para mostrar los productos.
    """
    template_name = 'index.html'
    queryset = Product.objects.all().order_by('-id')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['productos'] = context['product_list']
        return context


class ProductDetailView(DetailView):
    """
    Vista para mostrar el detalle de un producto.
    """
    model = Product
    template_name = 'products/detalle_producto.html'
    queryset = Product.objects.all()


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # print(context)
        return context
