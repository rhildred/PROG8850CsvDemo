ALTER TABLE subscriber
ADD CONSTRAINT uc_email UNIQUE (email);