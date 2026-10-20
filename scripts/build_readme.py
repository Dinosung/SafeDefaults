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
        "[![CI](https://github.com/Dinosung/safedefaults/actions/workflows/ci.yml/badge.svg)]"
        "(https://github.com/Dinosung/safedefaults/actions/workflows/ci.yml) "
        "[![License: CC BY 4.0](https://img.shields.io/badge/license-CC%20BY%204.0-blue.svg)](LICENSE) "
        f"![{len(tips)} tips](https://img.shields.io/badge/tips-{len(tips)}-informational.svg)",
        "",
        "[中文](README.zh-CN.md)",
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
        "## Contributing",
        "",
        "Grades move on evidence. To challenge one, [open a grade issue]"
        "(https://github.com/Dinosung/safedefaults/issues/new?template=grade.yml) with the source and the exact "
        "sentence or number; see [CONTRIBUTING.md](CONTRIBUTING.md) for the rubric.",
        "",
        "## License and citation",
        "",
        "Text and data: [CC BY 4.0](LICENSE). The README is generated from [`data/tips.yaml`](data/tips.yaml). "
        "To cite the list, use [`CITATION.cff`](CITATION.cff) (GitHub's \"Cite this repository\" button).",
        "",
    ]
    return "\n".join(out)


def render_zh(tips: list[dict]) -> str:
    """A short Chinese summary: counts, the A list and the X list, linking to the full English table."""
    count = {g: sum(t["grade"] == g for t in tips) for g in GRADES}
    out = [
        "# SafeDefaults",
        "",
        "[English](README.md)",
        "",
        f"**专家最看重的 {len(tips)} 条安全建议，按\u201c有没有证据证明有用\u201d打分。**",
        "",
        f"只有 **{count['A']}** 条有实测证据证明能减少损失；**{count['C']}** 条完全没有直接证据；"
        f"**{count['X']}** 条（其中几条出现在热门清单上）的证据反而不支持。",
        "",
        "每个评分都附有来源链接。完整表格见[英文版](README.md#all-tips)。",
        "",
        "## 先做这几件事：有实测证据的建议",
        "",
        *[f"1. **{t['zh']['tip']}**：{t['zh']['finding']}" for t in tips if t["grade"] == "A"],
        "",
        "## 证据并不支持的热门建议",
        "",
        *[f"- **{t['zh']['tip']}**：{t['zh']['finding']}" for t in tips if t["grade"] == "X"],
        "",
        "## 方法",
        "",
        "这些建议来自一项专家排名研究（Redmiles 等，USENIX Security 2020）中排名前 40 的条目。"
        "该研究发现专家认为 89% 的网上安全建议都\u201c有效\u201d，普通人因此无从取舍。"
        "我们为每条建议找出最好的证据并按标准打分：A 为实测结果，B 为间接证据，C 为无直接证据，X 为证据不支持。",
        "",
        "本项目面向个人，不构成专业建议。欢迎[提交更好的证据](CONTRIBUTING.md)。",
        "",
    ]
    return "\n".join(out)


if __name__ == "__main__":
    tips = load()
    (ROOT / "README.md").write_text(render(tips))
    (ROOT / "README.zh-CN.md").write_text(render_zh(tips))
