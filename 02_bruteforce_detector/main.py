with open("sample.log", "r") as file:
  d1 = {}
  
  for line in file:
    if 'Login failed' in line:
      row = line.split()
      user = ''
      ip = ''
      key = ''

      for word in row:
        if word.startswith('user=') and len(word) > 5:
          user = word[5:]
        elif word.startswith('ip=') and len(word) > 3:
          ip = word[3:]
          
      if user != '':
        key = user
      elif ip != '':
        key = ip
      else:
        key = 'unknown'

      if key not in d1:
        d1[key] = 1
      else:
        d1[key] += 1


  if not d1:
    print('No failed logins found.')
  else:
    print('Bruteforce suspects (threshold=3):')
    for key, value in d1.items():
      if value >= 3 and key != 'unknown':
        print(f'Identifier: {key} Fails: {value}')
      
        

    
    
    
