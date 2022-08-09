# Simple command line chat interface that takes an argument of 
# an image file path and returns a string of the chatbot response.
import asyncio
import argparse
from rich import print
from people import Crowd

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Audience Simulator")
    parser.add_argument("image", help="Path to image to describe")
    parser.add_argument("-n", "--num_people", type=int, default=3, help="Number of characters in the crowd")
    parser.add_argument("-v", "--vibe", help="Vibe of the crowd (any phrase)", default="")
    args = parser.parse_args()

    crowd = Crowd(args.num_people, args.vibe)
    responses = asyncio.run(crowd.describe_image(args.image))
    for r in responses:
        print(r)