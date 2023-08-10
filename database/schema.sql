CREATE TABLE student (
  id integer PRIMARY KEY,
  name varchar(255),
  email varchar(255),
  degree_program varchar(255),
  school varchar(255)
);

CREATE TABLE project (
  id integer PRIMARY KEY,
  name varchar(255),
  semester varchar(255),
  year integer,
  project_overview text,
  final_presentation varchar(255),
  award_id integer,
  skill_required_id integer,
  topic_id integer
);

CREATE TABLE project_has_student (
  project_id integer,
  student_id integer
);

CREATE TABLE advisor (
  id integer PRIMARY KEY,
  name varchar(255),
  email varchar(255),
  organization varchar(255),
  title varchar(255),
  primary_school varchar(255)
);

CREATE TABLE project_has_advisor (
  project_id integer,
  advisor_id integer
);

CREATE TABLE has_award (
  recipient_id integer,
  award integer
);

CREATE TABLE skill_or_software (
  id integer PRIMARY KEY,
  name varchar(255),
  type varchar(255)
);

CREATE TABLE topic (
  id integer PRIMARY KEY,
  name varchar(255)
);

ALTER TABLE has_award ADD FOREIGN KEY (recipient_id) REFERENCES project (award_id);

ALTER TABLE skill_or_software ADD FOREIGN KEY (id) REFERENCES project (skill_required_id);

ALTER TABLE topic ADD FOREIGN KEY (id) REFERENCES project (topic_id);

ALTER TABLE project_has_student ADD FOREIGN KEY (project_id) REFERENCES project (id);

ALTER TABLE project_has_student ADD FOREIGN KEY (student_id) REFERENCES student (id);

ALTER TABLE project_has_advisor ADD FOREIGN KEY (project_id) REFERENCES project (id);

ALTER TABLE project_has_advisor ADD FOREIGN KEY (advisor_id) REFERENCES advisor (id);

ALTER TABLE has_award ADD FOREIGN KEY (recipient_id) REFERENCES student (id);
