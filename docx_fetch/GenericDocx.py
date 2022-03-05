
from docx import Document

class GenericDocument:
  def __init__(self, path_or_bytes):
    self.path_or_bytes = path_or_bytes

  def get_document(self) -> Document:# type: ignore
    return Document(self.path_or_bytes)