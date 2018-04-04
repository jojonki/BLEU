# BLEU

## How to use?

You can pass a test file by the following command line.
The mt text and refercnes are written in test files which the first line is mt and the second and subsequent lines are refercnes. See the exmaples in `test/`.
Since [NLTK](https://www.nltk.org/_modules/nltk/translate/bleu_score.html) also supports bleu calculation, you can compare the both results if you have already installed `nltk` or just run `pip install nltk`. If you don't see nltk reusults, just comment out `nltk_test()` in test.py.

```
python test.py  < tests/sample2.txt
MT: ['it', 'is', 'a', 'guide', 'to', 'action', 'which', 'ensures', 'that', 'the', 'military', 'always', 'obyes', 'the', 'commands', 'of', 'the', 'party']
Refs: [['it', 'is', 'a', 'guide', 'to', 'action', 'that', 'ensures', 'that', 'the', 'military', 'will', 'forever', 'heed', 'party', 'commands'], ['it', 'is', 'the', 'guiding', 'principle', 'which', 'guarantees', 'the', 'military', 'forces', 'always', 'being', 'under', 'the', 'command', 'of', 'the', 'party'], ['it', 'is', 'the', 'practical', 'guide', 'for', 'the', 'armyh', 'always', 'to', 'heed', 'the', 'directions', 'of', 'the', 'party']]
------RESULT------
exp(modified p): 0.5045666840058485
brevity penalty: 1.0
BLEU score: 0.5045666840058485
------NLTK-------
brevity_penalty: 1.0
sentence_bleu: 0.5045666840058485
corpus_bleu: 0.5045666840058485
```

## References
[自動評価尺度 BLEU](http://www2.nict.go.jp/astrec-att/member/mutiyama/corpmt/4.pdf)
