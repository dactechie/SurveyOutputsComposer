import json
from AssessmentObjects.AssessmentDefinitions import AssessmentMeta, get_meta_name

# to fully qualify a blueprint we need 3 pieces of infomration
# * Program  - Tied to funder
# * Assessment Type - one or more(1-*)  tied to the 1-* ROLEs within the program 
# * client type - own use vs others use vs Psych ref vs ...

# * /client_type / Assessment type / Program
#      /OwnUse
#         /INAS
#             /COMMON
#             /PSYACT         #not PsychRef
#         /ITSP
#         /SITK
#             /COCO
#         /POTA
#             /COCO
#
#     /OthersUse
#         /INAS
#         /ITSP
#
#     /PsychRef
#         /INAS
#         /ITSP
#         /POTA         //post-treatment assessment
#             PSYCHACT
#             PSYCHNSW
#         /PYND
#            /GOLBGNRL    # NOTE: not possible ? only PSYCHACT, PSYCHNSW
#            /COMMON
#
#
#          


special_program_blueprints = {
  'CoCo': 'Arcadia', #blueprints/CoCo
  'Arcadia':'Arcadia',
  'PSYNSW': 'Psychologist',
  'PSYACT': 'Psychologist',
}

# FEATURE_DEFINITIONS ={
#   'Common':{
#     'Physical' : []
#   }
# }
# in not specified in map, take common version, as dictated in the blueprint section
# ROLE_FEATURESET_MAP = {
#   'AOD_Counsellor' : ['Physical', 'Mental', 'EverydayLiving'],
#   'PrePostRehab': ['EverydayLiving']

# }
# BLPRNT_FEATURESET_MAPPING = {
#   'ACTAODCounsellor': ['AOD_Counsellor'],
#   'PrePostRehab' : [],

# }


# # used when fetching the documents(template fragments) to stitch
# DOCFLDRPRFIX_PROGRAM_ROLES_MAP = {
#   "TSS": "ACTCounsellor",
#   "SAPPHIRE": "NSWCounsellor",
#   "MONPATH": "NSWCounsellor",
#   "COCO": "PrePostRehab",
#   "ArcadiaHouse": "ResiRehab",
#   "ACTPsych": "Psychologist",
#   "NSWPsych": "Psychologist"
# }



class SurveyFragments:

  def __init__(self, survey_data, assessment_meta:AssessmentMeta):
    self.survey_data = survey_data
    self.assessment_meta = assessment_meta

  def get_blueprint_filepath(self):
    # Std. Initial Assesssment -> precompiled
    # Std. Initial Assessment -> from fragments (some questions not answered)
    # Special   -> E.g. Coco
    # blueprint_folder = special_program_blueprints.get(self.program, 'AODCounsellor')  
    
    # asstype_code = SURVEY_TYPE_MAP.get(f"{self.survey_data['AssessmentType']}") # InitialAssessment -> INAS
    # 
    # blueprint_file = f"{prog_map}_{asstype_code}_{self.survey_data['ClientType']}"
    meta_name = get_meta_name(self.assessment_meta)
    bp_json = f"blueprints/{meta_name}.json"
    return bp_json



  def get_docpaths_from_section(self, Sections, section_map:dict):
    vals = list(section_map.values())
    
    # { "SDS": "SDSIsAODUseOutOfControl" }, 
    # if survey data has a non-none answer to question :SDSIsAODUseOutOfControl, then add section from path
    if vals[0] == 1 or self.survey_data.get(vals[0]):
      section_key = list(section_map.keys())[0]
      doc_path = Sections.get(section_key)
      return doc_path

    return None
    # raise Exception("No document for section name")

  # @staticmethod
  # def get_docpaths_from_section(Sections, section_name):  
  #   doc_path = Sections.get(section_name)
  #   if not doc_path:
  #     raise Exception("No document for section name")
  #   doc_filepath = f"{doc_path}/{section_name}.docx"
  #   return doc_filepath

  def get_fragpaths(self, blueprint_path):
    with open(blueprint_path) as jsonfile:
      blueprint = json.load(jsonfile)
      orderd_frag_filepaths = [
                    self.get_docpaths_from_section(blueprint['_Sections'], section) 
                    for section in blueprint['_Layout']] 
      return orderd_frag_filepaths    


# if __name__ == '__main__':
#   survey_submission = {'Program':'TSS',
#                        'AssessmentType':'ITSPReview', 'SurveyData' : '{"ClientType":"othersuse"}'}
#   survey_submission['SurveyData'] = json.loads(survey_submission['SurveyData'])
#   assessment_meta = AssessmentMeta(survey_submission)
#   sf = SurveyFragments(survey_submission['SurveyData'], assessment_meta) 
#   bluep_json_path = sf.get_blueprint_filepath()
#   print(bluep_json_path)

  # survey_data = {'AssessmentType':'InitialAssessment','ClientType':'ownuse'}
  # sf = SurveyFragments(survey_data, program='GOLBGNRL') 
  # bluep_json_path = sf.get_blueprint_filepath()
  # ordered_fragments_paths = sf.get_fragpaths(bluep_json_path)
  # print(bluep_json_path)  