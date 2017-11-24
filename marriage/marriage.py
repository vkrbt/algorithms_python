def marriage(men={}, women={}):
    manRow = dict.fromkeys(men.keys())
    married = {}
    for woman in women.keys():
        married[woman] = manRow
    print(married)
    existUnmarriedPair(married)

def existUnmarriedPair(married):
    for woman in married.values():
        for man in woman.values():
            if man is None:
                return True
