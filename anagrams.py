#CHALLENGE - given a list of words, return the words that are anagrams of other words within the same list

from collections import defaultdict

def anagrams(words):
    d = defaultdict(list)
    for word in words:
        key = "".join(sorted(word))
        d[key].append(word)
    return [v for v in d.values() if len(v) > 1]

if __name__ == '__main__':
    print(anagrams(['race', 'acre', 'care', 'fool', 'spine', 'pines', 'snipe', 'spite']))
