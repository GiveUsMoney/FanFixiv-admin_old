from src.config import config

from sqlalchemy import create_engine
from sqlalchemy.exc import ProgrammingError

engine = create_engine(
    config.DB_URI,
)

main_sql = """
CREATE TYPE "public"."tb_tag_type_enum" AS ENUM('0', '1', '2', '3', '4', '5')
CREATE TYPE "public"."tb_tag_extra_tag_enum" AS ENUM('0', '1')
CREATE TYPE "public"."tb_content_source_type_enum" AS ENUM('0', '1')
CREATE TABLE "tb_likes" ("seq" SERIAL NOT NULL, "created_at" TIMESTAMP NOT NULL DEFAULT now(), "updated_at" TIMESTAMP NOT NULL DEFAULT now(), "user_seq" integer NOT NULL, "content_seq" integer, CONSTRAINT "PK_e076eba140b8c23597daa2a093a" PRIMARY KEY ("seq"));
CREATE TABLE "tb_series" ("seq" SERIAL NOT NULL, "created_at" TIMESTAMP NOT NULL DEFAULT now(), "updated_at" TIMESTAMP NOT NULL DEFAULT now(), "title" character varying NOT NULL, CONSTRAINT "PK_47edf8d1abd7e6ff4d766b0ce8e" PRIMARY KEY ("seq"));
CREATE TABLE "tb_artist_profile" ("seq" SERIAL NOT NULL, "created_at" TIMESTAMP NOT NULL DEFAULT now(), "updated_at" TIMESTAMP NOT NULL DEFAULT now(), "artist_profile" character varying NOT NULL, "tag_seq" integer, CONSTRAINT "UQ_008a8d25f9f412f90376df04f46" UNIQUE ("artist_profile"), CONSTRAINT "PK_94e66f6d7324bc30d0b9cea59f0" PRIMARY KEY ("seq"));
SELECT "n"."nspname", "t"."typname" FROM "pg_type" "t" INNER JOIN "pg_namespace" "n" ON "n"."oid" = "t"."typnamespace" WHERE "n"."nspname" = 'public' AND "t"."typname" = 'tb_tag_type_enum';
SELECT "n"."nspname", "t"."typname" FROM "pg_type" "t" INNER JOIN "pg_namespace" "n" ON "n"."oid" = "t"."typnamespace" WHERE "n"."nspname" = 'public' AND "t"."typname" = 'tb_tag_extra_tag_enum';
CREATE TABLE "tb_tag" ("seq" SERIAL NOT NULL, "created_at" TIMESTAMP NOT NULL DEFAULT now(), "updated_at" TIMESTAMP NOT NULL DEFAULT now(), "type" "public"."tb_tag_type_enum" NOT NULL, "name" character varying NOT NULL, "description" character varying NOT NULL, "requester" integer, "status" boolean NOT NULL DEFAULT false, "is_adult" boolean NOT NULL DEFAULT false, "extra_tag" "public"."tb_tag_extra_tag_enum", CONSTRAINT "UQ_8bc3d5fb9ebfd2406ebf7e8a542" UNIQUE ("name"), CONSTRAINT "PK_0b2a9e87453c8c5596ceb4fcdde" PRIMARY KEY ("seq"));
CREATE TABLE "tb_type_name" ("seq" SERIAL NOT NULL, "created_at" TIMESTAMP NOT NULL DEFAULT now(), "updated_at" TIMESTAMP NOT NULL DEFAULT now(), "type_seq" character varying NOT NULL, "type_name" character varying NOT NULL, CONSTRAINT "PK_1f664bd3d7b3a34b13699d15aa3" PRIMARY KEY ("seq"));
CREATE TABLE "tb_content" ("seq" SERIAL NOT NULL, "created_at" TIMESTAMP NOT NULL DEFAULT now(), "updated_at" TIMESTAMP NOT NULL DEFAULT now(), "title" character varying NOT NULL, "thumbnail" character varying NOT NULL, "uploader_seq" integer NOT NULL, "translate_review" character varying NOT NULL, "is_adult" boolean NOT NULL DEFAULT false, "status" boolean NOT NULL, "like" integer, "do_like" boolean, "artist_seq" integer, "series_seq" integer, CONSTRAINT "PK_1d4204c2f36b681875efc1dab2a" PRIMARY KEY ("seq"));
SELECT "n"."nspname", "t"."typname" FROM "pg_type" "t" INNER JOIN "pg_namespace" "n" ON "n"."oid" = "t"."typnamespace" WHERE "n"."nspname" = 'public' AND "t"."typname" = 'tb_content_source_type_enum';
CREATE TABLE "tb_content_source" ("seq" SERIAL NOT NULL, "created_at" TIMESTAMP NOT NULL DEFAULT now(), "updated_at" TIMESTAMP NOT NULL DEFAULT now(), "type" "public"."tb_content_source_type_enum" NOT NULL, "link" character varying NOT NULL, "content_seq" integer, CONSTRAINT "PK_85dbf697b1ad65f1d4e876b4c29" PRIMARY KEY ("seq"));
CREATE TABLE "tb_content_tag_reg" ("content_seq" integer NOT NULL, "tag_seq" integer NOT NULL, CONSTRAINT "PK_1fcdb66b607970e848856c05d6b" PRIMARY KEY ("content_seq", "tag_seq"));
CREATE INDEX "IDX_23ae201542dc17db75a56f699a" ON "tb_content_tag_reg" ("content_seq") ;
CREATE INDEX "IDX_66b52612f93ab08fd5a34f1c4a" ON "tb_content_tag_reg" ("tag_seq");
ALTER TABLE "tb_likes" ADD CONSTRAINT "FK_2e837c22e439034286d06084f36" FOREIGN KEY ("content_seq") REFERENCES "tb_content"("seq") ON DELETE CASCADE ON UPDATE NO ACTION;
ALTER TABLE "tb_artist_profile" ADD CONSTRAINT "FK_85674377c575658fbd2e414033c" FOREIGN KEY ("tag_seq") REFERENCES "tb_tag"("seq") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "tb_content" ADD CONSTRAINT "FK_9ef1e0046a1fc659900d302d0b4" FOREIGN KEY ("artist_seq") REFERENCES "tb_tag"("seq") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "tb_content" ADD CONSTRAINT "FK_02531d9dfa3e7223ae82de9799d" FOREIGN KEY ("series_seq") REFERENCES "tb_series"("seq") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "tb_content_source" ADD CONSTRAINT "FK_3d9815ff6e39cecb9996ae23227" FOREIGN KEY ("content_seq") REFERENCES "tb_content"("seq") ON DELETE NO ACTION ON UPDATE NO ACTION;
ALTER TABLE "tb_content_tag_reg" ADD CONSTRAINT "FK_23ae201542dc17db75a56f699aa" FOREIGN KEY ("content_seq") REFERENCES "tb_content"("seq") ON DELETE CASCADE ON UPDATE CASCADE;
ALTER TABLE "tb_content_tag_reg" ADD CONSTRAINT "FK_66b52612f93ab08fd5a34f1c4ad" FOREIGN KEY ("tag_seq") REFERENCES "tb_tag"("seq") ON DELETE CASCADE ON UPDATE CASCADE;
"""

