# BLEU

## How to use?

You can pass a test file by the following command line.
The mt text and refercnes are written in test files which the first line is mt and the second and subsequent lines are refercnes. See the exmaples in `test/`.
```
python test.py  < tests/sample2.txt
MT: it is a guide to action which ensures that the military always obyes the commands of the party
Refs: ['it is a guide to action that ensures that the military will forever heed party commands', 'it is the guiding principle which guarantees the military forces always being under the command of the party', 'it is the practical guide for the armyh always to heed the directions of the party']
------RESULT------
modified p: -0.471488412695529
exp(modified p): 0.6240726989348756
brevity penalty: 0.1427288631175674
BLEU score: 0.08907318682168672
```

## References
[自動評価尺度 BLEU](http://www2.nict.go.jp/astrec-att/member/mutiyama/corpmt/4.pdf)
