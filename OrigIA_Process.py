import json
from typing import List, Dict
from constants import MAP_FIELD_TRANSLATIONS, STRFORMAT_OUTFILENAME #,SURVEY_TYPE_MAP 
from utils import  text_util, dict_util
from docx_fetch.GenericDocx import GenericDocument
from SurveyFragmentsV2 import SurveyFragments
import DocumentGenerator
from AssessmentObjects.AssessmentDefinitions import get_assessment_meta, AssessmentMeta


def get_ordered_fragments(survey_data:dict, assessment_meta:AssessmentMeta) -> List[GenericDocument]:

    sf = SurveyFragments(survey_data, assessment_meta) #survey data is passed in becuase 
    # show if Config says load SDS only if SDS is present in data vs for some survey types , always show blank SDS

    bluep_json_path = sf.get_blueprint_filepath()
    ordered_fragments_paths = sf.get_fragpaths(bluep_json_path)

    # versions = [1.0, 1.0 , 1.0, 1.5]
    versions = [1.0, 1.0 , 1.0, 1.0]
    documents = DocumentGenerator.build_doc_list(ordered_fragments_paths, versions)
    return documents
      
"""
TODO
see translate : C:/Users/aftab.jalal/dev/SurveyOutputsComposer/main_use_surveyjs_qjson.py
"""
def translate_answers(survey_submission:dict):
   pass


def file_name(assessment_meta:AssessmentMeta ,outfile_format, strip_spaces: bool = False) -> str:
  # TODO dont use dunder ?
  output_fname =  text_util.build_str_from_format(outfile_format, assessment_meta._asdict(), strip_spaces) 
  return output_fname

def fill_template_with_answers(documents, survey_submission:dict): 
  if not documents:
        print("No fragments. Quitting.")
        return
  root_template_folder = 'template_fragments' #TODO: get rid of this from here
  doc_gen = DocumentGenerator.DocumentGenerator(f"./{root_template_folder}/common/Base.docx") 
  final_doc = doc_gen.build_document(documents, survey_submission)
  return final_doc

def translate_fields(survey_submission:dict) -> Dict:
  # PartitionKey => SLK
  translated_fields = dict_util.translate_dict_keys(survey_submission, MAP_FIELD_TRANSLATIONS)
  
  return translated_fields
  

def get_flattened_survey_data(survey_submission:dict) -> Dict:
   sd_normd = dict_util.get_normalised_dict( survey_submission['SurveyData'])
   merged_dicts = dict_util.merge_dicts( survey_submission, sd_normd)
   return merged_dicts

def save_doc(full_doc, destination_path:str, output_fname:str):
  full_doc.save(f"{destination_path}/{output_fname}.docx")
  print(f"Saved document: {output_fname}.")

def do_all(survey_submission:dict):
  # prep_nested_map()
  survey_submission['SurveyData'] = json.loads(survey_submission['SurveyData'])
  assessment_meta = get_assessment_meta(survey_submission)
  flttened_survey_submsn =  get_flattened_survey_data(survey_submission)

  # assessment_meta = AssessmentMeta(survey_submission)

  doclist = get_ordered_fragments(flttened_survey_submsn, assessment_meta)
  flttened_survey_submsn = translate_fields(flttened_survey_submsn) # PartitionKey => SLK
  # translated_submission = translate_answers(survey_submission)
  full_doc = fill_template_with_answers(doclist, flttened_survey_submsn)
  
  output_fname = file_name(assessment_meta, STRFORMAT_OUTFILENAME, strip_spaces=True)
  save_doc(full_doc,"./Files/output" ,output_fname)


if __name__=="__main__":
  # infile_key = "BEGAPATH_INAS_20221217" 
  infile_key = "MURMPP_INAS_20230403"
  with open(f"./Files/input/{infile_key}.json", "r") as jsonfile: # IA_Orig
      survey_submission = json.load(jsonfile) 
      outputfile_path = do_all(survey_submission)
      print(f"Done processing. Outputfile : {outputfile_path}")




# # get_top_level_keys = lambda json_data: list(json_data.keys())

# # support for flattening survey data
# # based on the survey type, these are the top level keys
# MAP_SURVEY_NESTEDKEY = {
#   "PAT_INAS_ownuse": {
    
#   },  
#   "TSS_INAS_ownuse": ['PDC']
# }
# #
# # TODO: eventually figure this out from the questionnaire
# #
# def prep_nested_map():
#    MAP_SURVEY_NESTEDKEY["TSS_ITSP_ownuse"] = MAP_SURVEY_NESTEDKEY["TSS_INAS_ownuse"]



      # survey_data = json.loads(survey_submission)['SurveyData']
      
      # k = get_nestedmapkey_fromrowkey(survey_submission['AssessmentType'], survey_submission['ClientType'])

      # nested_fields = MAP_SURVEY_NESTEDKEY[k]

      # get_top_level_keys    