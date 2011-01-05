# biscrab

**biscrab** is a tool for measuring the score potential of letter pairs in Scrabble.

The score potential of a pair `(x,y)` is defined as the sum of the base scores of all words that contain both `x` and `y`. If `x` and `y` are the same letter, then the words must contain at least two of the letter.

The corpus of words are accepted as standard input to `biscrab.py`. The default output is a serialized python dictionary of the weighted scores of each letter pair. The weight of the pair `(x,y)` is computed as `(potential(x,y)-minimum)/(maximum-minimum)`, where `minumum` and `maximum` are the minumum and maximum score potentials of all pairs.

Pass in an "html" parameter to produce HTML output with [Cheetah](http://cheetahtemplate.org/).

# example

    egrep "^.{2,6}$" /usr/share/dict/words | python biscrab.py html > biscrab.html

![Example output](https://github.com/tantalor/biscrab/raw/master/example.png)
