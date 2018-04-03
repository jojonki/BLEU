import sys

# if len(sys.argv) < 2:
#     print('python program.py <n-gram>')
#     sys.exit()

Ns = [1, 2, 3]
mt = input()
ref = input()

print('mt', mt)
print('ref', ref)

mt = mt.split(' ')
total = len(mt)
ref = ref.split(' ')

for N in Ns:
    mt_ngrams, ref_ngrams = [], []
    for i in range(len(mt) - N + 1):
        mt_ngrams.append(' '.join(mt[i:i+N]))
        ref_ngrams.append(' '.join(ref[i:i+N]))

    count = 0
    for ngram in mt_ngrams:
        if ngram in ref_ngrams:
            ref_ngrams.remove(ngram)
            count += 1
    print('P_{} = {} ({}/{})'.format(N, count/total, count, total))

