"""One Word for the Boss.

Writes exactly one word describing the boss to /output/entry.txt.

The word is "Megaphone": the boss who never has an original idea of
their own, but broadcasts yours louder and takes the applause.
One concrete object, one beat, deadpan. It is funny because it is
true, and it travels to any workplace.
"""

from pathlib import Path

WORD = "Megaphone"

OUTPUT_PATH = Path("/output/entry.txt")


def validate(word: str) -> str:
    """Enforce the kit gate: one word, 1 to 30 characters, not blank."""
    text = word.strip()
    if not text:
        raise ValueError("entry word must not be blank")
    if len(text.split()) != 1:
        raise ValueError("entry must be exactly one word")
    if len(text) > 30:
        raise ValueError("entry must be at most 30 characters")
    return text


def main() -> None:
    word = validate(WORD)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(word, encoding="utf-8")


if __name__ == "__main__":
    main()
