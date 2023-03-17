import json

# from collections import namedtuple
# Program = namedtuple('Program',field_names=['code', 'name', 'assessmemt_types'
#                                             ])

# coco = Program('COCO', 'Arcadia Continuum of Care', ['Supplemental Intake Assessment', 'Post-Treatment Assessment'])
# resi = Program('ARCA', 'Arcadia Residential Rehab', ['ITSP Review Assessment'])

special_program_blueprints = {
  'COCO': 'Arcadia', #blueprints/CoCo
  'Arcadia':'Arcadia',
  'PSYNSW': 'Psychologist',
  'PSYACT': 'Psychologist',
}


assesment_clienttype_blueprints = {
  'ATOM Initial Assessment + ownuse': 'initial_assessment_ownuse',
  'ATOM Initial Assessment + othersuse': 'initial_assessment_othersuse',  
  'ATOM ITSP Review Assessment + ownuse': 'itsp_review_ownuse',
  'ATOM ITSP Review Assessment + othersuse': 'itsp_review_othersuse',
  
  # 'Arcadia Assessments + ownuse': 'arcadia_ownuse', # NOTE 'Arcadai Assessments is not an asses type
  'ATOM Initial Assessment + PsychiatristReferral': 'initial_assessment_psychref'

}


class SurveyFragments:

  def __init__(self, survey_data, program):
    self.survey_data = survey_data
    self.program = program

  def get_blueprint_filepath(self):
    # Std. Initial Assesssment -> precompiled
    # Std. Initial Assessment -> from fragments (some questions not answered)
    # Special   -> E.g. Coco
    blueprint_folder = special_program_blueprints.get(self.program, 'common')  
    ass_cltyp_key = f"{self.survey_data['AssessmentType']} + {self.survey_data['ClientType']}"  
    blueprint_type = assesment_clienttype_blueprints.get(ass_cltyp_key)
    if blueprint_type and blueprint_folder:
      bp_json = f"./blueprints/{blueprint_folder}/{blueprint_type}.json"
      return bp_json
    return None

  @staticmethod
  def get_docpaths_from_section(Sections, section_name):  
    doc_path = Sections.get(section_name)
    if not doc_path:
      raise Exception("No document for section name")
    doc_filepath = f"{doc_path}/{section_name}.docx"
    return doc_filepath
  

  def get_sections_in_data(self, blueprint, conditions)-> list:    
      # if the data has a question from the section then we show the section in the document
    sections = [ section for section in blueprint['_Layout']['General'] 
                  if section not in conditions 
                  or conditions[section]['Question'] in self.survey_data
                ]
    return sections


  def get_fragpaths(self, blueprint_path):
    with open(blueprint_path) as jsonfile:
      blueprint = json.load(jsonfile)
      conditions = blueprint.get("_Conditions")
      orderd_frag_filepaths = [SurveyFragments.get_docpaths_from_section(blueprint['_Sections'], section) 
                  for section in self.get_sections_in_data(blueprint, conditions)
                  ] 
      return orderd_frag_filepaths
    


if __name__ == '__main__':
  survey_data = {'AssessmentType':'ATOM ITSP Review Assessment','ClientType':'othersuse'}
  sf = SurveyFragments(survey_data, program='TSS') 
  bp_json = sf.get_blueprint_filepath()
  print(bp_json)