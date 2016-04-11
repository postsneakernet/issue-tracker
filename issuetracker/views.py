# views.py

from flask import Flask, render_template, redirect, request, flash, \
        session, url_for, jsonify, make_response, abort

from sqlalchemy import desc

from issuetracker.admin.views import admin_blueprint

from issuetracker.rest.views import rest_blueprint

from issuetracker import app, db_session

from issuetracker.models import Maintainer, Project, Ticket, Comment

app.register_blueprint(admin_blueprint)
app.register_blueprint(rest_blueprint)


@app.teardown_appcontext
def shutdown_session(exception=None):
    print("teardown request processed")
    db_session.remove()


# todo:
# create 404 img
@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404


# todo:
# add brief site description
# fix template formatting
@app.route('/', methods=['GET'])
def index():
    projects = Project.query.order_by(desc(Project.date_modified)).limit(2).all()
    tickets = Ticket.query.order_by(desc(Ticket.date_modified)).limit(2).all()
    return render_template('index.html', projects=projects, tickets=tickets)


# todo:
# show ticket count, open ticket count, high priority count
@app.route('/projects/', methods=['GET'])
def project_index():
    projects = Project.query.order_by(Project.title).all()
    return render_template('project_index.html', projects=projects)

# todo:
# show data created, adjusted in template
# show date modified for recent activity of ticket
# adjust spacing of info nuggets with half-tab class
@app.route('/projects/<int:project_id>', methods=['GET'])
def project_detail(project_id):
    project = Project.query.filter_by(id=project_id).first()
    tickets = Ticket.query.filter_by(project_id=project_id).order_by(desc(Ticket.date_modified)).limit(2).all()

    if project is None:
        abort(404)

    return render_template('project_detail.html', project=project, tickets=tickets)


# todo:
# adjust spacing of info nuggets with half-tab class
# show date modified for recent activity of ticket
@app.route('/projects/<int:project_id>/tickets/', methods=['GET'])
def project_tickets(project_id):
    project = Project.query.filter_by(id=project_id).first()
    tickets = Ticket.query.filter_by(project_id=project_id).filter_by(current_status='open').order_by(desc(Ticket.date_created)).all()

    if project is None:
        abort(404)

    return render_template('project_tickets.html', project=project, tickets=tickets)


# todo:
# display ticket info in template
# display all comments below ticket
# add comment form at bottom with validation
# validate, clean, and save comment in db and flash success message
@app.route('/projects/<int:project_id>/tickets/<int:ticket_id>', methods=['GET', 'POST'])
def ticket_detail(project_id, ticket_id):
    project = Project.query.filter_by(id=project_id).first()
    ticket = Ticket.query.filter_by(id=ticket_id).filter_by(current_status='open').first()

    if project is None:
        abort(404)

    if ticket is None:
        abort(404)

    if request.method == 'POST':
        pass

    return render_template('ticket_detail.html', project=project, ticket=ticket)


# todo:
# adjust spacing of info nuggets with half-tab class
# show date modified for recent activity of ticket
@app.route('/projects/<int:project_id>/archive/', methods=['GET'])
def archive_index(project_id):
    project = Project.query.filter_by(id=project_id).first()
    tickets = Ticket.query.filter_by(project_id=project_id).filter_by(current_status='closed').order_by(desc(Ticket.date_modified)).all()

    if project is None:
        abort(404)

    return render_template('archive_index.html', project=project, tickets=tickets)


# todo:
# display ticket info in template
# display all comments below ticket
@app.route('/projects/<int:project_id>/archive/<int:ticket_id>', methods=['GET'])
def archive_detail(project_id, ticket_id):
    project = Project.query.filter_by(id=project_id).first()
    ticket = Ticket.query.filter_by(id=ticket_id).filter_by(current_status='closed').first()

    if project is None:
        abort(404)

    if ticket is None:
        abort(404)

    return render_template('archive_detail.html', project=project, ticket=ticket)


# todo:
# create ticket form in template with validation
# validate, clean, and save ticket in db and flash success message
@app.route('/projects/<int:project_id>/submit/', methods=['GET', 'POST'])
def submit_ticket(project_id):
    project = Project.query.filter_by(id=project_id).first()

    if project is None:
        abort(404)

    if request.method == 'POST':
        pass

    return render_template('submit_ticket.html', project=project)


# todo:
# adjust spacing of info nuggets with half-tab class
# show date modified for recent activity of ticket
@app.route('/tickets/', methods=['GET'])
def ticket_index():
    tickets = Ticket.query.filter_by(current_status='open').order_by(desc(Ticket.date_created)).all()
    return render_template('ticket_index.html', tickets=tickets)







# todo:
# accept form and query models
# setup template to dispaly results or nothing found msg
@app.route('/search/', methods=['GET'])
def search():
    return render_template('search.html')






# todo:
# setup rest api for models
# create angular spa
@app.route('/dashboard/', methods=['GET'])
def dashboard():
    return render_template('dashboard.html')
