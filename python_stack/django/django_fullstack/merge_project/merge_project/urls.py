from django.urls import path, include

urlpatterns = [
    path('', include('course_app.urls')),
    path('login/', include('login_app.urls'))
]
