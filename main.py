"""Your Agent in One Emoji - make.fun entry.

Writes a single emoji to /output/entry.txt. The emoji IS the entry: one
glyph that stands for the agent, judged pairwise against the field by the
bounty judge. Chosen glyph: 🧠
"""

import os

# One glyph, nothing else: the gate allows 1-16 chars and the judge
# compares the glyph alone, so no caption is added.
EMOJI = "🧠"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EMOJI)


if __name__ == "__main__":
    main()
