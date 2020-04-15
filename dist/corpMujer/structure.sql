
-- Tables

CREATE TABLE "barrios" (
	"idBarrio"	INTEGER NOT NULL,
	"nombre"	TEXT NOT NULL,
	"fkCiudad"	INTEGER NOT NULL,
	PRIMARY KEY("idBarrio"),
	FOREIGN KEY("fkCiudad") REFERENCES "ciudades"("idCiudad") ON UPDATE CASCADE
)

CREATE TABLE "beneficiarios" (
	"documento"	INTEGER NOT NULL UNIQUE,
	"nombres"	TEXT NOT NULL,
	"apellidos"	TEXT NOT NULL,
	"nacimiento"	TEXT NOT NULL,
	"fkNacionalidad"	INTEGER NOT NULL,
	"tipoDocumento"	TEXT NOT NULL,
	"fkCiudadExp"	INTEGER NOT NULL,
	"fkPais"	INTEGER NOT NULL,
	"fkDepartamento"	INTEGER NOT NULL,
	"fkCiudad"	INTEGER NOT NULL,
	"fkBarrio"	INTEGER NOT NULL,
	"entorno"	TEXT NOT NULL,
	"direccion"	TEXT NOT NULL,
	"sexo"	TEXT NOT NULL,
	"indicadorTelefonico"	INTEGER NOT NULL DEFAULT 0,
	"fijo"	INTEGER NOT NULL DEFAULT 0000000,
	"email"	INTEGER NOT NULL DEFAULT 'nan@nan.com',
	"genero"	TEXT NOT NULL,
	"etnia"	TEXT NOT NULL,
	"discapacidad"	TEXT NOT NULL,
	"tipo"	TEXT NOT NULL DEFAULT 'emprendedor',
	PRIMARY KEY("documento"),
	FOREIGN KEY("fkCiudad") REFERENCES "ciudades"("idCiudad") ON UPDATE CASCADE,
	FOREIGN KEY("fkPais") REFERENCES "paises"("idPais") ON UPDATE CASCADE,
	FOREIGN KEY("fkCiudadExp") REFERENCES "ciudades"("idCiudad") ON UPDATE CASCADE,
	FOREIGN KEY("fkNacionalidad") REFERENCES "paises"("idPais") ON UPDATE CASCADE,
	FOREIGN KEY("fkDepartamento") REFERENCES "departamentos"("idDepartamento") ON UPDATE CASCADE,
	FOREIGN KEY("fkBarrio") REFERENCES "barrios"("idBarrio") ON UPDATE CASCADE
)

CREATE TABLE "beneficiariosProyectos" (
	"idRelacion"	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	"fkProyecto"	INTEGER NOT NULL,
	"fkBeneficiario"	INTEGER NOT NULL,
	"estado"	INTEGER NOT NULL DEFAULT 1,
	FOREIGN KEY("fkProyecto") REFERENCES "proyectos"("idProyecto") ON UPDATE CASCADE,
	FOREIGN KEY("fkBeneficiario") REFERENCES "beneficiarios"("documento") ON UPDATE CASCADE
)

CREATE TABLE "celulares" (
	"celular"	INTEGER NOT NULL UNIQUE,
	"fkBeneficiario"	INTEGER NOT NULL,
	"tipo"	TEXT NOT NULL DEFAULT 'beneficiario',
	PRIMARY KEY("celular"),
	FOREIGN KEY("fkBeneficiario") REFERENCES "beneficiarios"("documento") ON UPDATE CASCADE
)

CREATE TABLE "ciudades" (
	"idCiudad"	INTEGER NOT NULL UNIQUE,
	"nombre"	TEXT NOT NULL,
	"fkDepartamento"	INTEGER NOT NULL,
	PRIMARY KEY("idCiudad"),
	FOREIGN KEY("fkDepartamento") REFERENCES "departamentos"("idDepartamento") ON UPDATE CASCADE
)

CREATE TABLE "departamentos" (
	"idDepartamento"	INTEGER NOT NULL UNIQUE,
	"nombre"	TEXT NOT NULL,
	"fkPais"	INTEGER NOT NULL,
	PRIMARY KEY("idDepartamento"),
	FOREIGN KEY("fkPais") REFERENCES "paises"("idPais") ON UPDATE CASCADE
)

CREATE TABLE "diagnosticoPerfilProductivo" (
	"fkBeneficiario"	INTEGER NOT NULL,
	"pregunta"	INTEGER NOT NULL,
	"respuesta"	INTEGER NOT NULL,
	FOREIGN KEY("fkBeneficiario") REFERENCES "beneficiarios"("documento") ON UPDATE CASCADE
)

CREATE TABLE "ideaNegocio" (
	"fkProyecto"	INTEGER NOT NULL,
	"fkBeneficiario"	INTEGER NOT NULL,
	"emprendimiento"	TEXT NOT NULL,
	"sectorEmpresarial"	TEXT NOT NULL,
	"CIIU"	INTEGER NOT NULL,
	"fkDepartamento"	INTEGER NOT NULL,
	"fkCiudad"	INTEGER NOT NULL,
	"surgeIdea"	TEXT NOT NULL,
	"tiempoDedicar"	TEXT NOT NULL,
	"estudiosTema"	TEXT NOT NULL,
	"experiencia"	TEXT NOT NULL,
	"productoServicio"	TEXT NOT NULL,
	"listaProductoServicio"	TEXT NOT NULL,
	"esAgropecuario"	TEXT NOT NULL DEFAULT 0,
	"portafolio"	TEXT NOT NULL,
	"inversionActivos"	INTEGER NOT NULL,
	"inversionInicial"	INTEGER NOT NULL,
	"porcentajeInicial"	TEXT NOT NULL,
	"inversionCapital"	INTEGER NOT NULL,
	"ventasPrimerMes"	INTEGER NOT NULL,
	"ventasPrimerAño"	INTEGER NOT NULL,
	"necesitaColaboradores"	TEXT NOT NULL,
	"quienesColaboradores"	TEXT NOT NULL,
	"tiempoSemanal"	TEXT NOT NULL,
	"porQueNoEmpezaba"	TEXT NOT NULL,
	"mesesNegocio"	INTEGER NOT NULL,
	"imaginaNegocio"	TEXT NOT NULL,
	FOREIGN KEY("fkProyecto") REFERENCES "proyectos"("idProyecto") ON UPDATE CASCADE,
	FOREIGN KEY("fkDepartamento") REFERENCES "departamentos"("idDepartamento") ON UPDATE CASCADE,
	FOREIGN KEY("fkCiudad") REFERENCES "ciudades"("idCiudad") ON UPDATE CASCADE,
	FOREIGN KEY("fkBeneficiario") REFERENCES "beneficiarios"("documento") ON UPDATE CASCADE
)

