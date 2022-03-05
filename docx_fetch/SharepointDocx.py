
from typing import Any
from docx import Document
from .GenericDocx import GenericDocument
from SharepointHandler import SharepointHandler
# print ('>>> Importing ShareporintHandler and defining class')

class SharepointDocx(GenericDocument):
  
  def __init__(self, path_or_bytes:Any, sharepointHandler: SharepointHandler):
    super().__init__(path_or_bytes)
    self.sp_handler = sharepointHandler

  def get_document(self) -> Document:    # type: ignore
    return Document(
         self.sp_handler.get_document(self.path_or_bytes)
    )
