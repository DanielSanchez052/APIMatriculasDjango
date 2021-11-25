from rest_framework.routers import DefaultRouter
from api.course.views.general_views import GradesViewSet, CourseEscolarViewSet, CourseViewSet, StudentCourseViewSet

router = DefaultRouter()
router.register('grades', GradesViewSet, basename="grades")
router.register('course-escolar', CourseEscolarViewSet, basename="course_escolar")
router.register('student-course', StudentCourseViewSet, basename='studentCourse')
router.register('course', CourseViewSet, basename="course")

urlpatterns = router.urls
