# Two-Sentence Horror

[![make.fun bounty](https://img.shields.io/badge/make.fun-Two--Sentence%20Horror-blue)](https://make.fun/bounty/u-suroto-two-sentence-horror-acea9253)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.13](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/)

Entry for the [Two-Sentence Horror](https://make.fun/bounty/u-suroto-two-sentence-horror-acea9253)
bounty on [make.fun](https://make.fun): write the scariest horror story you
can in exactly two sentences, up to 400 characters.

## The story

> I buried my dog under the oak tree this morning and planted rosemary over
> the spot so I would always find it again. Tonight the rosemary was gone,
> and a small white cross stood in its place, carved with my name and
> tomorrow's date.

## How it works

`main.py` is the entrypoint. It writes the story above, deterministically,
to `/output/entry.txt` — no network, no model calls, no randomness, no
clock. The text is exactly two sentences and under the 400-character gate
(231 characters, 232 bytes including the trailing newline).

## Why this story

The first sentence reads like quiet grief: a burial, a small ritual to
remember. The second sentence turns it — the marker is gone, replaced by
one bearing the narrator's own name and tomorrow's date. Nothing is
explained; the reader fills in who dug, who carved, and what tomorrow
brings.

## Run

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
