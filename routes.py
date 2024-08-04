from flask import render_template, request, redirect, url_for
from . import db
from .models import Student
from .forms import StudentForm
from flask import current_app as app

@app.route('/')
def home():
    students = Student.query.all()
    return render_template('index.html', students=students)

@app.route('/add', methods=['GET', 'POST'])
def add_student():
    form = StudentForm()
    if form.validate_on_submit():
        student = Student(
            name=form.name.data,
            matric_number=form.matric_number.data,
            phone_number=form.phone_number.data,
            gender=form.gender.data,
            level=form.level.data
        )
        db.session.add(student)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add_student.html', form=form)

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_student(id):
    student = Student.query.get_or_404(id)
    form = StudentForm(obj=student)
    if form.validate_on_submit():
        student.name = form.name.data
        student.matric_number = form.matric_number.data
        student.phone_number = form.phone_number.data
        student.gender = form.gender.data
        student.level = form.level.data
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('edit_student.html', form=form, student=student)

@app.route('/view/<int:id>')
def view_student(id):
    student = Student.query.get_or_404(id)
    return render_template('view_student.html', student=student)

@app.route('/delete/<int:id>')
def delete_student(id):
    student = Student.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    return redirect(url_for('home'))
