# issuetracker.py

from flask import Flask, render_template, redirect, request, flash, \
    session, url_for, jsonify, make_response

from admin.admin import admin_blueprint

app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')
app.register_blueprint(admin_blueprint)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/projects', methods=['GET'])
def projects():
    return render_template('projects.html')


@app.route('/projects/id', methods=['GET'])
def project_detail():
    return render_template('project_detail.html')


@app.route('/projects/id/submit', methods=['GET'])
def submit_ticket():
    return render_template('submit_ticket.html')


@app.route('/projects/id/tickets', methods=['GET'])
def project_tickets():
    return render_template('project_tickets.html')


@app.route('/projects/id/tickets/id', methods=['GET'])
def ticket_detail():
    return render_template('ticket_detail.html')


@app.route('/projects/id/archive', methods=['GET'])
def archive():
    return render_template('archive.html')


@app.route('/projects/id/archive/id', methods=['GET'])
def archive_detail():
    return render_template('archive_detail.html')


@app.route('/tickets', methods=['GET'])
def tickets():
    return render_template('tickets.html')


@app.route('/search', methods=['GET'])
def search():
    return render_template('search.html')


@app.route('/dashboard', methods=['GET'])
def dashboard():
    return render_template('dashboard.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
