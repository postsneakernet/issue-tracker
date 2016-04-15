# models.py

from sqlalchemy.orm import relationship

from sqlalchemy.orm.session import object_session

from issuetracker import Base


class Maintainer(Base):
    __table__ = Base.metadata.tables['maintainer']

    projects = relationship("Project", backref="maintainer")

    def __init__(self, username=None, email=None, password=None, is_admin=None):
        self.username = name
        self.email = email
        self.password = password
        self.is_admin = is_admin

    def __repr__(self):
        return "<Maintainer(id='%s', username='%s')>" % (self.id, self.username)

    @property
    def serialize(self):
        return {
                'id': self.id,
                'username': self.username,
                'email': self.email,
                'isAdmin': self.is_admin,
        }


class Project(Base):
    __table__ = Base.metadata.tables['project']

    tickets = relationship("Ticket", backref="project")

    def __init__(self, title=None, description=None, maintainer=None):
        self.title = title
        self.description = description
        self.maintainer = maintainer

    def __repr__(self):
        return "<Project(id='%s', title='%s')>" % (self.id, self.title)

    @property
    def serialize(self):
        return {
                'id': self.id,
                'title': self.title,
                'description': self.description,
                'created': self.date_created,
                'modified': self.date_modified,
                'maintainerId': self.maintainer_id,
        }

    def _get_open_tickets(self):
        return object_session(self).query(Ticket).with_parent(self).filter(Ticket.current_status=='open').all()

    open_tickets = property(_get_open_tickets)

    def _get_high_tickets(self):
        return object_session(self).query(Ticket).with_parent(self).filter(Ticket.current_priority=='high').all()

    high_tickets = property(_get_high_tickets)


class Ticket(Base):
    __table__ = Base.metadata.tables['ticket']

    comments = relationship("Comment", backref="ticket")

    def __init__(self, name=None, email=None, title=None, content=None,
                 current_priority=None, project=None):
        self.name = name
        self.email = email
        self.title = title
        self.content = content
        self.current_priority = current_priority
        self.project = project

    def __repr__(self):
        return "<Ticket(id='%s', title='%s')>" % (self.id, self.title)

    @property
    def serialize(self):
        return {
                'id': self.id,
                'name': self.name,
                'email': self.email,
                'title': self.title,
                'content': self.content,
                'created': self.date_created,
                'modified': self.date_modified,
                'projectId': self.project_id,
        }


class Comment(Base):
    __table__ = Base.metadata.tables['ticket_comment']

    def __init__(self, name=None, email=None, content=None, ticket=None):
        self.name = name
        self.email = email
        self.content = content
        self.ticket = ticket

    def __repr__(self):
        return "<Comment(id='%s', name='%s', created='%s')>" % (self.id, self.name, self.date_created)

    @property
    def serialize(self):
        return {
                'id': self.id,
                'name': self.name,
                'email': self.email,
                'isMaintainer': self.is_maintainer,
                'content': self.content,
                'created': self.date_created,
                'ticketId': self.ticket_id,
        }
