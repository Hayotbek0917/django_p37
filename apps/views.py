# from django.contrib.auth import logout, login
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib.auth.models import User
# from django.contrib.auth.views import LoginView
# from django.core.mail import send_mail
# from django.db.models import F, Q
# from django.http import HttpResponseRedirect
# from django.shortcuts import redirect, render, get_object_or_404
# from django.urls import reverse_lazy
# from django.views import View
# from django.views.generic import ListView, DetailView, CreateView, TemplateView
#
# from apps.forms import RegisterUserModelForm
# from apps.models import Product, Cart, Category
# from root.settings import EMAIL_HOST_USER
#
#
# def test_list_page(request):
#     context = {}
#
#     return render(request, 'apps/product-grid.html', context)
#
#
# class CategoryMixin:
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(object_list=object_list, **kwargs)
#         context['categories'] = Category.objects.all()
#         return context
#
#
# class ProductListView(CategoryMixin, ListView):
#     queryset = Product.objects.all()
#     template_name = 'apps/product-grid.html'
#     context_object_name = 'products'
#     paginate_by = 1
#
#     def get_queryset(self):
#         qs = super().get_queryset()
#         _search = self.request.GET.get('search')
#         if _search:
#             qs = qs.filter(Q(name__icontains=_search) | Q(description__icontains=_search))
#
#         if _category := self.request.GET.get('category'):
#             qs = qs.filter(category_id=_category)
#         return qs
#
#
# class ProductDetailView(CategoryMixin, DetailView):
#     queryset = Product.objects.all()
#     template_name = 'apps/product-details.html'
#
#
# class CustomLoginView(LoginView):
#     template_name = 'apps/auth/login.html'
#     next_page = reverse_lazy('product_list_page')
#
#
# class CustomLogoutView(View):
#     def get(self, request, *args, **kwargs):
#         logout(request)
#         return redirect('product_list_page')
#
#
#
#
# class RegisterCreateView(CreateView):
#     queryset = User.objects.all()
#     template_name = 'apps/auth/register.html'
#     form_class = RegisterUserModelForm
#     success_url = reverse_lazy('product_list_page')
#
#     def form_invalid(self, form):
#         return super().form_invalid(form)
#
#     def form_valid(self, form):
#         self.object = form.save()
#         subject = "Ro'yhatdan o'tish"
#         message = f"{self.object.first_name }Bizning saytdan ro'yxattan o'tdingiz!"
#         send_mail(subject, message, EMAIL_HOST_USER, [self.object.email])
#         login(self.request, self.object)
#         return HttpResponseRedirect(self.get_success_url())
#
#
# class ShoppingCartListView(CategoryMixin, LoginRequiredMixin, ListView):
#     queryset = Cart.objects.all()
#     template_name = 'apps/shopping-cart.html'
#     context_object_name = 'carts'
#
#     def get_queryset(self):
#         qs = super().get_queryset()
#         return qs.filter(user=self.request.user)
#
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(object_list=object_list, **kwargs)
#         user = self.request.user
#
#         total_price = 0
#         total_count = 0
#         for cart in user.carts.all():
#             total_price += cart.product.current_price * cart.quantity
#             total_count += cart.quantity
#
#         context['total_price'] = total_price
#         context['total_count'] = total_count
#
#         return context
#
#
# class AddCartView(LoginRequiredMixin, View):
#
#     def get(self, request, pk, *args, **kwargs):
#         product = get_object_or_404(Product, pk=pk)
#
#         cart, created = Cart.objects.get_or_create(user=request.user, product=product)
#         if not created:
#             cart.quantity = F('quantity') + 1
#             cart.save()
#
#         return redirect(request.META['HTTP_REFERER'])
#
#
# class RemoveCartView(LoginRequiredMixin, View):
#     def get(self, request, pk, *args, **kwargs):
#         Cart.objects.filter(id=pk).delete()
#         return redirect('shopping_cart_page')




from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.db.models import Q

from .models import Todo
from .forms import TodoForm


class TodoListView(ListView):
    model = Todo
    template_name = "apps/bootdey-list.html"
    context_object_name = "todos"

    def get_queryset(self):
        query = self.request.GET.get("q")
        if query:
            return Todo.objects.filter(title__icontains=query)
        return Todo.objects.all()


class TodoDetailView(DetailView):
    model = Todo
    template_name = "apps/bootdey-details.html"
    context_object_name = "todo"


class TodoUpdateView(UpdateView):
    model = Todo
    form_class = TodoForm
    template_name = "apps/todo_form.html"
    success_url = reverse_lazy("todo_list")


class TodoDeleteView(DeleteView):
    model = Todo
    success_url = reverse_lazy("todo_list")

    def post(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)