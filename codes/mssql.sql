sqlcmd -S 190.145.94.91 -U Arnulforojas -P 'Arojas032020'
USE CMMCRSocial;

SELECT names, lastNames FROM payee;
DELETE FROM payee;

SELECT id FROM payeeProjects;
DELETE FROM payeeProjects;

SELECT payeeDocument FROM productionProfileDiag;
DELETE FROM productionProfileDiag;
