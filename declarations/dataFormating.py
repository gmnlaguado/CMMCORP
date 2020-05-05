# coding=utf-8
import datetime
from declarations import querys
from codes import snippets


def GeneralInformationData(information):
    org = [
        information.project,  # 0
        information.id_name.text,  # 1
        information.id_lastName.text,  # 2
        information.id_documentType.text,  # 3
        information.payeeDocument,  # 4
        information.id_expeditionCity.text,  # 5
        information.id_birthdate.text,  # 6
        information.id_cities.text,  # 7
        information.id_departments.text,  # 8
        information.id_country.text,  # 9
        information.id_sign.text,  # 10
        information.id_address.text,  # 11
        information.id_neighborhoods.text,  # 12
        'information.Indicative.text',  # 13
        information.id_telephone.text,  # 14
        information.id_cellphone.text,  # 15
        information.id_email.text,  # 16
        information.operator,  # 17
        information.id_cellphone2.text,  # 18
        information.id_payeeType.text,  # 19
        'information.DateToday.text',  # 20
        information.id_ageRange.text,  # 21
        information.id_nationality.text,  # 22
        information.id_environment.text,  # 23
        information.id_tier.text,  # 24
        information.id_sex.text,  # 25
        information.id_gender.text,  # 26
        information.id_ethnicGroup.text,  # 27
        information.id_disability.text  # 28
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
    for oo in org:
        print(oo)
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


def productionProfileDiagData(info):
    info = tuple(info)
    querys.loadProductionProfileDiag(info)


def bussinesIdeaData(info):
    org = [
        info.project,  # 0
        info.payeeDocument,  # 1
        info.operator,  # 2
        info.id_entrepreneurship.text,  # 3
        info.id_bussinesSector.text,  # 4
        info.id_ciiu.text,  # 5
        info.id_departments.text,  # 6
        info.id_cities.text,  # 7
        info.id_howArise.text,  # 8
        info.id_dedicationTime.text,  # 9
        info.id_studies.text,  # 10
        info.id_haveExperience.text,  # 11
        info.id_productServices.text,  # 12
        info.productServicesList,  # 13
        info.id_agricultural.text,  # 14
        info.id_briefcase.text,  # 15
        info.id_assetInvestment.text,  # 16
        info.id_initialInvestment.text,  # 17
        info.id_investmentPercent.text,  # 18
        info.id_capitalWorkInvestment.text,  # 19
        info.id_firstMonthSales.text,  # 20
        info.id_firstYearSales.text,  # 21
        info.id_needColabs.text,  # 22
        info.colaboratorsList,  # 23
        info.id_weeklyTime.text,  # 24
        info.id_whyNot.text,  # 25
        info.id_months.text,  # 26
        info.id_imagine.text,  # 27
        'date'  # 28
    ]
    org[0] = querys.idProject(org[0].lower())
    org[4] = querys.idParametrics('businessSector', org[4])
    org[5] = querys.idParametrics('ciiu', org[5])
    org[6] = querys.idParametrics('departments', org[6])
    org[7] = querys.idParametrics('cities', org[7])
    org[8] = querys.idParametrics('howArise', org[8])
    org[9] = querys.idParametrics('dedicationTime', org[9])
    org[10] = querys.idParametrics('studies', org[10])
    org[11] = querys.idParametrics('yesNo', org[11])
    org[12] = querys.idParametrics('productServices', org[12])
    org[14] = querys.idParametrics('yesNo', org[14])
    org[16] = float(org[16])
    org[17] = float(org[17])
    org[18] = querys.idParametrics('inversionPercentage', org[18])
    org[19] = float(org[19])
    org[20] = float(org[20])
    org[21] = float(org[21])
    org[22] = querys.idParametrics('yesNo', org[22])
    if org[23] is None:
        org[23] = ""
    org[24] = querys.idParametrics('weeklyTime', org[24])
    org[25] = querys.idParametrics('whyNot', org[25])
    org[26] = int(org[26])
    org[28] = str(datetime.date.today())

    org = tuple(org)
    querys.loadBussinesIdea(org)


def bussinesUnitData(info):
    org = [
        info.project,                                       # 0
        info.payeeDocument,                                 # 1
        info.operator,                                      # 2
        info.id_unit.text,                                  # 3
        info.id_departments.text,                           # 4
        info.id_cities.text,                                # 5
        info.id_howManyPartners.text,                       # 6
        info.id_sign.text,                                  # 7
        info.id_address.text,                               # 8
        info.id_ciiu.text,                                  # 9
        "info.id_indicator.text",                           # 10
        info.id_phone.text,                                 # 11
        info.id_email.text,                                 # 12
        info.id_webPage.text,                               # 13
        info.id_description.text,                           # 14
        info.id_briefcase.text,                             # 15
        info.id_creation.text,                              # 16
        info.id_nit.text,                                   # 17
        info.id_liabilitiesDescription.text,                # 18
        info.id_regCamara.text,                             # 19
        info.id_withContract.text,                          # 20
        info.id_withoutContract.text,                       # 21
        info.id_cellphone.text,                             # 22
        info.id_cellphone2.text,                            # 23
        info.id_tier.text,                                  # 24
        "date"                                              # 25
    ]

    org[0] = querys.idProject(org[0].lower())
    org[4] = querys.idParametrics('departments', org[4])
    org[5] = querys.idParametrics('cities', org[5])
    org[6] = int(org[6])
    org[7] = querys.idParametrics('sign', org[7])
    org[9] = querys.idParametrics('ciiu', org[9])
    org[10] = querys.indicator(org[4])
    org[11] = int(org[11])
    org[16] = snippets.formattingDate(org[16])
    org[19] = querys.idParametrics('yesNo', org[19])
    org[20] = int(org[20])
    org[21] = int(org[21])
    org[22] = int(org[22])
    org[23] = int(org[23])
    org[24] = int(org[24])
    org[25] = str(datetime.date.today())

    org = tuple(org)
    querys.loadBussinesUnit(org)
