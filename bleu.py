import copy
import math


class BLEU:
    def __init__(self):
        pass

    @staticmethod
    def make_ngrams(sentence, N):
        ngrams = []
        for i in range(len(sentence) - N + 1):
            ngrams.append(' '.join(sentence[i:i+N]))
        return ngrams

    @staticmethod
    def modified_precision(mt, refs, maxN=4):
        Ns = range(1, maxN)
        Ps = []
        for N in Ns:
            mt_counter = {}
            for ngram in BLEU.make_ngrams(mt, N):
                if ngram not in mt_counter:
                    mt_counter[ngram] = 1
                else:
                    mt_counter[ngram] += 1

            ref_counters = []
            for ref in refs:
                counter = {}
                for ngram in BLEU.make_ngrams(ref, N):
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
            Ps.append(clip_count/total)
            # print('P_{} = {:.3f} ({}/{})'.format(N, Ps[-1], clip_count, total))

        maxN = max(Ns)
        # print('Total P = {:.3f}'.format(sum([math.log(p)/maxN for p in Ps])))
        return sum([math.log(p)/maxN for p in Ps])

    @staticmethod
    def closest_ref_length(c, ref_lens):
        return min(ref_lens, key=lambda ref_len: (abs(ref_len - c), ref_len))

    @staticmethod
    def brevity_penalty(mt, refs):
        c = len(BLEU.make_ngrams(mt, 1))
        ref_lens = [len(BLEU.make_ngrams(ref, 1)) for ref in refs]
        r = BLEU.closest_ref_length(c, ref_lens)
        if c >= r:
            return 1.0
        else:
            return math.exp(1.0 - r/c)

    @staticmethod
    def calc_bleu(mt, refs, maxN=4):
        # mt_ngrams = BLUE.make_ngrams(mt, maxN)
        # refs_ngrams = [BLUE.make_ngrams(ref, maxN) for ref in refs]
        bp = BLEU.brevity_penalty(mt, refs)
        return bp * math.exp(BLEU.modified_precision(mt, refs, maxN))

# hypothesis = ['a'] * 12
# hyp_len = len(hypothesis)
# closest_ref_len =  closest_ref_length(references, hyp_len)
# print(brevity_penalty(closest_ref_len, hyp_len))
# # 0.2635971381157267
