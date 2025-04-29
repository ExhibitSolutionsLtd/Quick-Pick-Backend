from django.urls import include, path

urlpatterns = [
    path('auth/', include('qp_app.urls.auth_urls')),
    path('sys/', include('qp_app.urls.sys_urls')),
]
