import os, tempfile
import io
from office365.runtime.auth.client_credential import ClientCredential
from office365.sharepoint.client_context import ClientContext


print("**************** > imported SharepointHandler module")

class SharepointHandler:
  def __init__(self, site_url, client_id, client_secret):    
    self.ctx = ClientContext(site_url).with_credentials(ClientCredential(client_id, client_secret))
    

  # def download_file(self, file_url):
  #   download_path = os.path.join(tempfile.mkdtemp(), os.path.basename(file_url))
  #   with open(download_path, "wb") as local_file:
  #     file = self.ctx.web.get_file_by_server_relative_path(file_url).download(local_file).execute_query()      
  #     print(file)
  #   return file


  def _open_binary(self, file_url):# -> bytes:
    download_path = os.path.join(tempfile.mkdtemp(), os.path.basename(file_url))
    with open(download_path, "wb") as local_file:
      bstream = self.ctx.web.get_file_by_server_relative_path(file_url).open_binary_stream().execute_query()
    
    return io.BytesIO(bstream.value) #type: ignore

  def get_document(self, file_url):# -> bytes:
    return self._open_binary(file_url)

  # def upload_file(self, file_path):
  #   path = "../../data/report #123.csv"
  #   with open(path, 'rb') as content_file: 
  #     file_content = content_file.read()

  #   list_title = "Documents"
  #   target_folder = ctx.web.lists.get_by_title(list_title).root_folder
  #   name = os.path.basename(path)
  #   target_file = target_folder.upload_file(name, file_content).execute_query()
  #   print("File has been uploaded to url: {0}".format(target_file.serverRelativeUrl))



# if __name__ == '__main__':
#   client_id = "3b0d4f21-94af-4615-b921-ea0a0ef1346a"
#   client_secret = "9ekEusxbFweTp8Vjp81hKw8FaUSIWEGq62+F63r5Atc="
#   site_url = "https://directionshealth.sharepoint.com"
#   sph = SharePointHandler(site_url, client_id, client_secret)
#   file_url = "/Shared Documents/ICT/ATOM/Staging/template_fragments/common/SDS.docx"
#   sp_local_file_frag = sph.download_file(file_url)
#   # sp_local_file_frag.open_binary(ctx, server_relative_url)
  
#   file_stream = io.BytesIO(sp_local_file_frag.open_binary_stream())
  

