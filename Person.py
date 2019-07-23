class Person:
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex
        self._parents = []

    def set_parents(self, father, mother):
        self._parents.append(father)
        self._parents.append(mother)

    def parents(self):
        return self._parents


def chart(person):
    t = {}
    for i in range(1, 32):
        t[i] = '_______'

    t = update(t, person, 1)

    template = \
        (
                f"                                           |16 {t[16]}\n" +
                f"                                |08 {t[8]}\n" +
                f"                                |          |17 {t[17]}\n" +
                f"                     |04 {t[4]}\n" +
                f"                     |          |          |18 {t[18]}\n" +
                f"                     |          |09 {t[9]}\n" +
                f"                     |                     |19 {t[19]}\n" +
                f"          |02 {t[2]}\n" +
                f"          |          |                     |20 {t[20]}\n" +
                f"          |          |          |10 {t[10]}\n" +
                f"          |          |          |          |21 {t[21]}\n" +
                f"          |          |05 {t[5]}\n" +
                f"          |                     |          |22 {t[22]}\n" +
                f"          |                     |11 {t[11]}\n" +
                f"          |                                |23 {t[23]}\n" +
                f"01 {t[1]}\n" +
                f"          |                                |24 {t[24]}\n" +
                f"          |                     |12 {t[12]}\n" +
                f"          |                     |          |25 {t[25]}\n" +
                f"          |          |06 {t[6]}\n" +
                f"          |          |          |          |26 {t[26]}\n" +
                f"          |          |          |13 {t[13]}\n" +
                f"          |          |                     |27 {t[27]}\n" +
                f"          |03 {t[3]}\n" +
                f"                     |                     |28 {t[28]}\n" +
                f"                     |          |14 {t[14]}\n" +
                f"                     |          |          |29 {t[29]}\n" +
                f"                     |07 {t[7]}\n" +
                f"                                |          |30 {t[30]}\n" +
                f"                                |15 {t[15]}\n" +
                f"                                           |31 {t[31]}\n"
        )

    return template


def update(tracer, person, place):

    tracer[place] = person.name
    if place > 15:
        return tracer

    parents = person.parents()
    if len(parents) == 0:
        return tracer

    for parent in parents:
        if parent.sex == 'M':
            update(tracer, parent, place=2*place)
        elif parent.sex == 'F':
            update(tracer, parent, place=2*place+1)

    return tracer


def main():
    sansa = Person(name='Sansa', sex='F')
    catelyn = Person(name='Catelyn', sex='F')
    ned = Person(name='Ned', sex='M')

    sansa.set_parents(father=ned, mother=catelyn)

    print(chart(sansa))


if __name__ == "__main__":
    main()
