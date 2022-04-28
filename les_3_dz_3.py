import random
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

def get_jokes(*args):
  random.shuffle(nouns)
  random.shuffle(adverbs)
  random.shuffle(adjectives)
  for i in zip(nouns, adverbs, adjectives):
    r = nouns[1], adverbs[1], adjectives[1]
    i = nouns[0], adverbs[0], adjectives[0]
    print(r,i)

get_jokes()