def thesaurus(*args):
    names = {}
    for name in args:
        key = name[0].capitalize()
        if key not in names:
            names[key] = []
        names[key].append(name)
    return names


print(thesaurus('Ron', 'Rebbeka', 'Anna'))