def marriage(mens, womans):
    temp_mens = list(mens.values())

    while temp_mens:
        men = temp_mens[0]

        for woman in men.women:
            pref_woman = womans[woman]

            if pref_woman.partner is None:
                pref_woman.partner = men
                men.partner = pref_woman
                temp_mens.remove(men)
                break

            elif (pref_woman.women.index(men.name)
                    < pref_woman.women.index(pref_woman.partner.name)):

                temp_mens.append(pref_woman.partner)
                pref_woman.partner = men
                men.partner = pref_woman
                temp_mens.remove(men)
                break
    return mens

class Preferences:
    def __init__(self, name, women):
        self.name = name
        self.women = women
        self.partner = None

    def __str__(self):
        return str(self.partner)
