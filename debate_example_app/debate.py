""" 
authentication.py Example App: Debate
=====================================

Database schema
---------------

This is an example of the database schema for PostgreSQL. You must adapt the
schema to your own database server, and create the specified tables before
using the example app. It is assumed that the autentication.py users table is
called ``authenticationpy_users``, and you should edit this name if your table
is called differently. ::

   CREATE TABLE debates (
     id         serial PRIMARY KEY,
     title      varchar(255) UNIQUE,
     topic      text,
     posted_at  timestamp DEFAULT CURRENT_TIMESTAMP,
     author_id  integer REFERENCES authenticationpy_users (id)
   );
   CREATE INDEX title_index ON debates (title);

   CREATE TABLE arguments (
     id         serial PRIMARY KEY,
     debate_id  integer REFERENCES debates (id)
     argument   text,
     posted_at  timestamp DEFAULT CURRENT_TIMESTAMP,
     author_id  integer REFERENCES authenticationpy_users (id),
     UNIQUE (debate_id, author_id)
   );

"""

import web
from authenticationpy.auth import User


class debates:
    def GET(self):
        pass


class new_debate:
    def POST(self):
        pass


class debate:
    def GET(self, title):
        pass

    def POST(self, title):
        pass


class delete_debate:
    def POST(self, title):
        pass


class argument:
    def GET(self, title, username):
        pass

    def POST(self, title, username):
        pass


class delete_argument:
    def POST(self, title, username):
        pass
