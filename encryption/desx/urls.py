from django.urls import path

from .views import encrypt, decrypt

urlpatterns = [
	# URLs for projects
	path('encrypt', encrypt, name="encrypt"),
	path('decrypt', decrypt, name="decrypt"),
	# path('decrypt', Decrypt.as_view(), name="decrypt"),

]