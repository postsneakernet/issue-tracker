# views.py

from flask import request, jsonify, Blueprint

from issuetracker import db_session

from issuetracker.models import Project

rest_blueprint = Blueprint('rest_blueprint', __name__)


@rest_blueprint.route('/api/v1.0/projects/', methods=['GET'])
def get_projects():
    maintainer_id = request.args.get('maintainer')
    try:
        if maintainer_id is not None:
            projects = Project.query.filter_by(maintainer_id=maintainer_id).all()
        else:
            projects = Project.query.all()
    except Exception as e:
        print(e)
        return jsonify(error="There was an issue with resource request.")

    return jsonify(projects=[i.serialize for i in projects])


@rest_blueprint.route('/api/v1.0/projects/', methods=['POST'])
def create_project():
    return jsonify(error="not implemented yet")


@rest_blueprint.route('/api/v1.0/projects/<int:project_id>', methods=['GET'])
def get_project(project_id):
    return jsonify(error="not implemented yet")


@rest_blueprint.route('/api/v1.0/projects/<int:project_id>', methods=['PUT'])
def update_project(project_id):
    return jsonify(error="not implemented yet")


@rest_blueprint.route('/api/v1.0/projects/<int:project_id>', methods=['DELETE'])
def delete_project(project_id):
    return jsonify(error="not implemented yet")
