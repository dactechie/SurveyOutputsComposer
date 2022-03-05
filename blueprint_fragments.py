import json

special_program_blueprints = {
  'CoCo': 'CoCo', #blueprints/CoCo
  'Arcadia':''
}

assesment_clienttype_blueprints = {
  'ATOM Initial Assessment + ownuse': 'initial_assessment_ownuse',
  'ATOM Initial Assessment + othersuse': 'initial_assessment_othersuse',  
  'ATOM ITSP Review Assessment + ownuse': 'itsp_review_ownuse',
  'ATOM ITSP Review Assessment + othersuse': 'itsp_review_othersuse',
}


def get_docpaths_from_section(Sections, section_name):
  
  doc_path = Sections.get(section_name)
  if not doc_path:
    raise Exception("No document for section name")
  doc_filepath = f"{doc_path}/{section_name}.docx"
  return doc_filepath


def get_doc_fragments(blueprint):# -> List[str]:  
  
  doc_frag_paths = [get_docpaths_from_section(blueprint['_Sections'], section) 
                for section in blueprint['_Layout']['General'] ]  
  return doc_frag_paths


def get_fragpaths(blueprint_path):
  with open(blueprint_path) as jsonfile:
    blueprint = json.load(jsonfile)
    orderd_frag_filepaths = get_doc_fragments(blueprint)
    return orderd_frag_filepaths
  return None


def get_blueprint_type(survey_data):
  # Std. Initial Assesssment -> precompiled
  # Std. Initial Assessment -> from fragments (some questions not answered)
  # Special   -> E.g. Coco
  blueprint_folder = special_program_blueprints.get(survey_data['Program'], 'common')
  
  ass_cltyp_key = f"{survey_data['AssessmentType']} + {survey_data['ClientType']}"  
  blueprint_type = assesment_clienttype_blueprints.get(ass_cltyp_key)

  return blueprint_type, blueprint_folder



if __name__ == '__main__':
  # survey_data = {'Program':'TSS','AssessmentType':'ATOM Initial Assessment','ClientType':'ownuse'}
  # survey_data = {'Program':'TSS','AssessmentType':'ATOM ITSP Review Assessment','ClientType':'ownuse'}
  survey_data = {'Program':'TSS','AssessmentType':'ATOM ITSP Review Assessment','ClientType':'othersuse'}

  blueprint_type, blueprint_folder = get_blueprint_type(survey_data)
  if blueprint_type is not None and blueprint_folder is not None:
    bp_json = f"./blueprints/{blueprint_folder}/{blueprint_type}.json"
    ordered_file_paths = get_fragpaths(bp_json)
    print(ordered_file_paths) 
  else:
    print('Something went wrong')