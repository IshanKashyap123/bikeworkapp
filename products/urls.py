from django.urls import path
from . import views
# from django.urls import path
from .views import product_filter_view,load_models

urlpatterns = [
    path('', product_filter_view, name='product_filter'),
    path('ajax/load_models/', load_models, name='ajax_load_models'),

]
