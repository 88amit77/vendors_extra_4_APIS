from django.urls import path
from rest_framework_swagger.views import get_swagger_view

# TODO: add here your API URLs

schema_view = get_swagger_view(title='Micromerce API')


urlpatterns = [
	path("products/docs/", schema_view),
]
