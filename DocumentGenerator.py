from typing import Generator, List, Any, Dict
from docxcompose.composer import Composer
from docx import Document
from docx.text.paragraph import Paragraph
from docx_fetch.GenericDocx import GenericDocument
from utils.dict_util import get_normalised_dict
from utils.text_util import get_variables_in_text


def get_paras(doc:Document) -> (Generator[Paragraph, None, None], List[Any]):# type: ignore
  for table in doc.tables:
    for row in table.rows:
      for cell in row.cells:
        for para in cell.paragraphs:
          variables = get_variables_in_text(para.text)
          if variables:
            yield para, variables
  
def replace_placeholders(normalised_survey_data: dict, doc: Document) -> Generator[Document, None, None]:  # type: ignore
  for para, para_variables in get_paras(doc):
    for pv in para_variables:
      para.text = para.text.replace(f'%%{pv}%%', normalised_survey_data[pv])
  return doc

class DocumentGenerator:

  def __init__(self, base_doc_path):
    # self.base_doc = Document(base_doc_path)
    self.composer = Composer(Document(base_doc_path))


  def compose_document(self, ordered_fragments: List[GenericDocument], survey_data: dict):
    if ordered_fragments is None:
      print("FilePaths was null")
      return None
    
    survey_data = get_normalised_dict(survey_data)
    for fragment in ordered_fragments:
      #replace variable placeholders here
          
      replaced_fragment = replace_placeholders(survey_data, fragment)
      self.composer.append(replaced_fragment)

    return self.composer
  