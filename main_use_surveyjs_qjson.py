
import json

# survey_keys = {
#   ClientType: 'ClientType'
# }
# assessment_type :{
#   'InitialAssessment'
# }


# 'if field is present in the submission, show the entire section in the questionnaire'
question_display_groups = {
  'AssessmentDate': 'Intro'
}

def get_json_data(file_path:str) -> dict:
  with open(file_path, 'r') as jsonfile:
    survey_data = json.load(jsonfile)
    return survey_data

  
def get_survey_questionnaire(assessment_type:str):
  qstnr_filepath = f"./Files/SurveyJSQuestionnaires/{assessment_type.replace(' ', '_')}.json"
  qstionr = get_json_data(qstnr_filepath)
  return qstionr


# def compile_answer_doc(survey_questionnaire:dict, survey_data:dict):
#   #show K10 section only if done
#   # bp = get_blueprint_type()
#   bp_clienttype = survey_data.get('ClientType')
#   get_meta_header()
#   build_template_from_bp_data()
  
#   return None

#  "title": "Main Substance of Concern / Gambling",
#           "columns": [
#             {
#               "name": "PDCSubstanceOrGambling",
#               "title": "Drug of concern/Gambling",
#               "cellType": "dropdown",
#               "isRequired": true,
#               "choices": [
#                 {
#                   "value": "Ethanol",
#                   "text": "Alcohol (Ethanol)"
#                 },
#               "MDMA"

question_types_with_possible_translations = [  "dropdown", "radiogroup", "checkbox"]

# {
#   ...
#   "Program": [
#        {"value":"Sapphire", "text":"Sapphire Health & Wellbeing Service"}
#        {"value":"EUROPATH", "text":"Pathways Eurobodalla"}
#       ]
# }
def setup_choices_map(survey_questionnaire:dict)-> dict:
  choices_map = {}
  for page in survey_questionnaire["pages"]:
    for element in page["elements"]:
      if element["type"] in question_types_with_possible_translations:
        choices_map[element["name"]] = element["choices"]
  return choices_map


def translate_where_possible(choices_map:dict, survey_data:dict):
  translated = survey_data.copy()
  for question_id, answer in survey_data.items():
    choices:list = choices_map.get(question_id,[]) # SLK will return None
    for choice in choices:
      if isinstance(choice,dict):        
        if choice.get("value") == answer:
          translated[question_id] = choice.get("text")
  return translated
      

    # for choice in choces



if __name__ == '__main__':
  
  survey_data:dict = get_json_data('./Files/FlattenedSurveySubmission.json')
  qstnr = get_survey_questionnaire(survey_data['AssessmentType'])

  choices_map = setup_choices_map (qstnr) 

  translated_answers = translate_where_possible(choices_map, survey_data['SurveyData'])

  # process
  