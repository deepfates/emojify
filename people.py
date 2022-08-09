import asyncio
from random import choice, randint


from emojify import Emojifier
from ranker import Ranker
from describe import describe
from data import CHARACTERS

class Person():
    def __init__(self, personality: str = "Creative"):
        self.personality = personality
        self.character = CHARACTERS[self.personality]

    def __repr__(self):
        return(f"{self.character} ({self.personality})")

    def format_response(self, response):
        return(f"\n\n{self.character}:\n\t\t{response}")       
        return(f"\n\n{self.character} ({self.personality}):\n\t\t{response}")       

    async def describe_image(self, img):
        description = await describe(img, [self.personality])
        return(self.format_response(choice(description)))

class Crowd():
    def __init__(self, n_chars: int = 10, vibe: str = ""):
        self.ranker = Ranker()
        self.n_chars = n_chars
        self.characters = CHARACTERS
        self.vibe = vibe
        if self.vibe:
            personalities = self.get_similar_characters(self.vibe)
        else:
            personalities  = [self.get_random_character() for _ in range(self.n_chars)]
        self.people = {p:Person(p) for p in personalities}
        self.emo = Emojifier('emoji.json')

    def __repr__(self):
        return(f"{self.vibe} crowd of {self.n_chars} people: {[v for v in self.people.values()]}")

    def get_random_character(self):
        return(choice(list(self.characters.keys())))
    
    def get_similar_characters(self, vibe):
        return([p for p, _ in self.ranker.rank(self.characters.keys(), vibe, self.n_chars)])

    def respond_with_emote(self, personality, msg):
        response = self.people[personality].format_response(msg)
        emoji = ""
        num_emojis = randint(0, 5)
        emoji = [emoji for emoji, _ in self.emo.get_emojis(msg, num_emojis)]
        return f"{response} {''.join(emoji)}"

    async def describe_image(self, img):
        descriptions = await describe(img, self.people.keys())
        responses =  [self.respond_with_emote(p, choice(desc)) for p, desc in descriptions]
        return(responses)


if __name__ == "__main__":
    crowd = Crowd(3, vibe="Kind")
    responses = asyncio.run(crowd.describe_image("test.jpeg"))
    for r in responses:
        print(r)