# views.py

from flask import render_template, redirect, request, flash, \
    session, url_for, jsonify, Blueprint

from .models.dao import MaintainerDao, ProjectDao, TicketDao, CommentDao

admin_blueprint = Blueprint('admin_blueprint', __name__, template_folder='templates')


@admin_blueprint.route('/admin/login/', methods=['GET', 'POST'])
def admin_login():
    error = None

    if 'logged_in' in session:
        return redirect(url_for('.admin_index'))

    if request.method == 'POST':
        dao = MaintainerDao()
        username = request.form['username']
        password = request.form['password']
        result = dao.retrieve_match(dao.authenticate_admin, username, password)

        if len(result) != 1:
            error = 'There was an error authenticating your account. Please try again.'
        else:
            session['logged_in'] = True
            session['admin'] = username
            flash('You were successfully authenticated.')
            return redirect(url_for('.admin_index'))

    return render_template('admin/admin_login.html', error=error)


@admin_blueprint.route('/admin/logout/', methods=['GET'])
def admin_logout():
    session.pop('logged_in', None)
    session.pop('admin', None)
    flash('You have been logged out.')
    return redirect(url_for('index'))


@admin_blueprint.route('/admin/', methods=['GET'])
def admin_index():
    return render_template('admin/admin.html')


@admin_blueprint.route('/ajax/admin/', methods=['GET'])
def ajax_admin():
    if 'logged_in' not in session:
        return jsonify(error="authentication error")

    return jsonify(maintainer_count=MaintainerDao().count(),
                   project_count=ProjectDao().count(),
                   ticket_count=TicketDao().count(),
                   comment_count=CommentDao().count())


@admin_blueprint.route('/ajax/admin/maintainers/', methods=['GET'])
def ajax_maintainers():
    if 'logged_in' not in session:
        return jsonify(error="authentication error")

    results = MaintainerDao().retrieve_all()
    json = ["id", "username", "email", "skip", "isAdmin"]
    maintainers = []
    for maintainer in results:
        d = {}
        for k, v in zip(json, maintainer):
            d[k] = v
        d.pop("skip", None)
        maintainers.append(d)

    return jsonify(maintainers=maintainers)


@admin_blueprint.route('/ajax/admin/maintainers/create/', methods=['POST'])
def ajax_create_maintainers():
    if 'logged_in' not in session:
        return jsonify(error="authentication error")

    json_data = request.get_json()
    try:
        if json_data['password'] == json_data['confirmPassword']:
            MaintainerDao().create(json_data['username'], json_data['email'],
                                   json_data['password'], json_data['isAdmin'])
        else:
            return jsonify(error="Passwords don't match.")

    except:
        return jsonify(error="There was in issue creating new maintainer.")

    return jsonify(success="New maintainer was created.")


@admin_blueprint.route('/ajax/admin/maintainers/update/<maintainer_id>', methods=['GET', 'POST'])
def ajax_update_maintainers(maintainer_id):
    if 'logged_in' not in session:
        return jsonify(error="authentication error")

    if request.method == 'POST':
        # todo verify content exists and not null
        json_data = request.get_json()
        try:
            if 'delete' in json_data:
                MaintainerDao().delete(json_data['id'])
                return jsonify(success="Deletion of maintainer with id {} was successful".format(json_data['id']))
            else:
                MaintainerDao().update(json_data['id'], json_data['username'],
                                       json_data['email'], json_data['password'],
                                       json_data['isAdmin'])
                return jsonify(success="Successfully updated maintainer with id {}.".format(json_data['id']))

        except:
            return jsonify(error="There was an issue updating maintainer.")

    result = MaintainerDao().retrieve(maintainer_id)
    print(result)
    if result is None:
        return jsonify(error="Maintainer with id {} not found".format(maintainer_id))

    json = ["id", "username", "email", "password", "isAdmin"]
    d = {}
    for k, v in zip(json, result):
        print("k: {}, v: {}".format(k, v))
        d[k] = v

    d['confirmPassword'] = d['password']
    return jsonify(d)


