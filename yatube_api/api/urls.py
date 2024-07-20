from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import SimpleRouter

from api.views import CommentViewSet, GroupViewSet, PostViewSet


router_v1 = SimpleRouter()
router_v1.register('v1/posts', PostViewSet, basename='posts')
router_v1.register('v1/groups', GroupViewSet, basename='groups')
router_v1.register(
    r'v1/posts/(?P<post_id>\d+)/comments',
    CommentViewSet, basename='comments'
)

urlpatterns = [
    path('v1/api-token-auth/', views.obtain_auth_token),
    path('', include(router_v1.urls))
]
