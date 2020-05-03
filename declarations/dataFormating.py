# coding=utf-8
import datetime
from declarations import querys
from codes import snippets


def GeneralInformationData(information):
    org = [
        information.project,                        # 0
        information.id_name.text,                   # 1
        information.id_lastName.text,               # 2
        information.id_documentType.text,           # 3
        information.payeeDocument,                  # 4
        information.id_expeditionCity.text,         # 5
        information.id_birthdate.text,              # 6
        information.id_cities.text,                 # 7
        information.id_departments.text,            # 8
        information.id_country.text,                # 9
        information.id_sign.text,                   # 10
        information.id_address.text,                # 11
        information.id_neighborhoods.text,          # 12
        'information.Indicative.text',              # 13
        information.id_telephone.text,              # 14
        information.id_cellphone.text,              # 15
        information.id_email.text,                  # 16
        information.operator,                       # 17
        information.id_cellphone2.text,             # 18
        information.id_payeeType.text,              # 19
        'information.DateToday.text',               # 20
        information.id_ageRange.text,               # 21
        information.id_nationality.text,            # 22
        information.id_environment.text,            # 23
        information.id_tier.text,                   # 24
        information.id_sex.text,                    # 25
        information.id_gender.text,                 # 26
        information.id_ethnicGroup.text,            # 27
        information.id_disability.text              # 28
    ]
    # Normalizing
    org[0] = querys.idProject(org[0].lower())
    org[3] = querys.idParametrics('documentType', org[3])
    org[5] = querys.idParametrics('cities', org[5])
    org[6] = snippets.formattingDate(org[6])
    org[7] = querys.idParametrics('cities', org[7])
    org[8] = querys.idParametrics('departments', org[8])
    org[9] = querys.idParametrics('countries', org[9])
    org[10] = querys.idParametrics('sign', org[10])
    org[12] = querys.idParametrics('neighborhoods', org[12].upper())
    org[13] = querys.indicator(org[8])
    org[14] = int(org[14])
    org[15] = int(org[15])
    org[18] = int(org[18])
    org[19] = querys.idParametrics('payeeType', org[19])
    org[20] = str(datetime.date.today())
    org[21] = querys.idParametrics('ageRange', org[21])
    org[22] = querys.idParametrics('countries', org[22])
    org[23] = querys.idParametrics('environment', org[23])
    org[24] = int(org[24])
    org[25] = querys.idParametrics('sex', org[25])
    org[26] = querys.idParametrics('gender', org[26])
    org[27] = querys.idParametrics('ethnicGroup', org[27])
    org[28] = querys.idParametrics('disability', org[28])

    org = tuple(org)
    querys.loadPayee(org)

    pro = [
        org[0],
        org[17],
        org[4],
        org[20],
        1
    ]
    payeeProjectsData(pro, True)


def payeeProjectsData(info, clean):
    if clean:
        info = tuple(info)
        querys.loadPayeeProjects(info)







