with open('blacklist.txt', 'r') as blacklist_file:
  blacklist = set()

  for blist in blacklist_file:
    temp = blist.strip()
    if temp != '':
      blacklist.add(temp)

with open('sample_ips.txt', 'r') as sample_ips:
  ips = []

  for ip in sample_ips:
    ip_temp = ip.strip()
    if ip_temp != '':
      ips.append(ip_temp)

  blacklisted = []
  not_blacklisted = []
  total_blacklisted = 0 
  total_not_blacklisted = 0
    
  for ip in ips:
    if ip in blacklist:
      blacklisted.append(ip)
      total_blacklisted += 1
    else:
      not_blacklisted.append(ip)
      total_not_blacklisted += 1
      
with open('results.txt', 'w') as result:

  result.write('BLACKLISTED:\n')
  if not blacklisted:
    result.write('NONE\n')
    result.write('Total blacklisted: ' + str(total_blacklisted) + '\n')
  else:
    result.write('\n'.join(blacklisted) + '\n')
    result.write('Total blacklisted: ' + str(total_blacklisted) + '\n')
    
  result.write('\n')
  
  result.write('NOT BLACKLISTED:\n')
  if not not_blacklisted:
    result.write('NONE\n')
    result.write('Total not blacklisted: ' + str(total_not_blacklisted) + '\n')
  else:
    result.write('\n'.join(not_blacklisted) + '\n')
    result.write('Total not blacklisted: ' + str(total_not_blacklisted) + '\n')
    
  
