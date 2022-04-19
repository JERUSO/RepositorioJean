CREATE DATABASE IF NOT EXISTS master_python;
use master_python;

CREATE TABLE usuarios (
    id int(25) auto_increment not null,
    nombre varchar(100),
    apellidos varchar(255),
    email varchar(255) not null,
    password varchar(255) not null,
    fecha   date not null,
    CONSTRAINT pk_usuarios PRIMARY KEY(id),
    CONSTRAINT uq_email UNIQUE(email)
) ENGINE=InnoDb;

CREATE TABLE notas (
    id int(25) autoincrement not null,
    usuario_id int(25) not null,
    titulo varchar(255) not null,
    descripcion text not null,
    fecha date not null,
    CONSTRAINT PK_NOTAS PRIMARY KEY(id),
    CONSTRAINT FK_NOTA_USUARIO FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
)ENGINE=InnoDb
