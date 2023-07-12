from django.urls import path, include

from rest_framework.routers import DefaultRouter

from profiles_api import views


router  = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
router.register('profile', views.UserProfileViewset) #don't need to asssign base_name, as this viewset has a queryset

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('', include(router.urls))
]

