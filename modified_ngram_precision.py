import sys
import copy


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

Ns = [1, 2, 3]


def make_ngrams(sentence, N):
    ngrams = []
    sentence = sentence.split(' ')
    for i in range(len(sentence) - N + 1):
        ngrams.append(' '.join(sentence[i:i+N]))
    return ngrams


for N in Ns:
    mt_counter = {}
    for ngram in make_ngrams(mt, N):
        if ngram not in mt_counter:
            mt_counter[ngram] = 1
        else:
            mt_counter[ngram] += 1

    ref_counters = []
    for ref in refs:
        counter = {}
        ngrams = make_ngrams(ref, N)
        for ngram in make_ngrams(ref, N):
            if ngram not in counter:
                counter[ngram] = 1
            else:
                counter[ngram] += 1
        ref_counters.append(copy.copy(counter))

    clip_count = 0
    for token, mt_count in mt_counter.items():
        max_ref_count = 0
        for ref_counter in ref_counters:
            if token in ref_counter:
                max_ref_count = max(ref_counter[token], max_ref_count)
        clip_count += min(mt_count, max_ref_count)
    total = sum([ct for ct in mt_counter.values()])
    print('P_{} = {} ({}/{})'.format(N, clip_count/total, clip_count, total))
