from django.urls import path, include, re_path
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from . import views
from django.contrib import admin
from .docs import schema_view


urlpatterns = [
      path('admin/', admin.site.urls),
      path('', views.ok_view),
      path('api/v1/auth/', obtain_jwt_token),
      path('api/v1/refresh-auth/', refresh_jwt_token),
      path('api/v1/proposal/', include('proposal.api.urls')),
]

urlpatterns += [
   re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]

