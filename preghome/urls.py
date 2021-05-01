from django.urls import path
from django.conf.urls import url
from .import views
 

app_name = "preghome"

urlpatterns = [
	path('',views.intro_page, name='home'),
	path('aboutus/',views.aboutus, name='aboutus'),
	path('shop/', views.product_list,name='product_list'),
	path('booknurse/',views.nurse_package,name='booknurse'),
	path('book_final/',views.booknurse,name='book_final'),
	path('nurse_success/',views.book_success,name='nurse_success'),
	path('team/',views.our_team,name='our_team'),
	path('partners/',views.our_partners,name='our_partners'),
	path('<int:id>/<slug:slug>/', views.product_detail, name="detail"),
]