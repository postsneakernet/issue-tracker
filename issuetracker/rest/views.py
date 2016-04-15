# views.py

from datetime import datetime
from flask import request, jsonify, Blueprint
from issuetracker import db_session
from issuetracker.models import Comment, Ticket, Project, Maintainer

rest_blueprint = Blueprint('rest_blueprint', __name__)


@rest_blueprint.route('/api/v1/projects/', methods=['POST'])
def create_project():
    j = request.get_json()
    try:
        m = Maintainer.query.filter_by(id=j['maintainerId']).one()
        p = Project(j['title'], j['description'], m)
        db_session.add(p)
        db_session.commit()
        print(p)
    except Exception as e:
        print("Exception occurred: {}".format(e))
        return jsonify(error="There was an issue creating project resource.")

    return jsonify(success=j), 201


@rest_blueprint.route('/api/v1/projects/', methods=['GET'])
def get_projects():
    maintainer_id = request.args.get('maintainer')
    try:
        if maintainer_id is not None:
            projects = Project.query.filter_by(maintainer_id=maintainer_id).all()
        else:
            projects = Project.query.all()
    except Exception as e:
        print("Exception occurred: {}".format(e))
        return jsonify(error="There was an issue requesting project resources.")

    return jsonify(projects=[i.serialize for i in projects])


@rest_blueprint.route('/api/v1/projects/<int:project_id>', methods=['GET'])
def get_project(project_id):
    try:
        p = Project.query.filter_by(id=project_id).one()
    except Exception as e:
        print("Exception occurred: {}".format(e))
        return jsonify(error="There was an issue requesting project resource.")

    return jsonify(project=p.serialize)


@rest_blueprint.route('/api/v1/projects/<int:project_id>', methods=['PUT'])
def update_project(project_id):
    j = request.get_json()
    try:
        p = Project.query.filter_by(id=project_id).one()
        p.title = j['title']
        p.description = j['description']
        p.date_modified = datetime.now()

        db_session.add(p)
        db_session.commit()
        print(p)
    except Exception as e:
        print("Exception occurred: {}".format(e))
        return jsonify(error="There was an issue updating project resource.")

    return jsonify(project=p.serialize)


@rest_blueprint.route('/api/v1/projects/<int:project_id>', methods=['DELETE'])
def delete_project(project_id):
    try:
        p = Project.query.filter_by(id=project_id).one()
        tickets = Ticket.query.filter_by(project_id=project_id).all()
        for t in tickets:
            for c in t.comments:
                db_session.delete(c)
            db_session.delete(t)

        db_session.delete(p)
        db_session.commit()
        print(p)
    except Exception as e:
        print("Exception occurred: {}".format(e))
        return jsonify(error="There was an issue deleting project resource.")

    return jsonify(success="Project resource successfully deleted.")


@rest_blueprint.route('/api/v1/tickets/', methods=['POST'])
def create_ticket():
    j = request.get_json()
    try:
        p = Project.query.filter_by(id=j['projectId']).one()
        t = Ticket(j['name'],
                   j['email'],
                   j['title'],
                   j['content'],
                   j['priority'],
                   p)
        db_session.add(t)
        db_session.commit()
        print(t)
    except Exception as e:
        print("Exception occurred: {}".format(e))
        return jsonify(error="There was an issue creating ticket resource.")

    return jsonify(success=j), 201


@rest_blueprint.route('/api/v1/tickets/', methods=['GET'])
def get_tickets():
    project_id = request.args.get('project')
    try:
        if project_id is not None:
            tickets = Ticket.query.filter_by(project_id=project_id).all()
        else:
            tickets = Ticket.query.all()
    except Exception as e:
        print("Exception occurred: {}".format(e))
        return jsonify(error="There was an issue requesting ticket resources.")

    return jsonify(tickets=[i.serialize for i in tickets])


