import os,sys,re

if len(sys.argv) != 2:
    print('ファイルを指定してください')
    sys.exit

path = sys.argv[1]

csv_path = path + '.csv'

with open(csv_path, 'a') as output:
    with open(path, 'r') as input:
        for line in input:
            space_regex = re.compile(r'(\s+)')
            new_line = space_regex.sub(',', line.strip())

            output.write(new_line)
            output.write('\n')
