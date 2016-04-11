-- maintainer table dml
INSERT INTO maintainer VALUES (DEFAULT, 'admin', 'admin@admin.com', 'admin', TRUE);
INSERT INTO maintainer VALUES (DEFAULT, 'elliot', 'elliot@admin.com', 'pass', TRUE);
INSERT INTO maintainer VALUES (DEFAULT, 'james', 'james@email.com', 'pass', FALSE);


-- project table dml
INSERT INTO project VALUES (DEFAULT, 'CMS Project',
        'CMS issue tracker. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.',
        now(), now(), 1);
INSERT INTO project VALUES (DEFAULT, 'CRM Project',
        'CRM issue tracker. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.',
        now(), now(), 2);
INSERT INTO project VALUES (DEFAULT, 'Payment Portal Project',
        'Payment Portal issue tracker. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.',
        now(), now(), 3);


-- ticket table dml
INSERT INTO ticket VALUES (DEFAULT, 'andy', 'andy@example.com',
        'Cannot import from Word after update',
        'Ticket for CMS Project issue tracker and some rather involved description about the issue being experienced. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
        'low', 'open', now(), now(), 1);
INSERT INTO ticket VALUES (DEFAULT, 'arnold', 'arnold@example.com',
        'Crashes to desktop after resuming from standby',
        'Ticket for CMS Project issue tracker and some rather involved description about the issue being experienced. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
        'low', 'open', now(), now(), 1);
INSERT INTO ticket VALUES (DEFAULT, 'alex', 'alex@example.com',
        'Support for RTL languages',
        'Ticket for CMS Project issue tracker and some rather involved description about the issue being experienced. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
        'medium', 'open', now(), now(), 1);
INSERT INTO ticket VALUES (DEFAULT, 'bob', 'bob@example.com',
        'Settings are not saving properly after update',
        'Ticket for CMS Project issue tracker and some rather involved description about the issue being experienced. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
        'medium', 'open', now(), now(), 1);
INSERT INTO ticket VALUES (DEFAULT, 'babs', 'babs@example.com',
        'Client import hangs on Unicode characters',
        'Ticket for CMS Project issue tracker and some rather involved description about the issue being experienced. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
        'medium', 'open', now(), now(), 1);
INSERT INTO ticket VALUES (DEFAULT, 'bart', 'bart@example.com',
        'Is there a way to backup email lists',
        'Ticket for CMS Project issue tracker and some rather involved description about the issue being experienced. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
        'high', 'open', now(), now(), 1);

INSERT INTO ticket VALUES (DEFAULT, 'cara', 'cara@example.com',
        'Support for PayPal',
        'Ticket for Payment Portal Project issue tracker and some rather involved description about the issue being experienced. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
        'high', 'open', now(), now(), 2);
INSERT INTO ticket VALUES (DEFAULT, 'cat', 'cat@example.com',
        'Payment authorization timesout randomly',
        'Ticket for Payment Portal Project issue tracker and some rather involved description about the issue being experienced. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
        'low', 'open', now(), now(), 3);
INSERT INTO ticket VALUES (DEFAULT, 'cait', 'cait@example.com',
        'Log is slow to update',
        'Ticket for Payment Portal Project issue tracker and some rather involved description about the issue being experienced. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.',
        'high', 'open', now(), now(), 3);


-- ticket_comment table dml
INSERT INTO ticket_comment VALUES(DEFAULT, 'admin', 'admin@admin.com', TRUE,
        'A brief follow up comment to the ticket for the CMS Project. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
        now(), 1);
INSERT INTO ticket_comment VALUES(DEFAULT, 'abe', 'abe@example.com', FALSE,
        'A brief follow up comment to the ticket for the CMS Project. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
        now(), 1);
INSERT INTO ticket_comment VALUES(DEFAULT, 'alice', 'alice@example.com', TRUE,
        'A brief follow up comment to the ticket for the CMS Project. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
        now(), 1);
INSERT INTO ticket_comment VALUES(DEFAULT, 'ben', 'ben@email.com', FALSE,
        'A brief follow up comment to the ticket for the CRM Project. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
        now(), 7);
INSERT INTO ticket_comment VALUES(DEFAULT, 'carl', 'carl@example.com', FALSE,
        'A brief follow up comment to the ticket for the Payment Portal Project. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.',
        now(), 8);