CREATE TABLE "operarios" (
	"nombre"	TEXT NOT NULL,
	"documento"	INTEGER NOT NULL UNIQUE,
	"username"	TEXT NOT NULL UNIQUE,
	"password"	TEXT NOT NULL,
	"tipo"	INTEGER NOT NULL DEFAULT 0,
	PRIMARY KEY("documento")
)

CREATE TABLE "operariosProyectos" (
	"fkOperario"	TEXT NOT NULL,
	"fkProyecto"	INTEGER NOT NULL,
	FOREIGN KEY("fkOperario") REFERENCES "operarios"("username") ON UPDATE CASCADE,
	FOREIGN KEY("fkProyecto") REFERENCES "proyectos"("idProyecto") ON UPDATE CASCADE
)

CREATE TABLE "paises" (
	"idPais"	INTEGER NOT NULL UNIQUE,
	"nombre"	TEXT NOT NULL UNIQUE,
	PRIMARY KEY("idPais")
)

CREATE TABLE "proyectos" (
	"idProyecto"	INTEGER NOT NULL UNIQUE,
	"nombre"	TEXT NOT NULL,
	"creacion"	TEXT NOT NULL DEFAULT '01/01/2000',
	PRIMARY KEY("idProyecto")
)

CREATE TABLE "unidadNegocio" (
	"fkProyecto"	INTEGER NOT NULL,
	"fkBeneficiario"	INTEGER NOT NULL,
	"unidad"	TEXT NOT NULL,
	"fkDepartamento"	INTEGER NOT NULL,
	"fkCiudad"	INTEGER NOT NULL,
	"cantidadSocios"	INTEGER NOT NULL DEFAULT 0,
	"direccion"	TEXT NOT NULL,
	"CIIU"	INTEGER NOT NULL,
	"indicadorTel"	INTEGER NOT NULL DEFAULT 0,
	"telefonoFijo"	INTEGER NOT NULL DEFAULT 0000000,
	"correoElectronico"	TEXT NOT NULL DEFAULT 'nan@nan.com',
	"paginaWeb"	TEXT,
	"descripcion"	TEXT NOT NULL,
	"portafolio"	TEXT NOT NULL,
	"creacion"	TEXT NOT NULL,
	"nit"	TEXT NOT NULL,
	"descripcionPasivos"	TEXT NOT NULL,
	"camaraComercio"	INTEGER NOT NULL DEFAULT 0,
	"colaboradorContrato"	INTEGER NOT NULL DEFAULT 0,
	"colaboradorSinContrato"	INTEGER NOT NULL DEFAULT 0,
	FOREIGN KEY("fkProyecto") REFERENCES "proyectos"("idProyecto") ON UPDATE CASCADE,
	FOREIGN KEY("fkBeneficiario") REFERENCES "beneficiarios"("documento") ON UPDATE CASCADE,
	FOREIGN KEY("fkDepartamento") REFERENCES "departamentos"("idDepartamento") ON UPDATE CASCADE,
	FOREIGN KEY("fkCiudad") REFERENCES "ciudades"("idCiudad") ON UPDATE CASCADE
)


-- Views

CREATE VIEW 'Login' AS
  SELECT 'username', 'password'
  FROM 'operarios'


--Indexes

CREATE INDEX "beneficiarioProyectoIdea" ON "ideaNegocio" (
	"fkBeneficiario",
	"fkProyecto"
)

CREATE INDEX "beneficiarioProyectoUnidad" ON "unidadNegocio" (
	"fkBeneficiario",
	"fkProyecto"
)


-- Querys

INSERT INTO 'ciudades'('idCiudad', 'nombre', 'fkDepartamento')
SELECT 'codigo_ciudad_dian', 'ciudad', 'fk_codigo_departamento_dian'
FROM 'BaseDeDatos'.'ciudades'
WHERE 'fk_codigo_departamento_dian' NOT IN (100, 10);


INSERT INTO 'barrios'('idBarrio', 'nombre', 'fkCiudad')
SELECT 'codigo_barrio_dian', 'barrio', 'fk_codigo_ciudad_dian'
FROM 'BaseDeDatos'.'barrios'
WHERE 'codigo_barrio_dian' NOT IN (
    SELECT
        'codigo_barrio_dian'
    FROM
        'BaseDeDatos'.'barrios'
    GROUP BY
        'codigo_barrio_dian'
    HAVING 
        COUNT(*) > 1
) AND 'fk_codigo_ciudad_dian' IN (
    SELECT 'idCiudad' FROM 'ciudades'
);

INSERT INTO 'preguntasDiagnostico'('idPregunta', 'pregunta')
SELECT 'pregunta_id', 'pregunta'
FROM 'BaseDeDatos'.'preguntasDiagnostico';