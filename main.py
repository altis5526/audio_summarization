from pytube import YouTube
from pydub import AudioSegment
import openai
import argparse
from audio2text import audio2text
from summarize import summarize

if __name__ == "__main__":
    arg = argparse.ArgumentParser()
    arg.add_argument("--audio", type=str, default="test.m4a")
    arg.add_argment("--text", type=str, default="test.txt")
    args = arg.parse_args()

    api_key = "YOUR_API_KEY"
    
    audio2text(api_key, args.audio, args.text)
    summarize(api_key, args.text_file)