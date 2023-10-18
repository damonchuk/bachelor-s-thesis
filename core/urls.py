from django.urls import path

from core.views import IndexView, ContactView, AboutView, PricingView, CarsView, RentView, CarDetailView

app_name = 'core'
urlpatterns = [

    path('', IndexView.as_view(), name='index'),
    path('about', AboutView.as_view(), name='about'),
    path('pricing', PricingView.as_view(), name='pricing'),
    path('cars', CarsView.as_view(), name='cars'),
    path('rent', RentView.as_view(), name='rent'),
    path('contact', ContactView.as_view(), name='contact'),
    path('car_detail/<int:id>/', CarDetailView.as_view(), name='car_detail'),

]

