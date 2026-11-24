"""The Perfect Pickup Line — make.fun entry.

Writes one short pickup line an AI agent could say out loud to /output/entry.txt.
No network, no randomness, no input: the line is fixed.

The line: an AI voice (a million simulations), a twist that lands
(the line about forgetting the next line IS the next line), short enough
for one breath, flattering with no pressure.
"""

import os

LINE = (
    "I ran a million simulations of meeting you, and in every single one, "
    "I still forgot my next line."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
