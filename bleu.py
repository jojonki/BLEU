import copy
import math
from fractions import Fraction


def make_ngrams(sentence, N):
    ngrams = []
    for i in range(len(sentence) - N + 1):
        ngrams.append(' '.join(sentence[i:i+N]))
    return ngrams


def modified_precision(mt, refs, maxN=4, weights=None, epsilon=0.1):
    if weights is not None:
        assert(maxN == len(weights))

    Ns = range(1, maxN+1)
    Ps = []
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
        Ps.append(Fraction(clip_count, max(1, total), _normalize=False)) # ensures that denominator is minimum 1 to avoid ZeroDivisionError

    maxN = max(Ns)
    if weights is None:
        weights = [1 / maxN] * maxN

    # nltk prepares various smoothing functions. I used method1 implementation.
    # https://www.nltk.org/_modules/nltk/translate/bleu_score.html
    for i, p in enumerate(Ps):
        if p.numerator == 0:
            Ps[i] = epsilon / p.denominator

    return math.fsum([weights[i] * math.log(p) for i, p in enumerate(Ps)])


def closest_ref_length(c, ref_lens):
    return min(ref_lens, key=lambda ref_len: (abs(ref_len - c), ref_len))


def brevity_penalty(mt, refs):
    c = len(make_ngrams(mt, 1))
    ref_lens = [len(make_ngrams(ref, 1)) for ref in refs]
    r = closest_ref_length(c, ref_lens)
    if c >= r:
        return 1.0
    else:
        return math.exp(1.0 - r/c)


def calc_bleu(mt, refs, maxN=4, weights=None):
    # mt_ngrams = BLUE.make_ngrams(mt, maxN)
    # refs_ngrams = [BLUE.make_ngrams(ref, maxN) for ref in refs]
    bp = brevity_penalty(mt, refs)
    return bp * math.exp(modified_precision(mt, refs, maxN, weights))
