sqlcmd -S 190.145.94.91 -U Arnulforojas -P 'Arojas032020'
USE CMMCRSocial;

SELECT names, lastNames FROM payee;
DELETE FROM payee;

SELECT id FROM payeeProjects;
DELETE FROM payeeProjects;

SELECT payeeDocument FROM productionProfileDiag;
DELETE FROM productionProfileDiag;



sqlcmd -S 190.145.94.92 -d CMMCRSocial -U API -P Api*2020*


ALTER TABLE informacion_general_beneficiario ALTER COLUMN cellphone bigint;


sqlcmd -S 190.145.94.92 -d CMMCRSocial -U Arnulforojas -P Arojas032020

python -m PyInstaller --name cmm_app --icon C:\Users\drarn\Documents\Documents\Dev\cmm\compilacion_windows\windows_app_icon.ico C:\Users\drarn\Documents\Documents\Dev\cmm\corpMundialMujer\main.py
