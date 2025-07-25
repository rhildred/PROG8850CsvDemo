create table subscriber (
    id int not null  AUTO_INCREMENT,
    name varchar(100) not null,
    email varchar(100) not null,
    sign_up_date DATE DEFAULT (CURRENT_DATE()),
    interests varchar(255),
    PRIMARY KEY (ID)
);