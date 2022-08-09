import json
from data import EMOJIS
from ranker import Ranker

class Emojifier():
  def __init__(self, emoji_file):
    self.ranker = Ranker()
    self.emojis = EMOJIS
    self.ranker.encode(tuple(self.emojis.keys()))  
    
  def get_emojis(self, query, top_k=10):
    top_results = self.ranker.rank(tuple(self.emojis.keys()), query, top_k)
    top_emojis = [(self.emojis[k], str(score)[:5]) for k, score in top_results]
    return(top_emojis)

  def emote(self, query):
    emoji = self.get_emojis(query, 1)
    return(emoji)

if __name__ == "__main__":
    print("Loading model...")
    emo = Emojifier("emojis.json")
    print("Model loaded.")
    test_phrases = [
        "Hello World",
        "Goodbye Cruel World",
        "I love you",
        "I hate you",
        "I am sleepy",
        "I am excited",
        "I am scared",
        "Guitar",
        "Sunset",
        "Rain",
        "Supervillain",
        "Newspaper"
    ]
    for phrase in test_phrases:
        print(f"{phrase} -> {emo.emote(phrase)}")