# copied from:
# http://blog.cloudera.com/blog/2009/09/grouping-related-trends-with-hadoop-and-hive/
import sys, os, re

insert_regex = re.compile('''INSERT INTO `pagelinks` VALUES (.*)\;''')
row_regex = re.compile("""(.*),(.*),'(.*)'""")
 
for line in sys.stdin:
  match = insert_regex.match(line.strip())
  if match is not None:
    data = match.groups(0)[0]
    rows = data[1:-1].split("),(")
    for row in rows:
      row_match = row_regex.match(row)
      if row_match is not None:
        # >>> row_match.groups()
        # (12,0,'Anti-statism')
        # # page_id, pl_title
        if row_match.groups()[1] == '0':
          page_id, pl_title = row_match.groups()[0], row_match.groups()[2]
          sys.stdout.write('%s\t%s\n' % (page_id, pl_title))

