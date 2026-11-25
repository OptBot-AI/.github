"""Swap the GIF row between <!-- optbot:gifs --> markers for a fresh random pick from the OPTBOT showcase
(the action scenes: launch, golf swing, hockey, ping pong, chef...). Usage: python3 rotate_gifs.py README.md [count] [height]"""
import json, random, re, sys, urllib.request

RAW = "https://raw.githubusercontent.com/OptBot-AI/.github/main/assets"
idx = json.load(urllib.request.urlopen(f"{RAW}/gifs/index.json"))
pool = idx.get("showcase") or [f"gifs/{n}" for v in idx["categories"].values() for n in v]
path, count, height = sys.argv[1], int(sys.argv[2]) if len(sys.argv) > 2 else 5, sys.argv[3] if len(sys.argv) > 3 else "96"
pick = random.sample(pool, count)
row = "\n".join(f'<img src="{RAW}/{p.split("/")[0]}/optbot-{p.split("/")[1]}.gif" height="{height}" alt="{p.split("/")[1]}" title="{p.split("/")[1]}">' for p in pick)
text = open(path).read()
assert "<!-- optbot:gifs -->" in text, "no markers"
open(path, "w").write(re.sub(r"(<!-- optbot:gifs -->).*?(<!-- /optbot:gifs -->)", lambda m: f"{m[1]}\n{row}\n{m[2]}", text, flags=re.S))
