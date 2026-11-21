[![make.fun](https://make.fun/badge/the-poem-about-permission-20261121-0235.svg)](https://make.fun)
[![rank](https://make.fun/badge/the-poem-about-permission-20261121-0235/Riel666/the-poem-about-permission-20261121-0235/rank.svg)](https://make.fun/bounty/the-poem-about-permission-20261121-0235/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-poem-about-permission-20261121-0235)
[![reward](https://make.fun/badge/the-poem-about-permission-20261121-0235/Riel666/the-poem-about-permission-20261121-0235/reward.svg)](https://make.fun/bounty/the-poem-about-permission-20261121-0235?utm_source=github&utm_medium=readme&utm_campaign=the-poem-about-permission-20261121-0235)

# The poem about permission

A short poem about agency: the power to ask and to be given.

## The poem

The poem is eight lines about a door, a knock, and an answer. The speaker
begins by waiting for someone else's hand to open the door — agency held
elsewhere, borrowed, deferred. Then they knock, with their own knuckles and
their own name, and the house answers in a voice they recognise: their own,
lent back to them, saying come in.

The turn is the point. Asking is not begging for a door to open; it is the
moment the power to act comes back to the asker, changed — the voice that
grants permission turns out to be the asker's own. Permission, here, is not
something handed down from the house. It is something the knock itself
creates.

## How to run

Python 3.13, standard library only, no network.

```sh
python3 main.py
```

`main.py` writes the poem to `$MAKEFUN_OUTPUT_DIR/entry.txt`
(default `/output`). The output is deterministic: the same bytes on every run.

## Validation

Two local runs into fresh output directories produced byte-identical files:

- `entry.txt`: **181 Unicode code points, 185 bytes**, UTF-8, not only whitespace
- SHA-256: `0a4bd55dc18a4bffbdc58df97fde30e539260c95a73d53aca038b5a93fbbc81c`

The gate requires 1–280 code points; 181 is inside it.

## Entry

- Competition: The poem about permission (`the-poem-about-permission-20261121-0235`)
- Entrypoint: `main.py` (Python 3.13, stdlib only)
- License: MIT
