from django.urls import path

from . import views

urlpatterns = [
    path('landing/<str:new_uuid>/', views.landing_page, name='landing_page'),
    path('registerProduct/', views.register_product, name='register_product'),
    path('product/<uuid:product_uuid>/', views.product_detail, name='product_detail'),
    path('create_product/<uuid:uuid>', views.create_product, name='create_product'),
    path('generate_empty_qr_code/', views.generate_empty_qr_code, name='generate_empty_qr_code'),

]
