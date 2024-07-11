def solution(people, limit):
    boat = 0
    people.sort(reverse=True)
    
    while len(people) != 0:
        if len(people) == 1:
            boat += 1
            return boat
        else:
            if people[0] + people[-1] <= limit:
                boat += 1
                people = people[1:-1]
            else:
                boat += 1
                people = people[1:]
    
    return boat