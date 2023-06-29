def pohon_ecxeption(clas_ini, nest = 0):
    if nest > 1:
        print("   |" * (nest - 1), end="")
    if nest > 0:
        print("   +---", end="")

    print(clas_ini.__name__)

    for subclass in clas_ini.__subclasses__():
        pohon_ecxeption(subclass, nest + 1)


pohon_ecxeption(BaseException)
    