@rest_blueprint.route('/api/v1/tickets/<int:ticket_id>', methods=['GET'])
def get_ticket(ticket_id):
    try:
        t = Ticket.query.filter_by(id=ticket_id).one()
    except Exception as e:
        print("Exception occurred: {}".format(e))
        return jsonify(error="There was an issue requesting ticket resource.")

    return jsonify(ticket=t.serialize)


@rest_blueprint.route('/api/v1/tickets/<int:ticket_id>', methods=['PUT'])
def update_ticket(ticket_id):
    j = request.get_json()
    print(j)
    try:
        t = Ticket.query.filter_by(id=ticket_id).one()
        t.date_modified = datetime.now()
        t.name = j['name']
        t.email = j['email']
        t.title = j['title']
        t.content = j['content']
        t.current_priority = j['priority']
        t.current_status = j['status']

        db_session.add(t)
        db_session.commit()
    except Exception as e:
        print("Exception occurred: {}".format(e))
        return jsonify(error="There was an issue updating ticket resource.")

    return jsonify(ticket=t.serialize)


@rest_blueprint.route('/api/v1/tickets/<int:ticket_id>', methods=['DELETE'])
def delete_ticket(ticket_id):
    try:
        t = Ticket.query.filter_by(id=ticket_id).one()
        for c in t.comments:
            db_session.delete(c)
        db_session.delete(t)

        db_session.commit()
    except Exception as e:
        print("Exception occurred: {}".format(e))
        return jsonify(error="There was an issue deleting ticket resource.")

    return jsonify(success="Ticket resource successfully deleted.")


@rest_blueprint.route('/api/v1/comments/', methods=['POST'])
def create_comment():
    j = request.get_json()
    try:
        t = Ticket.query.filter_by(id=j['ticketId']).one()
        c = Comment(j['name'],
                    j['email'],
                    j['content'],
                    t)
        c.is_maintainer = True
        db_session.add(c)
        db_session.commit()
        print(c)
    except Exception as e:
        print("Exception occurred: {}".format(e))
        return jsonify(error="There was an issue creating comment resource.")

    return jsonify(success=j), 201


@rest_blueprint.route('/api/v1/comments/', methods=['GET'])
def get_comments():
    ticket_id = request.args.get('ticket')
    try:
        if ticket_id is not None:
            comments = Comment.query.filter_by(ticket_id=ticket_id).all()
        else:
            comments = Comment.query.all()
    except Exception as e:
        print("Exception occurred: {}".format(e))
        return jsonify(error="There was an issue requesting comment resources.")

    return jsonify(comments=[i.serialize for i in comments])


@rest_blueprint.route('/api/v1/comments/<int:comment_id>', methods=['GET'])
def get_comment(comment_id):
    try:
        c = Comment.query.filter_by(id=comment_id).one()
    except Exception as e:
        print("Exception occurred: {}".format(e))
        return jsonify(error="There was an issue requesting comment resource.")

    return jsonify(comment=c.serialize)


@rest_blueprint.route('/api/v1/comments/<int:comment_id>', methods=['PUT'])
def update_comment(comment_id):
    j = request.get_json()
    print(j)
    try:
        c = Comment.query.filter_by(id=comment_id).one()
        c.name = j['name']
        c.email = j['email']
        c.content = j['content']

        db_session.add(c)
        db_session.commit()
    except Exception as e:
        print("Exception occurred: {}".format(e))
        return jsonify(error="There was an issue updating comment resource.")

    return jsonify(comment=c.serialize)


@rest_blueprint.route('/api/v1/comments/<int:comment_id>', methods=['DELETE'])
def delete_comment(comment_id):
    try:
        c = Comment.query.filter_by(id=comment_id).one()

        db_session.delete(c)
        db_session.commit()
    except Exception as e:
        print("Exception occurred: {}".format(e))
        return jsonify(error="There was an issue deleting comment resource.")

    return jsonify(success="Comment resource successfully deleted.")
