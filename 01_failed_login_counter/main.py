with open('sample.log', 'r',  encoding='utf-8') as file_log:
  d1 = {}
  
  
  for line in file_log:
    if 'Login failed' in line:
      lines = line.split()
      user = ''
      ip = ''
      key = ''
      
      for word in lines:
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
  print('Failed login attempts by identifier: ')
  for key, value in d1.items():
    print(f'identifier: {key} Fails: {value} ')
