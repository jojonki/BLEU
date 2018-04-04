import math
from bleu import brevity_penalty, modified_precision, calc_bleu


mt = input().split(' ')
refs = []
while True:
    try:
        ref = input()
        refs.append(ref.split(' '))
    except EOFError:
        break

print('MT:', mt)
print('Refs:', refs)


def test():
    print('------RESULT------')
    # print('modified p:',      modified_precision(mt, refs))
    print('exp(modified p):', math.exp(modified_precision(mt, refs)))
    print('brevity penalty:', brevity_penalty(mt, refs))
    print('BLEU score:',      calc_bleu(mt, refs))


def nltk_test():
    print('------NLTK-------')
    from nltk.translate.bleu_score import closest_ref_length, brevity_penalty, sentence_bleu, corpus_bleu, SmoothingFunction
    # from nltk_bleu import closest_ref_length, brevity_penalty, sentence_bleu, corpus_bleu, SmoothingFunction # from local file
    # nltk.translatel.bleu == sentence_bleu
    sm_func = SmoothingFunction().method1
    print('brevity_penalty:', brevity_penalty(closest_ref_length(refs, len(mt)), len(mt)))
    print('sentence_bleu:',   sentence_bleu(refs, mt, smoothing_function=sm_func))
    print('corpus_bleu:',     corpus_bleu([refs], [mt], smoothing_function=sm_func))


test()
nltk_test()
