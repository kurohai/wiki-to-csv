import xml.etree.ElementTree as ET
from pprint import pprint
from dicto import dicto

import sys

infile = sys.argv[1]
outfile = sys.argv[2]
# outfile = 'xml-out.csv'

class User(dicto):
    pass

def main():
    user_list = list()
    tree = ET.parse(infile)
    # tree = ET.parse('wiki-data.xml')
    root = tree.getroot()
    for user in root[0]:
        data = dicto(user.attrib)
        # print data.Title
        n = User()
        n.id = data.ID
        n.name = data.Title

        for u in user:
            for u2 in u:
                u3 = dicto(u2.attrib)
                n[u3.Name] = u2.text
        user_list.append(n)


    headers = list()
    with open(outfile, 'wb') as f:
        for u in user_list:
            for k, v in u.items():
                headers.append(k)

        headers = set(headers)
        headers = [h for h in headers]
        for h in headers:
            f.write(h + '\t')


        for u in user_list:
            f.write('\n')
            key_count = 0
            for h in headers:
                if h in u.keys():
                    f.write(u[h] + '\t')
                else:
                    f.write('\t')


if __name__ == '__main__':
    main()
