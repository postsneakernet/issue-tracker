# issuetracker.py

from flask import Flask, render_template, redirect, request, flash, \
    session, url_for, jsonify, make_response


app = Flask(__name__)
app.config.from_object('config.DevelopmentConfig')


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


@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    error = None

    if 'logged_in' in session:
        return redirect(url_for('admin'))

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
            return redirect(url_for('admin'))

    return render_template('admin_login.html', error=error)


@app.route('/admin/logout', methods=['GET'])
def admin_logout():
    session.pop('logged_in', None)
    flash('You have been logged out')
    return redirect(url_for('index'))


@app.route('/admin', methods=['GET'])
def admin():
    return render_template('admin.html')


@app.route('/ajax/admin', methods=['GET'])
def ajax_admin():
    if 'logged_in' not in session:
        return jsonify(error="authentication error")

    return jsonify(maintainer_count=3,
                   project_count=5,
                   ticket_count=11,
                   comment_count=24)


@app.route('/ajax/admin/maintainers', methods=['GET'])
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


@app.route('/ajax/admin/maintainers/create', methods=['POST'])
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


@app.route('/ajax/admin/maintainers/update', methods=['GET', 'POST'])
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


if __name__ == '__main__':
    app.run(host='0.0.0.0')
