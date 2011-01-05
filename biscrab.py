#!/usr/bin/python

import os
import sys
from collections import defaultdict

points = defaultdict(lambda:1)
points.update(
 b=3, c=3, d=2, f=4, g=2,h=4, j=8, k=5,
 m=3, p=3, q=10, v=4, w=4, x=8, y=4, z=10,
)

letters = [
  'a','b','c','d','e','f','g','h','i','j','k','l','m',
  'n','o','p','q','r','s','t','u','v','w','x','y','z',
]

def read_input():
  while 1:
    try:
      line = raw_input()
      yield line.lower()
    except EOFError:
      return

def letter_pairs(word):
  pairs = set()
  for i in range(0,len(word)-1):
    for j in range(i+1,len(word)):
      if word[i] < word[j]:
        pairs.add(tuple([word[i], word[j]]))
      else:
        pairs.add(tuple([word[j], word[i]]))
  return pairs

def score_combos():
  combos = defaultdict(lambda:0)
  for word in read_input():
    score = sum(points[l] for l in word)
    for (a,b) in letter_pairs(word):
      combos[(a, b)] += score
  return combos

def weighted_combos():
  combos = score_combos()
  minp = min(combos.values())
  maxp = max(combos.values())
  def weight(a, b):
    if (a,b) in combos:
      return float(combos[(a,b)]-minp)/(maxp-minp)
    else:
      return 0
  weighted = dict()
  for a in letters:
    for b in letters:
      if a <= b:
        weighted[(a,b)] = weight(a,b)
  return weighted

def main():
  combos = weighted_combos()
  if 'html' in sys.argv:
    from Cheetah.Template import Template
    print Template(
      file('biscrab.html.template').read(),
      searchList=[dict(
        combos=combos,
        letters=letters,
      )])
  else:
    print combos

if __name__ == '__main__':
  main();
