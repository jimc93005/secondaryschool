from django.contrib import admin
from .models import Departments
from .models import Subjects
from .models import HoursperWeek
from .models import SubjectTopics
from .models import SubjectTeacher


@admin.register(HoursperWeek)
class HoursPerWeekAdmin(admin.ModelAdmin):
    list_display = ('hours_subjects', 'text', 'date_added')  # columns to show
    list_filter = ('date_added', 'hours_subjects')  # add filter sidebar
    search_fields = ('text', 'hours_subjects__text')  # search bar
    ordering = ('-date_added',)  # newest first


@admin.register(Departments)
class SchoolDepartments(admin.ModelAdmin):
    list_display = ('text', 'subject_count', 'date_added')  # columns to show
    list_display_links = ('text',)
    list_filter = ('date_added', 'text')  # add filter sidebar
    search_fields = ('text',) # search bar
    ordering = ('-date_added',)  # newest first

    def subject_count(self, obj):
        return obj.subjects_set.count()

    subject_count.short_description = 'number of subjects'


class SubjectLessons(admin.TabularInline):
    model = SubjectTopics
    extra = 1


@admin.register(Subjects)
class SubjectsAdmin(admin.ModelAdmin):
    list_display = ('text', 'date_added')  # adjust to match your Subjects model fields
    inlines = [SubjectLessons]


@admin.register(SubjectTeacher)
class SubjectTeacherAdmin(admin.ModelAdmin):
    list_display = ('teacher_subject', 'teacher_name', 'date_added')  # columns to show
    list_filter = ('date_added', 'teacher_subject')  # add filter sidebar
    search_fields = ('text', 'teacher_subject__text')  # search bar
    ordering = ('-date_added',)  # newest first

    def teacher_name(self, obj):
        return obj.text
    teacher_name.short_description = 'Teacher Name'



# admin.site.register(Departments)
# admin.site.register(Subjects)
# admin.site.register(Hours_per_Week)
