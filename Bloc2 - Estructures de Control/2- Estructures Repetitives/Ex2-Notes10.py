totalNotes = 0
totalNotes10 = 0

notaEntrada = int(input())
while notaEntrada != -1:
    if notaEntrada in range(0,11):
        totalNotes += 1
    if notaEntrada == 10:
        totalNotes10 += 1
    notaEntrada = int(input())

print("TOTAL NOTES: {} NOTES10: {}".format(totalNotes,totalNotes10))