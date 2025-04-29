from django.urls import path
from qp_app.views import logout, register
from qp_app.views.cookiesAuth import CustomTokenObtainPairView, CustomRefreshToken, is_Authenticated

urlpatterns = [
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', CustomRefreshToken.as_view(), name='token_refresh'),
    path('logout/', logout),
    path('authentication/', is_Authenticated),
    path('register/', register),
]
