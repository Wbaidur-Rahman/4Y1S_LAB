class Activity:
    def __init__(self, id, name, dur) -> None:
        self.id = id
        self.name = name
        self.dur = dur
        self.es = 0
        self.ef = 0
        self.lf = 0
        self.ls = 0
        self.predecessors = []
        self.successors = []

index = []
activities = {}

for line in open('activity.txt'):
    words = line.rstrip('\n').split(',')
    id = int(words[0])
    name = words[1]
    dur = int(words[2])
    predessor = words[3]
    index.append(id)
    activities[id] = Activity(id, name, dur)
    if predessor!='':
        predessors = predessor.split(';')
        for u in predessors:
            u = int(u)
            activities[id].predecessors.append(u)
            activities[u].successors.append(id)

maxEF = 0
for id in index:
    if len(activities[id].predecessors)==0:
        activities[id].ef = activities[id].dur
    else:
        maxTime = 0
        for item in activities[id].predecessors:
            maxTime = max(maxTime, activities[item].ef)
        
        activities[id].es = maxTime
        activities[id].ef = maxTime+activities[id].dur

    maxEF = max(maxEF, activities[id].ef)

for id in reversed(list(index)):
    if len(activities[id].successors)==0:
        activities[id].lf = maxEF
        activities[id].ls = maxEF - activities[id].dur
    else:
        minTime = 1000
        for item in activities[id].successors:
            minTime = min(minTime, activities[item].ls)
        
        activities[id].lf = minTime
        activities[id].ls = minTime-activities[id].dur

result = []

for id in index:
    if(activities[id].lf == activities[id].ef):
        result.append(activities[id].name)

for i,e in (list(enumerate(result))):
    if(i!=len(result)-1):
        print(e, end = ' --> ')
    else:
        print(e, end='')
