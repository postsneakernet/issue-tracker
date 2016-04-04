# admin.py


from flask import render_template, redirect, request, flash, \
    session, url_for, jsonify, Blueprint

from .models.dao import MaintainerDao, ProjectDao, TicketDao, CommentDao

admin_blueprint = Blueprint('admin_blueprint', __name__, template_folder='templates')


@admin_blueprint.route('/admin/login', methods=['GET', 'POST'])
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


@admin_blueprint.route('/admin/logout', methods=['GET'])
def admin_logout():
    session.pop('logged_in', None)
    session.pop('admin', None)
    flash('You have been logged out.')
    return redirect(url_for('index'))


@admin_blueprint.route('/admin', methods=['GET'])
def admin_index():
    return render_template('admin/admin.html')


@admin_blueprint.route('/ajax/admin', methods=['GET'])
def ajax_admin():
    if 'logged_in' not in session:
        return jsonify(error="authentication error")

    return jsonify(maintainer_count=MaintainerDao().count(),
                   project_count=ProjectDao().count(),
                   ticket_count=TicketDao().count(),
                   comment_count=CommentDao().count())


@admin_blueprint.route('/ajax/admin/maintainers', methods=['GET'])
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


@admin_blueprint.route('/ajax/admin/maintainers/create', methods=['POST'])
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
