refuse = 0
suggest = 1
accept = 2

def marriage(men, women):
    married = [[refuse for _ in women] for _ in men]
    pairs = []
    pairs_number = len(men);
    unapaired_man_index = get_unpaired_man(married)
    while unapaired_man_index is not None:
        pref_woman_index = men[unapaired_man_index].pop(0)

        while unapaired_man_index not in women[pref_woman_index]:
            pref_woman_index = men[unapaired_man_index].pop(0)

        man_index = women[pref_woman_index].index(unapaired_man_index)
        married = delete_prev_suggestion(married, pref_woman_index)

        if man_index is 0:
            married[unapaired_man_index][pref_woman_index] = accept
            pairs.append((unapaired_man_index, pref_woman_index))
            men = remove_woman_from_men(men, pref_woman_index)
        else:
            married[unapaired_man_index][pref_woman_index] = suggest

        women[pref_woman_index] = women[pref_woman_index][:man_index]
        unapaired_man_index = get_unpaired_man(married)
    return pairs

def get_unpaired_man(married):
    unamarried = None
    for man_index in range(len(married)):
        if suggest not in married[man_index] and accept not in married[man_index]:
            return man_index
        if accept not in married[man_index] and unamarried is None:
            unamarried = man_index
    return unamarried

def remove_woman_from_men(men, woman):
    for man in men:
        try:
            man.remove(woman)
        except ValueError:
            pass
    return men

def delete_prev_suggestion(married, woman):
    for man in married:
        if man[woman] is accept or man[woman] is suggest:
            married[married.index(man)][woman] = refuse
            return married
    return married
