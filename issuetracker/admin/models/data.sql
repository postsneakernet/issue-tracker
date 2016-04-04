-- maintainer table dml
INSERT INTO maintainer VALUES (DEFAULT, 'elliot', 'elliot@eh.com', 'pass', TRUE);
INSERT INTO maintainer VALUES (DEFAULT, 'james', 'james@someemail.com', 'pass', FALSE);


-- project table dml
INSERT INTO project VALUES (DEFAULT, 'CMS Project', 'CMS issue tracker', now(), now(), 1);
INSERT INTO project VALUES (DEFAULT, 'CRM Project', 'CRM issue tracker', now(), now(), 1);


-- ticket table dml
INSERT INTO ticket VALUES (DEFAULT, 'elliot', 'e@someemail.com',
        'Cannot import from Word after update',
        'Some rather involved description about this issue being experienced',
        'medium', 'open', now(), now(), 1);
INSERT INTO ticket VALUES (DEFAULT, 'joey jojo', 'jotaro@mail.com',
        'Settings are not saving properly',
        'Some rather involved description about this issue being experienced',
        'high', 'open', now(), now(), 1);


-- ticket_comment table dml
INSERT INTO ticket_comment VALUES(DEFAULT, 'elliot', 'elliot@e.com', TRUE,
        'A brief follow up comment to the ticket',
        now(), 1);
INSERT INTO ticket_comment VALUES(DEFAULT, 'jojojoy', 'joestar@adv.biz', FALSE,
        'A brief follow up comment to the ticket',
        now(), 1);