user_sql = """
create table tb_notice (
seq bigint not null,
created_at timestamp not null,
updated_at timestamp not null,
checked boolean default false,
content varchar(255),
to_all boolean,
user_seq bigint,
primary key (seq)
);
create table tb_profile (
seq bigint not null,
created_at timestamp not null,
updated_at timestamp not null,
birth date,
descript varchar(255),
is_tr boolean default false,
nickname varchar(255),
nn_md_date timestamp default now(),
profile_img varchar(255),
primary key (seq)
);
create table tb_role (
seq bigint not null,
created_at timestamp not null,
updated_at timestamp not null,
role varchar(255) default 'ROLE_USER',
user_seq bigint,
primary key (seq)
);
create table tb_secession (
seq bigint not null,
created_at timestamp not null,
updated_at timestamp not null,
email varchar(255),
sec_date date,
primary key (seq)
);
create table tb_user (
seq bigint not null,
created_at timestamp not null,
updated_at timestamp not null,
email varchar(255),
is_social boolean,
pw varchar(255),
profile_seq bigint,
primary key (seq)
);
alter table tb_notice
add constraint FKtkai02rahnsqb600pqf9036yt
foreign key (user_seq)
references tb_user;
alter table tb_role
add constraint FKarmjjjrylmm48m6yrkt307t28
foreign key (user_seq)
references tb_user;
alter table tb_user
add constraint FK1169u36ssvjc9hy07m8oi0bu6
foreign key (profile_seq)
references tb_profile;
"""

with engine.connect() as con:
    for i in main_sql.split('\n'):
        if len(i.strip()) < 1: continue
        try:
            con.execute(i)
        except ProgrammingError as e:
            continue

    for i in user_sql.split(';'):
        if len(i.strip()) < 1: continue
        try:
            con.execute(i)
        except ProgrammingError as e:
            continue