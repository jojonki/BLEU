class BLEU:
    def __init__(self):
        pass

    @staticmethod
    def make_ngrams(sentence, N):
        ngrams = []
        sentence = sentence.split(' ')
        for i in range(len(sentence) - N + 1):
            ngrams.append(' '.join(sentence[i:i+N]))
        return ngrams
