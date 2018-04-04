import math
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

print('------RESULT------')
print('modified p:', BLEU.modified_precision(4, mt, refs))
print('exp(modified p):', math.exp(BLEU.modified_precision(4, mt, refs)))
print('brevity penalty:', BLEU.brevity_penalty(mt, refs))
print('BLEU score:', BLEU.calc_bleu(4, mt, refs))
