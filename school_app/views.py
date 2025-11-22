from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Departments
from .models import Subjects
from .models import HoursperWeek
from .models import SubjectTopics
from .forms import NewDepartments
from .forms import NewSubject

from .forms import NewTopics
from .models import SubjectTeacher
from .forms import NewSubjectTeacher
from django.http import Http404


# Create your views here.


def index(request):
    return render(request, 'school_app/index.html')


@login_required()
def departments(request):
    departments = Departments.objects.filter(owner= request.user).order_by('-date_added')
    context = {'departments': departments}
    return render(request, 'school_app/departments.html', context)


@login_required()
def subjects(request, department_id):
    department = Departments.objects.get(id=department_id)
    if department.owner != request.user:
        raise Http404
    subjects = department.subjects_set.order_by('-date_added')  # note: subjects_set
    context = {'department': department, 'subjects': subjects}
    return render(request, 'school_app/subjects.html', context)


@login_required()
def hoursperWeek(request, subject_id):
    subject = Subjects.objects.get(id=subject_id)
    if subject.owner != request.user:
        raise Http404
    hours_per_week = subject.hoursperweek_set.order_by("-date_added")
    context = {'subject': subject, 'hours_per_week': hours_per_week}
    return render(request, 'school_app/hours.html', context)


@login_required()
def new_department(request):
    if request.method != 'POST':
        form = NewDepartments()

    else:
        form = NewDepartments(data=request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.owner = request.user
            new_user.save()
            return redirect('school_app:departments')

    context = {'form':form}
    return render(request, 'school_app/new_department.html', context)


@login_required()
def new_subject(request, department_id):
    department = Departments.objects.get(id=department_id)
    if request.method != 'POST':
        form = NewSubject()

    else:
        form = NewSubject(data=request.POST)
        if form.is_valid():
            form_save = form.save(commit=False)
            form_save.department_subjects = department
            form_save.owner = request.user
            form_save.save()

            return redirect('school_app:subjects', department_id=department.id)

    context = {'form': form, 'department': department}
    return render(request, 'school_app/new_subject.html', context)


@login_required()
def topics(request, subject_id):
    subject = Subjects.objects.get(id=subject_id)
    if subject.owner != request.user:
        raise Http404
    topic = subject.topics_subjects.order_by("-date_added")
    department = subject.department_subjects
    context = {'subject': subject, 'topic': topic, 'department': department}
    return render(request, 'school_app/topics.html', context)


@login_required()
def new_topics(request, subject_id):
    subject = Subjects.objects.get(id=subject_id)
    if subject.owner != request.user:
        raise Http404

    if request.method != 'POST':
        form = NewTopics()

    else:
        form = NewTopics(data=request.POST)
        if form.is_valid():
            form_save = form.save(commit=False)
            form_save.topics_subjects = subject
            form_save.save()
            return redirect('school_app:topics', subject_id = subject.id)

    context = {'subject': subject, 'form': form}
    return render(request, 'school_app/new_topics.html', context)


@login_required()
def subject_teacher(request, subject_id):

    subject = get_object_or_404(Subjects, id=subject_id)
    if subject.owner != request.user:
        raise Http404
    teacher = subject.teacher_subject.order_by("date_added")
    department = subject.department_subjects
    context = {'subject': subject, 'teacher': teacher, 'department': department}
    return render(request, 'school_app/subject_teacher.html', context)


@login_required()
def edit_subject(request, subject_id):
    subject = Subjects.objects.get(id=subject_id)
    if subject.owner != request.user:
        raise Http404
    department = subject.department_subjects

    if request.method != 'POST':
        form = NewSubject(instance=subject)
    else:
        form = NewSubject(instance=subject, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('school_app:subjects',department_id = subject.department_subjects.id)

    context = {'form':form, 'subject':subject, 'department': department}
    return render(request, 'school_app/edit_subject.html', context)


def new_teacher(request, subject_id):
    subject = Subjects.objects.get(id=subject_id)

    if request.method != 'POST':
        form = NewSubjectTeacher()
    else:
        form = NewSubjectTeacher(data=request.POST)
        if form.is_valid():
            form_save = form.save(commit=False)
            form_save.teacher_subject = subject
            form_save.save()

            return redirect('school_app:subject_teacher',subject_id = subject.id)

    context ={'form': form, 'subject':subject}
    return render(request, 'school_app/new_teacher.html', context)


@login_required()
def edit_topic(request, topic_id):
    topic = SubjectTopics.objects.get(id=topic_id)
    subject = topic.topics_subjects
    if subject.owner != request.user:
        raise Http404

    if request.method != 'POST':
        form = NewTopics(instance=topic)
    else:
        form = NewTopics(instance=topic, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('school_app:topics', subject_id=subject.id)

    context = {'form':form, 'topic':topic, 'subject':subject}
    return render(request, 'school_app/edit_topic.html', context)
















