from functools import lru_cache
import logging
from typing import Union
from sentence_transformers import SentenceTransformer, util # type: ignore

class Ranker():
  def __init__(self):
    self.model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

  @lru_cache(maxsize=None)
  def _encode(self, text: Union[tuple, str]):
    logging.debug("NOT CACHED. Encoding", text)
    embedding = self.model.encode(text, convert_to_tensor=True)
    return(embedding)

  def encode(self, text):
    if type(text) is str:
      embedding = self._encode(text)
    else:
      embedding = self._encode(tuple(text))
    return(embedding)

  def score(self, texts, query):
    query_embed= self.encode(query)
    texts_embed = self.encode(texts)
    scores = util.pytorch_cos_sim(query_embed, texts_embed)
    return(tuple(zip(texts, scores.tolist()[0])))

  def rank(self, texts, query, top_k):
    scores = self.score(texts, query)
    sorted_scores = sorted(scores, key=lambda x: x[1], reverse=True)
    return(sorted_scores[:top_k])
