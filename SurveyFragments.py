import json

special_program_blueprints = {
  'CoCo': 'Arcadia', #blueprints/CoCo
  'Arcadia':'Arcadia'
}

assesment_clienttype_blueprints = {
  'ATOM Initial Assessment + ownuse': 'initial_assessment_ownuse',
  'ATOM Initial Assessment + othersuse': 'initial_assessment_othersuse',  
  'ATOM ITSP Review Assessment + ownuse': 'itsp_review_ownuse',
  'ATOM ITSP Review Assessment + othersuse': 'itsp_review_othersuse',

  'Arcadia Assessments + ownuse': 'arcadia_ownuse',
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

  def get_fragpaths(self, blueprint_path):
    with open(blueprint_path) as jsonfile:
      blueprint = json.load(jsonfile)
      orderd_frag_filepaths = [SurveyFragments.get_docpaths_from_section(blueprint['_Sections'], section) 
                  for section in blueprint['_Layout']['General'] ] 
      return orderd_frag_filepaths
    return None  
    


if __name__ == '__main__':
  survey_data = {'AssessmentType':'ATOM ITSP Review Assessment','ClientType':'othersuse'}
  sf = SurveyFragments(survey_data, program='TSS') 
  bp_json = sf.get_blueprint_filepath()
  print(bp_json)