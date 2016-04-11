-- maintainer table ddl
DROP TABLE IF EXISTS maintainer CASCADE;
CREATE TABLE maintainer (
    id serial PRIMARY KEY,
    username varchar(25) NOT NULL UNIQUE,
    email varchar(40) NOT NULL UNIQUE,
    password varchar(60) NOT NULL,
    is_admin boolean NOT NULL DEFAULT FALSE
);


-- project table ddl
DROP TABLE IF EXISTS project CASCADE;
CREATE TABLE project (
    id serial PRIMARY KEY,
    title varchar(80) NOT NULL,
    description varchar(1000) NOT NULL,
    date_created timestamp DEFAULT now(),
    date_modified timestamp DEFAULT now(),
    maintainer_id integer references maintainer NOT NULL
);


-- ticket table ddl
DROP TYPE IF EXISTS priority CASCADE;
CREATE TYPE priority AS ENUM ('low', 'medium', 'high');

DROP TYPE IF EXISTS status CASCADE;
CREATE TYPE status AS ENUM ('open', 'closed');

DROP TABLE IF EXISTS ticket CASCADE;
CREATE TABLE ticket (
    id serial PRIMARY KEY,
    name varchar(25) NOT NULL,
    email varchar(40) NOT NULL,
    title varchar(80) NOT NULL,
    content varchar(1000) NOT NULL,
    current_priority priority NOT NULL,
    current_status status NOT NULL DEFAULT 'open',
    date_created timestamp DEFAULT now(),
    date_modified timestamp DEFAULT now(),
    project_id integer references project NOT NULL
);


-- ticket_comment table ddl
DROP TABLE IF EXISTS ticket_comment CASCADE;
CREATE TABLE ticket_comment (
    id serial PRIMARY KEY,
    name varchar(25) NOT NULL,
    email varchar(40) NOT NULL,
    is_maintainer boolean NOT NULL DEFAULT FALSE,
    content varchar(500) NOT NULL,
    date_created timestamp DEFAULT now(),
    ticket_id integer references ticket NOT NULL
);
