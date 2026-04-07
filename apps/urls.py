# # from django.contrib.auth.views import LoginView, LogoutView
# # from django.urls import path
# #
# # from apps.views import ProductListView, ProductDetailView, CustomLoginView, CustomLogoutView, RegisterCreateView, \
# #     AddCartView, ShoppingCartListView, CheckoutCartView, RemoveCartView
# #
# # urlpatterns = [
# #     path('', ProductListView.as_view(), name='product_list_page'),
# #     path('product-detail/<int:pk>', ProductDetailView.as_view(), name='product_detail_page'),
# #     path('login', CustomLoginView.as_view(), name='login_page'),
# #     path('logout', CustomLogoutView.as_view(), name='logout_page'),
# #     path('register', RegisterCreateView.as_view(), name='register_page'),
# #     path('shopping-cart', ShoppingCartListView.as_view(), name='shopping_cart_page'),
# #     path('products/add-cart/<int:pk>', AddCartView.as_view(), name='add_cart_page'),
# #     path('checkout_page', CheckoutCartView.as_view(), name='checkout_page'),
# #     path('remove_page', RemoveCartView.as_view(), name='remove_page'),
# # ]
#
#
# from django.urls import path
#
# from apps.views import ProductListView, ProductDetailView, CustomLoginView, CustomLogoutView, RegisterCreateView, \
#     ShoppingCartListView, AddCartView, test_list_page, RemoveCartView
#
# urlpatterns = [
#     path('', ProductListView.as_view(), name='product_list_page'),
#     path('product-detail/<int:pk>', ProductDetailView.as_view(), name='product_detail_page'),
#
#     path('shopping-cart', ShoppingCartListView.as_view(), name='shopping_cart_page'),
#     path('products/add-cart/<int:pk>', AddCartView.as_view(), name='add_cart_page'),
#     path('products/remove-cart/<int:pk>', RemoveCartView.as_view(), name='remove_cart_page'),
#     path('login', CustomLoginView.as_view(), name='login_page'),
#     path('register', RegisterCreateView.as_view(), name='register_page'),
#     path('logout', CustomLogoutView.as_view(), name='logout_page'),
# ]


from django.urls import path
from .views import (
    TodoListView,
    TodoDetailView,
    TodoUpdateView,
    TodoDeleteView
)

urlpatterns = [
    path("", TodoListView.as_view(), name="todo_list"),
    path("todo/<int:pk>/", TodoDetailView.as_view(), name="todo_detail"),
    path("todo/<int:pk>/update/", TodoUpdateView.as_view(), name="todo_update"),
    path("todo/<int:pk>/delete/", TodoDeleteView.as_view(), name="todo_delete"),
]
