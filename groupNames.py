from unidecode import unidecode

def findName(line):
    line = line.split("\"")
    return line[1].strip()

def groupNamesUnidecode(fin):
    group = {}
    with open(fin, 'r') as f:
        for line in f:
            if line[0]!="*" and len(line.split())!=3:
                name = findName(line)
                uni = unicode(name,'utf8')
                uni = unidecode(uni)
                if uni in group:
                    group[uni].append(name)
                else:
                    group[uni]=[name]
    for key, value in group.iteritems():
        if len(value)>1:
            print key,value


def groupNamesCase(fin):
    group = {}
    with open(fin, 'r') as f:
        for line in f:
            if line[0]!="*" and len(line.split())!=3:
                name = findName(line)
                low = name.lower()
                if low in group:
                    group[low].append(name)
                else:
                    group[low]=[name]
    for key, value in group.iteritems():
        if len(value)>1:
            print key,value

def groupNamesBoth(fin):
    group = {}
    with open(fin, 'r') as f:
        for line in f:
            if line[0]!="*" and len(line.split())!=3:
                name = findName(line)
                unilow = unicode(name,'utf8')
                unilow = unidecode(unilow)
                unilow = unilow.lower()
                if unilow in group:
                    group[unilow].append(name)
                else:
                    group[unilow]=[name]
    for key, value in group.iteritems():
        if len(value)>1:
            value = [unicode(name,'utf8')  for name in value]
            print key,value

if __name__ == '__main__':
    groupNamesBoth('dblp.net')
