with open('sample.log', 'r',  encoding='utf-8') as file_log:
  d1 = {}
  lines = []
  user = ''
  
  for line in file_log:
    if 'Login failed' in line:
      lines = line.split()
      for word in lines:
        user = ''
        if word.startswith('user=') and len(word) > 5:
          user = word[5:]
        elif word.startswith('ip=') and len(word) > 3:
          user = word[3:]
        else:
          user = 'unknown'
      if user not in d1:
        d1[user] = 1
      else:
        d1[user] += 1
      
