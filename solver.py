from functools import lru_cache

@lru_cache(maxsize=None) # CACHING
def response(guess, answer):
    lguess = list(guess)
    lanswer = list(answer)
    resp = [0 for _ in range(5)]
    for i in range(5):
        if lguess[i] == lanswer[i]:
            resp[i] = 2
            lanswer[i] = '-'
    for i in range(5):
        if lguess[i] in lanswer and resp[i] == 0:
            resp[i] = 1
            lanswer[lanswer.index(lguess[i])] = '-'
    return tuple(resp)

def predict(candidate, solution1, solution2, solution3, solution4):
    min_avg = 1e5 # HIGH ENOUGH
    table1 = {}
    table2 = {}
    table3 = {}
    table4 = {}
    bestguess = ""
    for guess in candidate:
        guess = guess.strip()
        tsol1 = {}
        tsol2 = {}
        tsol3 = {}
        tsol4 = {}
        for posans in solution1:
            posans = posans.strip()
            resp = response(guess, posans)
            if resp not in tsol1:
                tsol1[resp] = [posans]
            else:
                tsol1[resp].append(posans)
        for posans in solution2:
            posans = posans.strip()
            resp = response(guess, posans)
            if resp not in tsol2:
                tsol2[resp] = [posans]
            else:
                tsol2[resp].append(posans)
        for posans in solution3:
            posans = posans.strip()
            resp = response(guess, posans)
            if resp not in tsol3:
                tsol3[resp] = [posans]
            else:
                tsol3[resp].append(posans)
        for posans in solution4:
            posans = posans.strip()
            resp = response(guess, posans)
            if resp not in tsol4:
                tsol4[resp] = [posans]
            else:
                tsol4[resp].append(posans)
        maxsol1 = max([len(v) for v in tsol1.values()] + [0])
        maxsol2 = max([len(v) for v in tsol2.values()] + [0])
        maxsol3 = max([len(v) for v in tsol3.values()] + [0])
        maxsol4 = max([len(v) for v in tsol4.values()] + [0])
        avg_max = (maxsol1 + maxsol2 + maxsol3 + maxsol4) / 4
        if avg_max < min_avg:
            min_avg = avg_max
            bestguess = guess
            table1 = tsol1
            table2 = tsol2
            table3 = tsol3
            table4 = tsol4
    return bestguess, table1, table2, table3, table4
