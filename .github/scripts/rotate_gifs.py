"""Swap the GIF row between <!-- optbot:gifs --> markers for a fresh random pick from the approved OPTBOT library.
Usage: python3 rotate_gifs.py README.md [count] [height]"""
import json, random, re, sys, urllib.request

RAW = "https://raw.githubusercontent.com/OptBot-AI/.github/main/assets"
idx = json.load(urllib.request.urlopen(f"{RAW}/gifs/index.json"))
names = [n for v in idx["categories"].values() for n in v]
path, count, height = sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else 5, sys.argv[3] if len(sys.argv) > 3 else "88"
row = "\n".join(f'<img src="{RAW}/gifs/optbot-{n}.gif" height="{height}" alt="{n}" title="{n}">' for n in random.sample(names, count))
text = open(path).read()
new = re.sub(r"(<!-- optbot:gifs -->).*?(<!-- /optbot:gifs -->)", lambda m: f"{m[1]}\n{row}\n{m[2]}", text, flags=re.S)
assert new != text or "<!-- optbot:gifs -->" in text, "no markers"
open(path, "w").write(new)
