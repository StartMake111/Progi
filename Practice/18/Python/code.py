import string
check_words = ['hallo', 'klempner','das','ist','fantastisch','fluggegecheimen']
dl = 0
word = input()
word = list(word)
chance = {}
schetchick = {}
for string in string.ascii_lowercase:
    chance[string] = schetchick[string] = 0
for wond in check_words:
    dl += len(wond)
    for F in wond:
        schetchick[F] += 1
for buckv in schetchick:
    chance[buckv] = schetchick[buckv] / dl
chance_proiznesti = 1
for i in range(len(word)):
    if chance[word[i]] == 0:
        continue
    chance_proiznesti *= chance[word[i]]
print(format(chance_proiznesti,'.2e'))