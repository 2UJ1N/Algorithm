def solution(people, limit):
    boat = 0
    people.sort(reverse=True)
    
    while len(people) != 0:
        if len(people) == 1:
            boat += 1
            return boat
        else:
            cnt = 0
            for i in range(len(people) - 1):
                if people[i] + people[-1] <= limit:
                    break
                else: 
                    cnt += 1
            boat += cnt + 1
            people = people[cnt + 1 : -1]

    return boat