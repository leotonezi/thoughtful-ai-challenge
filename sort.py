def sort(width, height, length, mass):
  bulky = False
  heavy = False

  try:
    if(width * height * length >= 1000000) or ((width >= 150) or (height >= 150) or (length >= 150)):
      bulky = True
    
    if(mass >= 20):
      heavy = True
    
    if heavy and bulky:
      return 'REJECTED'
    
    if heavy or bulky:
      return 'SPECIAL'
    
    return 'STANDARD'
  except Exception as e:
    print('Error: ', str(e))
    raise