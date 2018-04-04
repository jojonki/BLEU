from bleu import BLEU


mt = input()
refs = []
while True:
    try:
        ref = input()
        refs.append(ref)
    except EOFError:
        break

print('MT:', mt)
print('Refs:', refs)

bleu = BLEU()
print(bleu.modified_precision(4, mt, refs))