@admin_blueprint.route('/ajax/admin/projects/', methods=['GET'])
def ajax_projects():
    if 'logged_in' not in session:
        return jsonify(error="authentication error")

    results = ProjectDao().retrieve_all()
    json = ["id", "title", "description", "dateCreated", "dateModified", "maintainerId"]
    projects = []
    for project in results:
        d = {}
        for k, v in zip(json, project):
            d[k] = v
        projects.append(d)

    return jsonify(projects=projects)


@admin_blueprint.route('/ajax/admin/projects/create/', methods=['GET', 'POST'])
def ajax_create_projects():
    if 'logged_in' not in session:
        return jsonify(error="authentication error")

    if request.method == 'POST':
        json_data = request.get_json()
        try:
            ProjectDao().create(json_data['title'], json_data['description'], json_data['maintainerId'])
            return jsonify(success="New project was created.")
        except:
            return jsonify(error="There was in issue creating new maintainer.")

    results = MaintainerDao().retrieve_all()
    maintainers = []
    for maintainer in results:
        d = {}
        d['id'] = maintainer[0]
        maintainers.append(d)

    return jsonify(maintainers=maintainers)


@admin_blueprint.route('/ajax/admin/projects/update/<project_id>', methods=['GET', 'POST'])
def ajax_update_projects(project_id):
    if 'logged_in' not in session:
        return jsonify(error="authentication error")

    if request.method == 'POST':
        json_data = request.get_json()
        try:
            if 'delete' in json_data:
                ProjectDao().delete(json_data['id'])
                return jsonify(success="Deletion of project with id {} was successful".format(json_data['id']))
            else:
                ProjectDao().update(json_data['id'], json_data['title'],
                                    json_data['description'], json_data['maintainerId'])
                return jsonify(success="Successfully updated project with id {}.".format(json_data['id']))
        except:
            return jsonify(error="There was an issue updating project.")

    result = ProjectDao().retrieve(project_id)
    print(result)
    if result is None:
        return jsonify(error="Project with id {} not found".format(project_id))

    json = ["id", "title", "description", "skip", "skip", "maintainerId"]
    d = {}
    for k, v in zip(json, result):
        print("k: {}, v: {}".format(k, v))
        d[k] = v
    d.pop('skip', None)
    print("dictionary d: {}".format(d))

    results = MaintainerDao().retrieve_all()
    maintainers = []
    for maintainer in results:
        d2 = {}
        d2['id'] = maintainer[0]
        if maintainer[0] == d['maintainerId']:
            d2['isMaintainer'] = True
        maintainers.append(d2)

    return jsonify(d, maintainers=maintainers)


@admin_blueprint.route('/ajax/admin/tickets/', methods=['GET'])
def ajax_tickets():
    if 'logged_in' not in session:
        return jsonify(error="authentication error")

    results = TicketDao().retrieve_all()
    json = ["id", "name", "email", "title", "content", "priority", "status", "dateCreated", "dateModified", "projectId"]
    tickets = []
    for ticket in results:
        d = {}
        for k, v in zip(json, ticket):
            d[k] = v
        tickets.append(d)

    return jsonify(tickets=tickets)


@admin_blueprint.route('/ajax/admin/tickets/create/', methods=['GET', 'POST'])
def ajax_create_tickets():
    if 'logged_in' not in session:
        return jsonify(error="authentication error")

    if request.method == 'POST':
        json_data = request.get_json()
        try:
            TicketDao().create(json_data['name'], json_data['email'],
                    json_data['title'], json_data['content'], json_data['priority'],
                    json_data['projectId'])
            return jsonify(success="New ticket was created.")
        except:
            return jsonify(error="There was in issue creating new ticket.")

    results = ProjectDao().retrieve_all()
    projects = []
    for project in results:
        d = {}
        d['id'] = project[0]
        projects.append(d)

    return jsonify(projects=projects)


