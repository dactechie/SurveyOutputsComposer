def get_normalised_dict(survey_data, parent_key = ''):
  normalised_data = {}
  for k, v in survey_data.items():
    newk = f'{parent_key}{k.replace(" ", "")}'
    t = type(v)
    if t is list:
      x = type(v[0])
      if x is str:        
        normalised_data[newk] = ",".join(v)
      elif x is dict:
        # only takng the first one for now 
        sub_dict = get_normalised_dict(v[0], newk)
        normalised_data.update(sub_dict)
      continue
    elif t is int:
      val = str(v)
    elif t is dict:  # e.g otherAddictiveBehaviours
      print(f'Dict {newk} found, continuing')
      val = get_normalised_dict(v, newk)
      normalised_data.update(val)
      continue          
    else:
      val = v
    normalised_data[newk] = val
  return normalised_data
