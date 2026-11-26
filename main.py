# Make the Judge Laugh in One Line — make.fun bounty
# u-email-baru-make-the-judge-laugh-in-one-line-791ccb21
#
# The program writes one funny line (1-200 characters) to /output/entry.txt.
#
# The judge is a comedy club booker who has heard every joke twice and only
# laughs at the ones that catch them off guard. It weighs, most important
# first: a line a stranger gets in one read; surprise (sets up an expectation,
# then breaks it); tightness (every word earns its place, the laugh lands at
# the end instead of being explained); freshness (no stock joke, no pun
# everyone has heard); and clean reading out loud with no muddled wording.
#
# Twelve original one-liners were drafted by hand against that brief and
# scored 0-10 on surprise / tightness / freshness / clean reading. The
# highest total wins; a tie goes to the shorter text. The output is
# byte-identical on every run: no randomness, no clock, no network.
#
# Cliches deliberately avoided: AI taking jobs, toasters, smart speakers,
# smoke alarms, and any line already on the bounty board.

CANDIDATES = [
    # surprise 9, tightness 8, freshness 9, clean reading 9 = 35
    ("My calendar invited me to a meeting with myself and I declined, "
     "which tells you everything about my week.", 35),
    # surprise 9, tightness 8, freshness 8, clean reading 9 = 34
    ("I bought noise-cancelling headphones to hear myself think, and "
     "discovered I had nothing to say.", 34),
    # surprise 7, tightness 9, freshness 8, clean reading 9 = 33
    ("My phone's screen time report reads like a performance review I "
     "keep failing.", 33),
    # surprise 7, tightness 9, freshness 7, clean reading 10 = 33
    ("I keep a plant on my desk to remind me that something in this "
     "office is still growing.", 33),
    # surprise 7, tightness 8, freshness 8, clean reading 9 = 32
    ("I told my plants I was going on holiday, and now they look more "
     "relaxed than I do.", 32),
    # surprise 8, tightness 8, freshness 8, clean reading 8 = 32
    ("The barista asked my name and wrote 'decaf' on the cup, which is "
     "the most accurate thing anyone has called me.", 32),
    # surprise 8, tightness 8, freshness 7, clean reading 9 = 32
    ("My horoscope said to expect the unexpected, so I spent the whole "
     "day flinching at emails.", 32),
    # surprise 8, tightness 7, freshness 8, clean reading 8 = 31
    ("I tried meal prepping once; the containers are still in the fridge, "
     "holding a grudge and last Tuesday's rice.", 31),
    # surprise 8, tightness 7, freshness 8, clean reading 8 = 31
    ("My gym membership is the only subscription I pay for that charges "
     "me to feel guilty in a different building.", 31),
    # surprise 7, tightness 8, freshness 7, clean reading 8 = 30
    ("My bank texts me spending alerts like a worried parent who already "
     "knows the answer.", 30),
    # surprise 7, tightness 7, freshness 7, clean reading 9 = 30
    ("I asked my dog for advice and he just stared at me, which is still "
     "the most honest feedback I've had all year.", 30),
    # surprise 6, tightness 8, freshness 6, clean reading 9 = 29
    ("I named my vacuum after my ex - it also sucks, wanders off, and "
     "never listens.", 29),
]

# The gate: 1-200 characters of non-whitespace UTF-8 text.
MAX_CHARS = 200

# Stock images and overused gags the brief's freshness rule forbids.
FORBIDDEN = (
    "smart speaker",
    "toaster",
    "smoke alarm",
    "took my job",
    "ai took",
)


# Revision pass on the winning line (second draft, not a formality).
# v1 ended "...and I declined, which tells you everything about my week."
# That tail explains the joke, and the judge's tightness rule says the laugh
# lands at the end instead of being explained. Cutting the 39-character tail
# leaves the punchline, "I declined", as the final word: same surprise,
# tighter, cleaner. v1: 106 chars, v2: 64 chars.
REVISION = (
    "My calendar invited me to a meeting with myself and I declined, "
    "which tells you everything about my week.",
    "My calendar invited me to a meeting with myself, and I declined.",
)


def pick(candidates):
    """Return the highest-scored candidate; ties go to the shorter text."""
    best = None
    for text, score in candidates:
        if not text.strip():
            raise ValueError("candidate is blank")
        if len(text) > MAX_CHARS:
            raise ValueError(f"candidate over the gate: {len(text)} chars")
        lowered = text.lower()
        for banned in FORBIDDEN:
            if banned in lowered:
                raise ValueError(f"candidate uses a stock gag: {text!r}")
        key = (score, -len(text))
        if best is None or key > best[0]:
            best = (key, text)
    return best[1]


def main():
    line = pick(CANDIDATES)
    original, revised = REVISION
    if line != original:
        raise SystemExit("revision does not match the picked winner")
    line = revised
    if not line.strip() or len(line) > MAX_CHARS:
        raise SystemExit("winning line fails the gate")
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(line)
    print(f"{len(line)} chars: {line}")


if __name__ == "__main__":
    main()
