# admin.py


from flask import render_template, redirect, request, flash, \
    session, url_for, jsonify, Blueprint


admin_blueprint = Blueprint('admin_blueprint', __name__, template_folder='templates')


@admin_blueprint.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    error = None

    if 'logged_in' in session:
        return redirect(url_for('.admin_index'))

    if request.method == 'POST':
        print("post method")
        if request.form['username'] != 'admin':
            print("in if")
            error = 'Invalid username'
        elif request.form['password'] != 'admin':
            print("in elif")
            error = 'Invalid password'
        else:
            print("in else")
            session['logged_in'] = True
            session['admin'] = request.form['username']
            flash('You were successfully authenticated')
            return redirect(url_for('.admin_index'))

    return render_template('admin/admin_login.html', error=error)


@admin_blueprint.route('/admin/logout', methods=['GET'])
def admin_logout():
    session.pop('logged_in', None)
    flash('You have been logged out')
    return redirect(url_for('index'))


@admin_blueprint.route('/admin', methods=['GET'])
def admin_index():
    return render_template('admin/admin.html')


@admin_blueprint.route('/ajax/admin', methods=['GET'])
def ajax_admin():
    if 'logged_in' not in session:
        return jsonify(error="authentication error")

    return jsonify(maintainer_count=3,
                   project_count=5,
                   ticket_count=11,
                   comment_count=24)


@admin_blueprint.route('/ajax/admin/maintainers', methods=['GET'])
def ajax_maintainers():
    if 'logged_in' not in session:
        return jsonify(error="authentication error")

    return jsonify(
            maintainers=[
                         {
                            "id": 1,
                            "username": "elliot",
                            "email": "elliot@elliothutchinson.com",
                            "admin": True
                         },
                         {
                            "id": 2,
                            "username": "james",
                            "email": "james@gmail.com",
                            "admin": False
                         },
                         {
                            "id": 3,
                            "username": "sneakernet",
                            "email": "ps@postsneakernet.com",
                            "admin": False
                         }
            ])


@admin_blueprint.route('/ajax/admin/maintainers/create', methods=['POST'])
def ajax_create_maintainers():
    if 'logged_in' not in session:
        print("not logged in")
        return jsonify(error="authentication error")

    print(request.form)
    print(request.data)
    json_data = request.get_json()
    try:
        print(json_data.keys())
        print(json_data['username'])
        print(json_data['email'])
        print(json_data['password'])
        print(json_data['confirmPassword'])
        print(json_data['isAdmin'])

    except:
        print("that didn't work but carry on")
        return jsonify(error="authentication error")

    return jsonify(success="New maintainer was successfully saved")
    #return jsonify(error="simulating error with submission")


@admin_blueprint.route('/ajax/admin/maintainers/update', methods=['GET', 'POST'])
def ajax_update_maintainers():
    if 'logged_in' not in session:
        print("not logged in")
        return jsonify(error="authentication error")

    if request.method == 'POST':
        # verify content exists and not null
        json_data = request.get_json()
        id = -1
        try:
            print(json_data.keys())
            id = json_data['id']
            if 'delete' in json_data:
                return jsonify(success="Deletion of object with id {} was successful".format(id))

        except:
            print("ooops there was an issue")
            return jsonify(error="There was an issue updating data")

        return jsonify(success="Successfully updated id {}".format(id))

    return jsonify(id=111,
                   username="elliot",
                   email="elliot@elliot.com",
                   password="pass1",
                   confirmPassword="pass1",
                   isAdmin=True)
