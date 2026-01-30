from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from .models import Student
from .forms import StudentForm

@login_required
def student_list(request):
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})

@login_required
def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'students/student_detail.html', {'student': student})

@login_required
def student_create(request):
    if not request.user.has_perm('students.add_student'):
        raise PermissionDenied

    form = StudentForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('student_list')

    return render(request, 'students/student_form.html', {
        'form': form,
        'title': 'Add Student'
    })

@login_required
def student_update(request, pk):
    if not request.user.has_perm('students.change_student'):
        raise PermissionDenied

    student = get_object_or_404(Student, pk=pk)
    form = StudentForm(request.POST or None, instance=student)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('student_list')

    return render(request, 'students/student_form.html', {
        'form': form,
        'title': 'Edit Student'
    })

@login_required
def student_delete(request, pk):
    if not request.user.has_perm('students.delete_student'):
        raise PermissionDenied

    student = get_object_or_404(Student, pk=pk)

    if request.method == 'POST':
        student.delete()
        return redirect('student_list')

    return render(request, 'students/student_confirm_delete.html', {
        'student': student
    })