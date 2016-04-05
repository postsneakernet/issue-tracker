#!/usr/bin/env python
# dao.py

import psycopg2


class Dao:
    DB_NAME = "issuetracker"
    DB_USER = "vagrant"

    def __init__(self, db_table, sql_create, sql_update):
        self.db_table = db_table
        self.sql_create = sql_create
        self.sql_update = sql_update


    def __str__(self):
        return "Dao for {} table".format(self.db_table)


    def get_connection(self):
        return psycopg2.connect("dbname={} user={}".format(self.DB_NAME, self.DB_USER))


    def close_connection(self, conn, cur):
        conn.close()


    def create(self, *args):
        conn = self.get_connection()
        cur = conn.cursor()
        sql = "INSERT INTO {} VALUES ({});".format(self.db_table, self.sql_create)
        cur.execute(sql, (args))
        conn.commit()
        result = cur.rowcount
        self.close_connection(conn, cur)
        return result == 1


    def retrieve(self, id):
        conn = self.get_connection()
        cur = conn.cursor()
        sql = "SELECT * FROM {} WHERE id=%s;".format(self.db_table)
        cur.execute(sql, (id,))
        result = cur.fetchone()
        self.close_connection(conn, cur)
        return result


    def retrieve_all(self):
        conn = self.get_connection()
        cur = conn.cursor()
        sql = "SELECT * FROM {};".format(self.db_table)
        cur.execute(sql)
        result = cur.fetchall()
        self.close_connection(conn, cur)
        return result


    def retrieve_match(self, where, *args):
        conn = self.get_connection()
        cur = conn.cursor()
        sql = "SELECT * FROM {} WHERE {};".format(self.db_table, where)
        cur.execute(sql, (args))
        result = cur.fetchall()
        self.close_connection(conn, cur)
        return result


    def update(self, id, *args):
        conn = self.get_connection()
        cur = conn.cursor()
        sql = "UPDATE {} SET {} WHERE id=%s;".format(self.db_table, self.sql_update)
        cur.execute(sql, (args + (id,)))
        conn.commit()
        result = cur.rowcount
        self.close_connection(conn, cur)
        return result == 1


    def delete(self, id):
        conn = self.get_connection()
        cur = conn.cursor()
        sql = "DELETE FROM {} WHERE id=%s;".format(self.db_table)
        cur.execute(sql, (id,))
        conn.commit()
        result = cur.rowcount
        self.close_connection(conn, cur)
        return result == 1


    def count(self):
        conn = self.get_connection()
        cur = conn.cursor()
        sql = "SELECT count(*) FROM {};".format(self.db_table)
        cur.execute(sql)
        result = cur.fetchone()
        self.close_connection(conn, cur)
        return result


class MaintainerDao(Dao):
    authenticate_admin = "username=%s AND password=%s AND is_admin=TRUE"

    def __init__(self):
        DB_TABLE = "maintainer"
        SQL_CREATE = "DEFAULT, %s, %s, %s, %s"
        SQL_UPDATE = "username=%s, email=%s, password=%s, is_admin=%s"
        super().__init__(DB_TABLE, SQL_CREATE, SQL_UPDATE)


class ProjectDao(Dao):
    def __init__(self):
        DB_TABLE = "project"
        SQL_CREATE = "DEFAULT, %s, %s, now(), now(), %s"
        SQL_UPDATE = "title=%s, description=%s, date_modified=now(), maintainer_id=%s"
        super().__init__(DB_TABLE, SQL_CREATE, SQL_UPDATE)


class TicketDao(Dao):
    def __init__(self):
        DB_TABLE = "ticket"
        SQL_CREATE = "DEFAULT, %s, %s, %s, %s, %s, 'open', now(), now(), %s"
        SQL_UPDATE = "name=%s, email=%s, title=%s, content=%s, current_priority=%s, " \
                     "current_status=%s, date_modified=now(), project_id=%s"
        super().__init__(DB_TABLE, SQL_CREATE, SQL_UPDATE)


class CommentDao(Dao):
    def __init__(self):
        DB_TABLE = "ticket_comment"
        SQL_CREATE = "DEFAULT, %s, %s, %s, %s, now(), %s"
        SQL_UPDATE = "name=%s, email=%s, is_maintainer=%s, content=%s, ticket_id=%s"
        super().__init__(DB_TABLE, SQL_CREATE, SQL_UPDATE)


def main():
    dao = MaintainerDao()
    result = dao.retrieve_match(dao.username_and_password, 'admin', 'admin')
    print(result)


if __name__ == "__main__":
    main()

