"""One-line comedy entry for the make.fun bounty
u-email-baru-make-the-judge-laugh-in-one-line-791ccb21.
A dozen hand-written one-liners are graded on four axes, the strongest one
is kept, and a single tightening pass trims its tail so the punchline lands
last. The finished line is written to /output/entry.txt. Runs are pure and
repeatable: no dice rolls, no wall clock, no network, no files read."""
from pathlib import Path as _Path
_CHAR_CAP = 200
_FINAL_LEN = 64
_BANNED_BITS = ("took my job", "toaster", "smart speaker", "smoke alarm", "ai took")
_DRAFT_HEAD = "My calendar invited me to a meeting with myself"
_DRAFT_TAIL = " and I declined, which tells you everything about my week."
_TIGHT_TAIL = ", and I declined."
_DRAFTS = (
    {"line": ("My calendar invited me to a meeting with myself and I declined,"
              " which tells you everything about my week."),
     "marks": (9, 8, 9, 9)},
    {"line": ("I bought noise-cancelling headphones "
              "to hear myself think, and discovered I had nothing to say."),
     "marks": (9, 8, 8, 9)},
    {"line": ("My phone's screen time "
              "report reads like a performance review I keep failing."),
     "marks": (7, 9, 8, 9)},
    {"line": ("I keep a plant on my desk to "
              "remind me that something in this office is still growing."),
     "marks": (7, 9, 7, 10)},
    {"line": ("I told my plants I "
              "was going on holiday, and now they look more relaxed than I do."),
     "marks": (7, 8, 8, 9)},
    {"line": ("The barista asked my name and "
              "wrote 'decaf' on the cup, which is the most accurate thing anyone has called me."),
     "marks": (8, 8, 8, 8)},
    {"line": ("My horoscope said to expect the unexpected, so "
              "I spent the whole day flinching at emails."),
     "marks": (8, 8, 7, 9)},
    {"line": ("I tried meal prepping once; the "
              "containers are still in the fridge, holding a grudge and last Tuesday's rice."),
     "marks": (8, 7, 8, 8)},
    {"line": ("My gym membership is the only subscription I "
              "pay for that charges me to feel guilty in a different building."),
     "marks": (8, 7, 8, 8)},
    {"line": ("My bank texts me spending alerts like "
              "a worried parent who already knows the answer."),
     "marks": (7, 8, 7, 8)},
    {"line": ("I asked my dog for advice and "
              "he just stared at me, which is still the most honest feedback I've had all year."),
     "marks": (7, 7, 7, 9)},
    {"line": ("I named my vacuum after "
              "my ex - it also sucks, wanders off, and never listens."),
     "marks": (6, 8, 6, 9)})
def _total(entry):
    return sum(entry["marks"])
def _validate_table(drafts):
    seen = set()
    for entry in drafts:
        text = entry["line"]
        if text in seen:
            raise SystemExit("two drafts share the same text")
        seen.add(text)
        for mark in entry["marks"]:
            if mark < 0 or mark > 10:
                raise SystemExit(f"a mark sits outside 0-10: {mark}")
    if len(drafts) != 12:
        raise SystemExit(f"expected 12 drafts, found {len(drafts)}")
def _ranked(drafts):
    return sorted(drafts, key=lambda d: (-_total(d), len(d["line"])))
def _screen(line):
    if line != line.strip() or not line:
        raise SystemExit("entry text is blank or padded with whitespace")
    if len(line) > _CHAR_CAP:
        raise SystemExit(f"entry text runs {len(line)} characters, over the 200 cap")
    if "\n" in line or "\r" in line:
        raise SystemExit("entry text must stay on one line")
    folded = line.lower()
    for bit in _BANNED_BITS:
        if bit in folded:
            raise SystemExit(f"entry text leans on a tired gag: {bit}")
def _tighten(line):
    if line != _DRAFT_HEAD + _DRAFT_TAIL:
        raise SystemExit("tightening only knows the winning first draft")
    return _DRAFT_HEAD + _TIGHT_TAIL
def run():
    _validate_table(_DRAFTS)
    ordered = _ranked(_DRAFTS)
    top = ordered[0]["line"]
    _screen(top)
    if _total(ordered[0]) <= _total(ordered[1]):
        raise SystemExit("top two drafts tie, so no single winner exists")
    final = _tighten(top)
    _screen(final)
    if len(final) != _FINAL_LEN:
        raise SystemExit(f"tightened line is {len(final)} characters, expected 64")
    if final != _DRAFT_HEAD + _TIGHT_TAIL:
        raise SystemExit("tightened line is not the expected final text")
    _Path("/output").mkdir(parents=True, exist_ok=True)
    _Path("/output/entry.txt").write_text(final, encoding="utf-8")
    print(f"entry is {len(final)} characters long: {final}")
_GUARD = "__main__"
if __name__ == _GUARD:
    run()
