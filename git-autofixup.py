#!/usr/bin/env python3

import os

exceptions = {
  'emptyBranch': 'No commits in this branch yet!',
  'singleCommit': 'Only one commit in this branch use amend instead'
}

data = os.sys.stdin.read()
for commit in data[1:].split('\n\n'):
  print()
  lines = commit.split('\n')
  if exceptions['emptyBranch'] in lines[0] or exceptions['singleCommit'] in lines[0]:
    print(lines[0])
    break

  commit_hash = commit[5:12]
  print(lines[0])
  files = list(filter(lambda line: (len(line) > 1 and '^--' not in line and line[5] == 'M'), lines[1:]))

  os.system('git reset -q')
  for file in files:
    print(f'  {file[14:]}')
    os.system(f'git add {file[14:]}')

  if commit_hash == '#######':
    print('There are leftovers')
  else:
    os.system(f'git fixup {commit_hash}')
