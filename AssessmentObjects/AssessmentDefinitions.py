# import json
from constants import SURVEY_TYPE_MAP, BLPRNT_PROGRAM_MAPPING
# from abc import ABC, abstractmethod

from collections import namedtuple

AssessmentMeta = namedtuple('AssessmentMeta', "SLK AssessmentType Program ClientType")


def get_assessment_meta(survey_submission:dict):
  return AssessmentMeta(
    SLK = survey_submission['PartitionKey'],
    AssessmentType = SURVEY_TYPE_MAP.get(f"{survey_submission['AssessmentType']}"),
    Program = survey_submission['Program'],
    ClientType = survey_submission['SurveyData']['ClientType']
  )

# class AssessmentMeta:
#   def __init__(self, survey_data:dict):
#     self.SLK = survey_data['PartitionKey']
#     self.assessment_type = SURVEY_TYPE_MAP.get(f"{survey_data['AssessmentType']}")
#     self.program = survey_data['Program']
#     self.client_type = survey_data['SurveyData']['ClientType']
    
def get_meta_name(meta:AssessmentMeta):
  prog_map = BLPRNT_PROGRAM_MAPPING.get(f"{meta.Program}") # TSS -> ACT/AODCounsellor
  return f"{prog_map}_{meta.AssessmentType}_{meta.ClientType}"

# class AssessmentBase:
#   def __init__(self, survey_submission):  
#     self.survey_submission = survey_submission
#     self.survey_data = json.loads(survey_submission['SurveyData'])
#     self.assessment_date = survey_submission['AssessmentDate']
#     self.assessment_type = survey_submission['AssessmentType']
#     self.client_type = survey_submission['ClientType']
#     self.program = survey_submission['Program']

# class FeatureFactoryBase(ABC):
#   @abstractmethod
#   def get_feature(self):
#     pass

# class AssessmentFeature(ABC):
#   @abstractmethod
#   def get_feature(self):
#     pass


# class DrugOfConcern(AssessmentFeature):
#   def __init__(self, pdc):
#     self.substance = pdc['PDCSubstanceOrGambling']
#     self.daysinlast28 = pdc['PDCDaysInLast28']
#     self.units = pdc['PDCUnits']
#     self.methodofuse = pdc['PDCMethodOfUse']
#     self.howmuchperoccasion = pdc['PDCHowMuchPerOccasion']
  
#   def get_feature(self):
#     return self


# class DrugOfConcernFactory(FeatureFactoryBase):
#   def __init__(self, pdc):
#     self.pdc = pdc

#   def get_feature(self) -> AssessmentFeature:
#     return DrugOfConcern(self.pdc)

# assessment_feature_keys = {
#   'AOD_INAS_ownuse': {
#     'PDC': DrugOfConcern
#   } 
  
# } 




#     # self.agefirstused = pdc['PDCAgeFirstUsed']
#     # self.agelastused = pdc['PDCAgeLastUsed']
#     # self.goals = pdc['PDCGoals']
 
#     # self.impact_on_life = pdc['PDCImpactOnLife']
#     # self.impact_on_health = pdc['PDCImpactOnHealth']
#     # self.impact_on_work = pdc['PDCImpactOnWork']
#     # self.impact_on_family = pdc['PDCImpactOnFamily']
#     # self.impact_on_friends = pdc['PDCImpactOnFriends']
#     # self.impact_on_legal = pdc['PDCImpactOnLegal']
#     # self.impact_on_financial = pdc['PDCImpactOnFinancial']

# class InitialAssessment(AssessmentBase):
  
#   def __init__(self, survey_submission):
#     super().__init__(survey_submission)
#     self.pdc = DrugOfConcern(self.survey_data['PDC'][0])


  