@admin_blueprint.route('/ajax/admin/tickets/update/<ticket_id>', methods=['GET', 'POST'])
def ajax_update_tickets(ticket_id):
    if 'logged_in' not in session:
        return jsonify(error="authentication error")

    if request.method == 'POST':
        # todo verify content exists and not null
        json_data = request.get_json()
        try:
            if 'delete' in json_data:
                TicketDao().delete(json_data['id'])
                return jsonify(success="Deletion of ticket with id {} was successful".format(json_data['id']))
            else:
                TicketDao().update(json_data['id'], json_data['name'], json_data['email'],
                                   json_data['title'], json_data['content'], json_data['priority'],
                                   json_data['status'], json_data['projectId'])
                return jsonify(success="Successfully updated ticket with id {}.".format(json_data['id']))
        except:
            return jsonify(error="There was an issue updating ticket.")

    result = TicketDao().retrieve(ticket_id)
    print(result)
    if result is None:
        return jsonify(error="Ticket with id {} not found".format(ticket_id))

    json = ["id", "name", "email", "title", "content", "priority", "status", "skip", "skip", "projectId"]
    d = {}
    for k, v in zip(json, result):
        print("k: {}, v: {}".format(k, v))
        d[k] = v
    d.pop('skip', None)

    priority = d['priority']
    d[priority] = True
    status = d['status']
    d[status] = True
    print("dictionary d: {}".format(d))

    results = ProjectDao().retrieve_all()
    projects = []
    for project in results:
        d2 = {}
        d2['id'] = project[0]
        if project[0] == d['projectId']:
            d2['isProject'] = True
        projects.append(d2)

    return jsonify(d, projects=projects)


@admin_blueprint.route('/ajax/admin/comments/', methods=['GET'])
def ajax_comments():
    if 'logged_in' not in session:
        return jsonify(error="authentication error")

    results = CommentDao().retrieve_all()
    json = ["id", "name", "email", "isMaintainer", "content", "dateCreated", "ticketId"]
    comments = []
    for comment in results:
        d = {}
        for k, v in zip(json, comment):
            d[k] = v
        comments.append(d)

    return jsonify(comments=comments)


@admin_blueprint.route('/ajax/admin/comments/create/', methods=['GET', 'POST'])
def ajax_create_comments():
    if 'logged_in' not in session:
        return jsonify(error="authentication error")

    if request.method == 'POST':
        json_data = request.get_json()
        try:
            CommentDao().create(json_data['name'], json_data['email'],
                    json_data['isMaintainer'], json_data['content'], json_data['ticketId'])
            return jsonify(success="New comment was created.")
        except:
            return jsonify(error="There was in issue creating new comment.")

    results = TicketDao().retrieve_all()
    tickets = []
    for ticket in results:
        d = {}
        d['id'] = ticket[0]
        tickets.append(d)

    return jsonify(tickets=tickets)


@admin_blueprint.route('/ajax/admin/comments/update/<comment_id>', methods=['GET', 'POST'])
def ajax_update_comments(comment_id):
    if 'logged_in' not in session:
        return jsonify(error="authentication error")

    if request.method == 'POST':
        # todo verify content exists and not null
        json_data = request.get_json()
        try:
            if 'delete' in json_data:
                CommentDao().delete(json_data['id'])
                return jsonify(success="Deletion of comment with id {} was successful".format(json_data['id']))
            else:
                print(json_data)
                CommentDao().update(json_data['id'], json_data['name'], json_data['email'],
                                   json_data['isMaintainer'], json_data['content'], json_data['ticketId'])
                return jsonify(success="Successfully updated comment with id {}.".format(json_data['id']))
        except Exception as e:
            print(e)
            return jsonify(error="There was an issue updating comment.")

    result = CommentDao().retrieve(comment_id)
    print(result)
    if result is None:
        return jsonify(error="Comment with id {} not found".format(ticket_id))

    json = ["id", "name", "email", "isMaintainer", "content", "skip", "ticketId"]
    d = {}
    for k, v in zip(json, result):
        print("k: {}, v: {}".format(k, v))
        d[k] = v
    d.pop('skip', None)

    results = TicketDao().retrieve_all()
    tickets = []
    for ticket in results:
        d2 = {}
        d2['id'] = ticket[0]
        if ticket[0] == d['ticketId']:
            d2['isTicket'] = True
        tickets.append(d2)

    return jsonify(d, tickets=tickets)
