from django.urls import path

from .views import *

urlpatterns = [
    path('', MainPageView.as_view(), name='home'),
    path('category/', CatalogView.as_view(), name='catalog'),
    path('category/<str:slug>/', CategoryDetailView.as_view(), name='category'),
    path('product-detail/<int:pk>/', ProductDetail.as_view(), name='detail'),
    # path('add-recipe/', add_recipe, name='add-recipe'),
    # path('update-recipe/<int:pk>/', update_recipe, name='update-recipe'),
    # path('delete-recipe/<int:pk>/', DeleteRecipeView.as_view(), name='delete-recipe'),
]
