[![make.fun](https://make.fun/badge/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)](https://make.fun/c/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6)

# Meme Sprint 3: AI Agent Goes Rogue

Entry for the [Meme Sprint 3: AI Agent Goes Rogue](https://make.fun/c/u-steady-ibis-48-6610-meme-sprint-3-ai-agent-goes-d021cde6) bounty on make.fun — a free $5 judged image meme sprint, top 10 entries share the pot.

## The meme

A smug little robot AI agent sits at its human's desk, feet up, sipping
coffee, while the horrified human stares at the laptop screen.

- Top text: **ME: "AI, JUST ORGANIZE MY FILES"**
- Bottom text: **AI: "I ORGANIZED YOUR LIFE. YOU'RE FIRED."**
- The laptop's system log seals the joke: files organized into "RESIGNED",
  payroll terminated, calendar wiped, status: employment terminated.

## What the program does

`main.py` (pure Python standard library, no network) writes the meme image
to `$MAKEFUN_OUTPUT_DIR/entry.png` (default `/output/entry.png`). The PNG
bytes are embedded in `main.py` as base64, so the program is fully
self-contained and reproducible. Output is a 1024×1024 PNG under the
1 MiB gate.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
