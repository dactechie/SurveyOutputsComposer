
# import io
# import json
from typing import Generator, List, Dict
from docxcompose.composer import Composer
from docx import Document
from docx.text.paragraph import Paragraph

from docx_fetch.GenericDocx import GenericDocument

survey_data_mapper_funcs={
  'PDC': lambda PDCList: PDCList[0]['PDCSubstanceOrGambling']
}

def get_paras(doc:Document) -> Generator[Paragraph, None, None]:# type: ignore
  for table in doc.tables:
    for row in table.rows:
      for cell in row.cells:
        for para in cell.paragraphs:
          if '%%' in para.text:            
            yield para

  
def get_normalised_surveydata(survey_data, k_prepend = ''):
  normalised_survey_data = {}
  for k, v in survey_data.items():
    newk = f'{k_prepend}{k.replace(" ", "")}'
    t = type(v)
    if t is list:
      x = type(v[0])
      if x is str:        
        normalised_survey_data[newk] = ",".join(v)
      elif x is dict:
        # only takng the first one for now 
        sub_dict = get_normalised_surveydata(v[0], newk)
        normalised_survey_data.update(sub_dict)
      continue
    elif t is int:
      val = str(v)
    elif t is dict:  # e.g otherAddictiveBehaviours
      print(f'Dict {newk} found, continuing')
      val = get_normalised_surveydata(v, newk)
      normalised_survey_data.update(val)
      continue          
    else:
      val = v
    normalised_survey_data[newk] = val
  return normalised_survey_data
  

def replace_text(normalised_survey_data, doc: Document) -> Generator[Document, None, None]:  # type: ignore
  for para in get_paras(doc):    
    # if '%%' not in para.text:
    #   print('text: ', para.text)
    #   continue
    # print(f"Has variable : {para.text} ")
    for k, v in normalised_survey_data.items():
      para.text = para.text.replace(f'%%{k}%%', v)
  return doc



class DocumentGenerator:

  # '''
  #   Gets the correct blueprint based on the Survey data
  # '''
  # def load_blueprint(self, survey_data):
  #   pass

  # @classmethod
  # def get_document(cls, doc_bytes_or_path):        
  #   return Document(doc_bytes_or_path)

  def replace_placeholders(self):
    pass

  def __init__(self, base_doc_path):
    # self.base_doc = Document(base_doc_path)
    self.composer = Composer(Document(base_doc_path))


  def compose_document(self, ordered_fragments: List[GenericDocument], survey_data):
    if ordered_fragments is None:
      print("FilePaths was null")
      return None
    
    survey_data = get_normalised_surveydata(survey_data)
    for fragment in ordered_fragments:
      #replace variable placeholders here
      
      replaced_fragment = replace_text(survey_data, fragment)
      self.composer.append(replaced_fragment)

    return self.composer
  



# if __name__ == '__main__':
