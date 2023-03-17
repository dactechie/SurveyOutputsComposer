
import json
from SurveyFragments import SurveyFragments
import DocumentGenerator


root_template_folder = 'template_fragments'

def main (data: dict, outfile_format: str) -> None:
  """
    inspects the survey data against a set of blueprints
    constructs a list of documents (fraagments) and populates their placeholders
    saves the stitched-together fragements

    Uses local fragments if correct version, else 
  """


  survey_data = {
          **{
             "Staff": data["Staff"], 
             "SLK": data["SLK"],
             "Program": data['Program'],
             "AssessmentType": data["AssessmentType"]
            } 
          , **data['SurveyData']
          }

  sf = SurveyFragments(survey_data, data['Program'])

  bluep_json_path = sf.get_blueprint_filepath()
  ordered_fragments_paths = sf.get_fragpaths(bluep_json_path)

  # versions = [1.0, 1.0 , 1.0, 1.5]
  versions = [1.0, 1.0 , 1.0, 1.0]
  documents = DocumentGenerator.build_doc_list(ordered_fragments_paths, versions)
  
  if not documents:
    print("No fragments. Quitting.")
    return

  doc_gen = DocumentGenerator.DocumentGenerator(f"./{root_template_folder}/common/Base.docx")
  final_doc, output_fname = doc_gen.build_document(documents, survey_data, outfile_format, strip_spaces=True)
  
  final_doc.save(f"{output_fname}.docx")
  
  print(f"Saved document: {output_fname}.")



if __name__ == '__main__':
  
  with open('./Files/FlattenedSurveySubmission.json', 'r') as jsonfile:
    data = json.load(jsonfile)
  

  outfile_format = "SLK_AssessmentType_ClientType"

  main(data, outfile_format)
 

 

 # survey_data = {'AssessmentType':'ATOM ITSP Review Assessment','ClientType':'othersuse'}
# sf = SurveyFragments(survey_data, program='TSS')
# bluep_json_path = sf.get_blueprint_filepath()
# ordered_fragments = sf.get_fragpaths(bluep_json_path)
# print(ordered_fragments)


# sdata_sds = {}
# with open('./IASubmission.json', 'r') as jsonfile:
#   survey_data = json.load(jsonfile)
  # meta_keys = ['SLK', 'AssessmentType', 'ClientType']
  # sdata_sds = {k:v for k, v in survey_data.items() if k in meta_keys or k.startswith('SDS')}
  

# print(sdata_sds)
# survey data
#data = sdata_sds


  # Sharepoint
  # sp_prefix = f'/Shared Documents/ICT/ATOM/{RUNTIME_STAGE}/{root_template_folder}'  
  # ordered_fragments_paths = get_full_doc_paths(ordered_section_paths, sp_prefix)
  # documents = get_sharepoint_docx_files(ordered_fragments_paths)

  # Local
  # path_prefix=f'./{root_template_folder}'
  # local_ordered_fragments_paths = get_full_doc_paths(ordered_section_paths)
  # documents = get_local_docx_files(local_ordered_fragments_paths)

  # document = get_section_document(ordered_fragments_paths[3]) # from Sharepoint
  # documents = get_section_document(ordered_fragments_paths) # from Sharepoint