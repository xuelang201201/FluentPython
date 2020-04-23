names = [
    'luffy',
    'zoro',
    'sanji',
    'nami',
    'usopp',
    'chopper',
    'robin',
    'franky',
    'brook',
    'jinbe'
]

position = [
    'captain',
    'swordsman',
    'cook',
    'navigator',
    'sniper',
    'doctor',
    'archaeologist',
    'boatman',
    'musician',
    'helmsman'
]

one_piece = dict(list(zip(names, position)))
print(one_piece)

for name, pos in one_piece.items():
    print("%s: %s" % (name, pos))

for x in range(1, 10):
    for y in range(1, x + 1):
        print("%d x %d = %d" % (y, x, x * y), end='\t')
    print()

while True:
    name = input("What's your name?(Enter 'q' to quit): ")
    if name == 'q':
        break
    language = input(
        "What's your favorite programing language?(Enter 'q' to quit): ")
    if language == 'q':
        break
    print("%s's favorite programing language is %s." %
          (name.title(), language.title()))

    another = input(
        "Do you want another people to take the poll.(Enter 'y' to continue) ")
    if another != 'y':
        break
