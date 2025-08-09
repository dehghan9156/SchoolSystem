import django_filters
from ...models import News,ClassRoom,ClassRoom_Student
from rest_framework import filters


class NewsFilter(django_filters.FilterSet):
    lesson = django_filters.CharFilter(field_name="lesson__name",lookup_expr="icontains")
    # , method=
    classroom = django_filters.CharFilter(field_name="classroom__name",lookup_expr="icontains")
    created_by = django_filters.CharFilter(field_name="created_by__username",lookup_expr="icontains")
    class Meta:
        model = News
        fields = {
            "title":["exact","icontains"],
            "created_date":["exact"]
        }

class NewsFilterBackend(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        if request.user.is_staff:
            return queryset
        else:
            return queryset.filter(created_by=request.user) 
        

class ReviewsNewsFilterBakend(filters.BaseFilterBackend):
    
    def filter_queryset(self, request, queryset, view):
        classroom_ids = ClassRoom_Student.objects.filter(student_id=request.user.id).values_list("classroom_id",flat=True)
        teacher_ids = ClassRoom.objects.filter(pk__in=classroom_ids).values_list("teacher_id",flat=True)
        news = News.objects.filter(created_by__in=teacher_ids,classroom_id__in=classroom_ids)
        return news 




    