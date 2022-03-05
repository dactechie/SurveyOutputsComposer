from typing import Any, List
import json
from SurveyFragments import SurveyFragments
from SharepointHandler import SharepointHandler
from DocumentGenerator  import DocumentGenerator
from docx_fetch.GenericDocx import GenericDocument
from docx_fetch.LocalDocx import LocalDocx
from docx_fetch.SharepointDocx import SharepointDocx

site_url = "https://directionshealth.sharepoint.com"
# load from config.prod.json / env client id and client secret
root_template_folder = 'template_fragments'
current_version_all_docs = 1.0 # temporary. Each doc would have its current version

RUNTIME_STAGE ="Staging" # Prod

def get_sp_doc_fetcher(sph:SharepointHandler, path_versions, sp_prefix)-> Any:
  for fp, version in path_versions:     
    docx_fetcher = None
    if version != current_version_all_docs:
      full_path = f"{sp_prefix}/{fp}"
      docx_fetcher = SharepointDocx(full_path, sph)
      yield docx_fetcher

      # doc = docx_fetcher.get_document()
      # yield doc
  #     sp_docs.append(doc)
  # return sp_docs


def build_doc_list(ordered_fragments_paths, versions) -> List[GenericDocument]:  
  documents : list[GenericDocument]= []
  prefixes = []
  sp_docs: list[SharepointDocx] = []
  path_versions = zip(ordered_fragments_paths, versions)
  if any(v for v in versions if v != current_version_all_docs):
    sph = SharepointHandler(site_url, client_id, client_secret)
    sp_prefix = f'/Shared Documents/ICT/ATOM/{RUNTIME_STAGE}/{root_template_folder}'
    sp_docs = list(reversed(list(get_sp_doc_fetcher(sph, path_versions, sp_prefix))))

  for fp, version in  zip(ordered_fragments_paths, versions):     
    docx_fetcher = None
    if version == current_version_all_docs:
      full_path = f"./{root_template_folder}/{fp}"
      docx_fetcher = LocalDocx(full_path)
    else:
      docx_fetcher = sp_docs.pop()

    doc = docx_fetcher.get_document()
    documents.append(doc)
  return documents



if __name__ == '__main__':
  
  
  # survey_data = {'AssessmentType':'ATOM ITSP Review Assessment','ClientType':'othersuse'}
  # sf = SurveyFragments(survey_data, program='TSS')
  # bluep_json_path = sf.get_blueprint_filepath()
  # ordered_fragments = sf.get_fragpaths(bluep_json_path)
  # print(ordered_fragments)


  sdata_sds = {}
  with open('./IASubmission.json', 'r') as jsonfile:
    survey_data = json.load(jsonfile)
    meta_keys = ['SLK', 'AssessmentType', 'ClientType']
    sdata_sds = {k:v for k, v in survey_data.items() if k in meta_keys or k.startswith('SDS')}
    

  print(sdata_sds)
  # survey data
  #data = sdata_sds
  
  sf = SurveyFragments(survey_data, program='TSS')

  bluep_json_path = sf.get_blueprint_filepath()
  ordered_fragments_paths = sf.get_fragpaths(bluep_json_path)

  versions = [1.0, 1.0 , 1.0, 1.5]
  documents = build_doc_list(ordered_fragments_paths, versions)
  
  
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
  
  doc_gen = DocumentGenerator(f"./{root_template_folder}/common/Base.docx") # this will always be local to the application

  final_doc = doc_gen.compose_document(documents, survey_data)
  if final_doc:
    final_doc.save(f"{survey_data['SLK']}_{survey_data['AssessmentType']}_{survey_data['ClientType']}.docx")
  else :
    print("final doc was null")

