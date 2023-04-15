from shareplum import Site, Office365
from shareplum.site import Version

import json, os

# https://github.com/vgrem/Office365-REST-Python-Client/wiki/How-to-connect-to-SharePoint-Online-and-and-SharePoint-2013-2016-2019-on-premises--with-app-principal
# Client Id:  	3b0d4f21-94af-4615-b921-ea0a0ef1346a
# Client Secret:  	9ekEusxbFweTp8Vjp81hKw8FaUSIWEGq62+F63r5Atc=
# Title:  	Python Console
# App Domain:  	localhost
# Redirect URI:  	https://localhost

def load_config(level):
  ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
  config_path = '/'.join([ROOT_DIR,f'config.{level}.json'])

  with open (config_path) as configfile:
      cfg = json.load(configfile)
      sp_cfg = cfg['share_point']
  return sp_cfg

# if __name__ == '__main__':
#   sp_cfg = load_config()
#   UNAME = sp_cfg['username']
#   PWD = sp_cfg['password']
#   SP_URL = sp_cfg['url']
#   SP_SITE =  sp_cfg['site']
#   SP_DOC = sp_cfg['doc_library']


class SharePoint:
  
  def __init__(self, config):
    self.UNAME = config['username']
    self.PWD = config['password']
    self.SP_URL = config['url']
    self.SP_SITE =  config['site']
    self.SP_DOC = config['doc_library']
      
  def auth(self):
      self.authcookie = Office365(self.SP_URL, username=self.UNAME, password=self.PWD).GetCookies()
      self.site = Site(self.SP_SITE, version=Version.v365, authcookie=self.authcookie)

      return self.site

  
  def connect_folder(self, folder_name):
      self.auth_site = self.auth()

      self.sharepoint_dir = '\\'.join([self.SP_DOC, folder_name])
      self.folder = self.auth_site.Folder(self.sharepoint_dir)

      return self.folder

  def download_file(self, file_name, folder_name):
      self._folder = self.connect_folder(folder_name)
      return self._folder.get_file(file_name)