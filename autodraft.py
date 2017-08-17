
import glob, os, sys, re, pyperclip

def is_numeric(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

path = os.path.join(os.getcwd(), 'templates')

if not os.path.exists(path):
    os.mkdir(path)

os.chdir(path)

files = glob.glob('*.txt')

if len(files) == 0:
    print("\nYou have no template files located at " + path + "\n")
    sys.exit()

print("\nSelect a template:")

for file in files:
    print("{}) {}".format(files.index(file) + 1, file.replace('.txt','')))

print()

while True:
    s = input()

    if not is_numeric(s):
        print("Invalid input. Enter a number to select a template.")
        continue

    i = int(s)

    if i < 1 or i > len(files):
        print("Invalid input. Select the index of the desired template.")
        continue

    break

selText = open(files[i - 1]).read()
idx = [m.start() for m in re.finditer('{{', selText)]
strMap = []

for i in idx:
    s = selText[i:selText.find('}}', i) + 2]
    duplicate = False
    for x in strMap:
        if x[0] == s:
            duplicate = True
    if not duplicate:
        strMap.append((s, input(s.replace('{{','').replace('}}','') + ': ')))

for x in strMap:
    selText = selText.replace(x[0], x[1])

pyperclip.copy(selText)
