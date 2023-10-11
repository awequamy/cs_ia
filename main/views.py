from django.core.paginator import Paginator
from django.db.models import Q
from django.views.generic import ListView, DetailView

from cart.forms import CartAddProductForm
from main.models import Product, Category


class MainPageView(ListView):
    model = Product
    template_name = 'index.html'
    context_object_name = 'products'
    paginate_by = 4

    def get_template_names(self):
        template_name = super(MainPageView, self).get_template_names()
        search = self.request.GET.get('query')
        if search:
            template_name = 'search.html'
        return template_name

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        search = self.request.GET.get('query')
        if search:
            context['products'] = Product.objects.filter(Q(title__icontains=search))
        else:
            context['products'] = Product.objects.all()
        return context


class CatalogView(ListView):
    model = Product
    template_name = 'catalog.html'
    paginate_by = 6


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'category_view.html'
    context_object_name = 'category'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.slug = kwargs.get('slug', None)
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.filter(category=self.slug)
        return context


class ProductDetail(DetailView):
    model = Product
    template_name = 'product-detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cart_product_form'] = CartAddProductForm
        return context
