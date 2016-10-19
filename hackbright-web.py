from flask import Flask, request, render_template

import hackbright

app = Flask(__name__)


@app.route("/student", methods=['GET'])
def get_student():
    """Show information about a student."""

    github = request.args.get('github', 'jhacks')
    first, last, github = hackbright.get_student_by_github(github)
    projects = hackbright.get_grades_by_github(github)
    return render_template("student_info.html", first=first, last=last, 
                            github=github, projects=projects)

@app.route("/student-form", methods=['GET'])
def get_student_form():
    """Show form for searching for a student."""

    return render_template("student_search.html")

@app.route("/student-add", methods=['GET'])
def get_add_form():
    """Show form for adding students"""

    return render_template("student_add.html")

@app.route("/student-add", methods=['POST'])
def student_add():
    """Add a student."""
    first_name = request.form.get('firstname')
    last_name = request.form.get('lastname')
    github = request.form.get('github')
    hackbright.make_new_student(first_name, last_name, github)
    return render_template('add_confirmation.html', first=first_name, last=last_name, github=github)

@app.route("/project", methods=['GET'])
def project():
    """Show project info"""

    title = request.args.get('title')
    project_title, description, max_grade = hackbright.get_project_by_title(title)
    student_grades = hackbright.get_grades_by_title(title)
    return render_template("project_details.html", project_title=project_title, description=description, max_grade=max_grade, student_grades=student_grades)



if __name__ == "__main__":
    hackbright.connect_to_db(app)
    app.run(debug=True)
