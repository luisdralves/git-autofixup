#!/usr/bin/env python3

import os

exceptions = {
  'emptyBranch': 'No commits in this branch yet!',
  'singleCommit': 'Only one commit in this branch use amend instead'
}

data = os.sys.stdin.read()
for commit in data[1:].split('\n\n'):
  lines = commit.split('\n')
  if exceptions['emptyBranch'] in lines[0] or exceptions['singleCommit'] in lines[0]:
    print(lines[0])
    break

  commit_hash = commit[5:12]
  print(lines[0])
  files = commit.split('\n')

  os.system('git reset')  
  for file in files[1:]:
    if len(file) > 1:
      os.system('git add '+file[14:])

  if commit_hash == '#######':
    try:
      os.system('git commit -m '+argv[1])
    except:
      print('There are leftovers')
  else:
    os.system('git fixup '+commit_hash)
