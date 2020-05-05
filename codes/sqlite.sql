-- Attachment querys from legacy database

INSERT INTO countries  SELECT * FROM datos.paises

INSERT INTO departments SELECT * FROM datos.departamentos

INSERT INTO cities SELECT * FROM datos.ciudades

INSERT INTO neighborhoods SELECT * FROM datos.barrios

INSERT INTO ciiu SELECT * FROM datos.cIIU

INSERT INTO diagnosticQuestions SELECT * FROM datos.preguntasDiagnostico

sqlcmd -S 190.145.94.91 -U Arnulforojas -P 'Arojas032020'
USE CMM_Prueba;

SELECT names, lastNames FROM payee;
