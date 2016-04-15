# test_api.py

import requests


def create_project():
    json = {'title': 'project title',
            'description': 'project description',
            'maintainerId': 11,
           }

    r = requests.post('http://localhost:5000/api/v1/projects/', json=json)
    print(r.json())


def get_projects():
    r = requests.get('http://localhost:5000/api/v1/projects/')
    print(r.json())


def get_projects_filter():
    r = requests.get('http://localhost:5000/api/v1/projects/?maintainer=1')
    print(r.json())


def get_project(id):
    r = requests.get('http://localhost:5000/api/v1/projects/{}'.format(id))
    print(r.json())


def update_project(id):
    json = {'title': 'new title',
            'description': 'new description',
           }

    r = requests.put('http://localhost:5000/api/v1/projects/{}'.format(id), json=json)
    print(r.json())


def delete_project(id):
    r = requests.delete('http://localhost:5000/api/v1/projects/{}'.format(id))
    print(r.json())


def create_ticket():
    json = {'name': 'ticket name',
            'email': 'ticket email',
            'title': 'ticket title',
            'content': 'ticket content',
            'priority': 'low',
            'projectId': 1,
           }

    r = requests.post('http://localhost:5000/api/v1/tickets/', json=json)
    print(r.json())


def get_tickets():
    r = requests.get('http://localhost:5000/api/v1/tickets/')
    print(r.json())


def get_tickets_filter():
    r = requests.get('http://localhost:5000/api/v1/tickets/?project=1')
    print(r.json())


def get_ticket(id):
    r = requests.get('http://localhost:5000/api/v1/tickets/{}'.format(id))
    print(r.json())


def update_ticket(id):
    json = {'name': 'new name',
            'email': 'new email',
            'title': 'new title',
            'content': 'new content',
            'priority': 'low',
            'status': 'closed',
           }

    r = requests.put('http://localhost:5000/api/v1/tickets/{}'.format(id), json=json)
    print(r.json())


def delete_ticket(id):
    r = requests.delete('http://localhost:5000/api/v1/tickets/{}'.format(id))
    print(r.json())


def create_comment():
    json = {'name': 'comment name',
            'email': 'comment email',
            'content': 'comment content',
            'ticketId': 1,
           }

    r = requests.post('http://localhost:5000/api/v1/comments/', json=json)
    print(r.json())


def get_comments():
    r = requests.get('http://localhost:5000/api/v1/comments/')
    print(r.json())


def get_comments_filter():
    r = requests.get('http://localhost:5000/api/v1/comments/?ticket=1')
    print(r.json())


def get_comment(id):
    r = requests.get('http://localhost:5000/api/v1/comments/{}'.format(id))
    print(r.json())


def update_comment(id):
    json = {'name': 'new name',
            'email': 'new email',
            'content': 'new content',
           }

    r = requests.put('http://localhost:5000/api/v1/comments/{}'.format(id), json=json)
    print(r.json())


def delete_comment(id):
    r = requests.delete('http://localhost:5000/api/v1/comments/{}'.format(id))
    print(r.json())


if __name__ == "__main__":
    get_all_tickets_filter()

