import re

placeholder_pattern = re.compile(r'%%([^%%]+)%%')

def get_variables_in_text(text: str):
  matches = re.findall(placeholder_pattern, text)
  return matches

# if __name__ == '__main__':
#   s = 'asdf=5;iw%%var1%%tthi%%var2%%jasd'
#   # result = re.search('%%(.*)%%', s)
#   # print(result.group(1))

  
#   match = re.findall(pattern, s)
#   print(match)
  