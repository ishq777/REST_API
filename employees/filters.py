import django_filters
from .models import Employee


class EmployeeFilter(django_filters.FilterSet):

    designation = django_filters.CharFilter(field_name='designation', lookup_expr='icontains')
    emp_name = django_filters.CharFilter(field_name='emp_name', lookup_expr='icontains')
    emp_id =django_filters.RangeFilter(field_name='emp_id')

    class Meta:
        model = Employee
        fields = ['emp_id', 'emp_name','designation']

    