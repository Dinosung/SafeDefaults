"""Generate README.md from data/tips.yaml. Run: python3 scripts/build_readme.py"""
import pathlib

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
GRADES = {
    "A": ("🟢 A", "Measured: following it means fewer infections, hijacks or compromises"),
    "B": ("🟡 B", "Indirect: attack simulations, update uptake, or how common the threat is"),
    "C": ("⚪ C", "No direct evidence found that it helps: often sensible, just unmeasured"),
    "X": ("🔴 X", "Evidence against: little or no measured value, or it backfires"),
}
AREAS = ["Accounts", "Updates & software", "Devices", "Network & messaging", "Scams & privacy"]


def load() -> list[dict]:
    return yaml.safe_load((ROOT / "data" / "tips.yaml").read_text())


def link(src: dict) -> str:
    return f"[{src['title']}, {src['year']}]({src['url']})"


def row(t: dict) -> str:
    evidence = link(t["source"]) if "source" in t else ""
    if "also" in t:
        evidence += "; " + link(t["also"])
    note = t["finding"] + (f" *{t['caveat']}*" if t.get("caveat") else "")
    return f"| {GRADES[t['grade']][0]} | **{t['tip']}** | {note} | {evidence} | {t['rank']} |"


def render(tips: list[dict]) -> str:
    count = {g: sum(t["grade"] == g for t in tips) for g in GRADES}
    out = [
        "# SafeDefaults",
        "",
        f"**The {len(tips)} security tips experts rank highest, graded by the evidence that they work.**",
        "",
        f"Only **{count['A']}** have measured proof that they prevent harm. **{count['C']}** have no direct "
        f"evidence at all. **{count['X']}**, several of them on popular checklists, have evidence against them.",
        "",
        "Every grade links to its source. Disagree with one? [Open an issue with better evidence](CONTRIBUTING.md).",
        "",
        "## Grades",
        "",
        "| Grade | Meaning |",
        "|---|---|",
        *[f"| {label} | {meaning} |" for label, meaning in GRADES.values()],
        "",
        "## Start here: the tips with measured proof",
        "",
        *[f"1. **{t['tip']}**: {t['finding']}" for t in tips if t["grade"] == "A"],
        "",
        "## Popular advice the evidence doesn't back",
        "",
        *[f"- **{t['tip']}**: {t['finding']}" + (f" *{t['caveat']}*" if t.get("caveat") else "")
          for t in tips if t["grade"] == "X"],
        "",
        "## All tips",
        "",
        "Rank is the experts' priority in the source study (1 = most important).",
        "",
    ]
    order = "ABXC"
    for area in AREAS:
        rows = sorted((t for t in tips if t["area"] == area), key=lambda t: (order.index(t["grade"]), t["rank"]))
        out += [f"### {area}", "", "| Grade | Tip | What the evidence says | Source | Rank |",
                "|---|---|---|---|---|", *map(row, rows), ""]
    out += [
        "## How this was made",
        "",
        "The tips are the top 40 from an expert ranking of 374 pieces of security advice found on the web "
        "([Redmiles et al., USENIX Security 2020](https://securityadvice.cs.umd.edu/expert-ranking.html)), "
        "with two near-duplicates merged. That study found experts rated 89% of all the advice as effective, "
        "which leaves people with no way to prioritise. This list adds the missing piece: for each tip, the "
        "best evidence we could find that following it reduces harm, graded by the rubric above.",
        "",
        "- Findings are paraphrased; follow each link for the exact wording.",
        "- A grade describes the evidence, not how sensible a tip sounds. Many C tips may well be good "
        "advice; nobody has measured them.",
        "- This is for individuals, not organisations, and it is not legal or professional advice.",
        "",
        "## License",
        "",
        "Text and data: [CC BY 4.0](LICENSE). The README is generated from [`data/tips.yaml`](data/tips.yaml).",
        "",
    ]
    return "\n".join(out)


if __name__ == "__main__":
    (ROOT / "README.md").write_text(render(load()))
