from rest_framework.routers import DefaultRouter
from api.user.views.general_views import DepartmentViewSet
from api.user.views.TeacherViewSet import TeacherViewSet
from api.user.views.UserViewSet import UserViewSet

router = DefaultRouter()
router.register('person', UserViewSet, basename="persons")
router.register('teacher', TeacherViewSet, basename='teacher')
router.register('department', DepartmentViewSet, basename="departments")

urlpatterns = router.urls