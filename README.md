# Note
Run Sql script to create the accountFb table in AccountDB.db(allocate in folder resource) A if it doesn't exist.
CREATE TABLE accountFb(
                        uid TEXT PRIMARY KEY,
                        password TEXT NOT NULL,
                        code2fa TEXT,
                        bank TEXT
                       )
