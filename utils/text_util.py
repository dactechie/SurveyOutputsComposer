import re

placeholder_pattern = re.compile(r'%%([^%%]+)%%')

def get_variables_in_text(text: str):
  matches = re.findall(placeholder_pattern, text)
  return matches

def build_str_from_format(str_format:str, data:dict, strip_spaces: bool) -> str:
  parts = [data[p] for p in str_format.split('_')]
  if strip_spaces:
      parts = [p.replace(' ','')  for p in parts]
  return '_'.join(parts)

# if __name__ == '__main__':
#   s = 'asdf=5;iw%%var1%%tthi%%var2%%jasd'
#   # result = re.search('%%(.*)%%', s)
#   # print(result.group(1))

  
#   match = re.findall(pattern, s)
#   print(match)
  