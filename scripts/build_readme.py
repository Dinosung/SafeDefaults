"""Generate README.md from data/tips.yaml. Run: python3 scripts/build_readme.py"""
import pathlib
import re

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
REPO = "https://github.com/Dinosung/SafeDefaults"
GRADE_FORM = f"{REPO}/issues/new?template=grade.yml"
GRADES = {
    "A": ("🟢 A", "Measured: following it means fewer infections, hijacks or compromises"),
    "B": ("🟡 B", "Indirect: attack simulations, update uptake, or how common the threat is"),
    "C": ("⚪ C", "Not yet measured: no direct evidence found that it helps, though it is often sensible"),
    "X": ("🔴 X", "Evidence against: little or no measured value, or it backfires"),
}
GRADES_ZH = {"A": "实测：照做的人被感染、被盗号或被入侵的更少",
             "B": "间接：攻击模拟、更新普及率，或威胁有多常见",
             "C": "尚未测量：没有找到直接证据，但通常是合理的建议",
             "X": "证据不支持：几乎没有实测效果，甚至适得其反"}
AREAS = ["Accounts", "Updates & software", "Devices", "Network & messaging", "Scams & privacy"]
WORDS = [
    ("2-factor authentication (2FA, MFA, 2-step verification)",
     "a second check after your password, such as a code on your phone"),
    ("Phishing", "fake emails, texts or websites that try to get your password or money"),
    ("Malware", "harmful software, such as viruses or ransomware"),
    ("Update, patch", "a fix from the maker of your software"),
    ("Password manager", "an app, often built into your phone or browser, that creates and remembers passwords"),
    ("SSO (single sign-on)", "\"Sign in with Google\" or \"Sign in with Apple\" buttons"),
    ("Attack simulation", "researchers attacking test accounts to measure what stops them"),
]


def load() -> list[dict]:
    return yaml.safe_load((ROOT / "data" / "tips.yaml").read_text())


def label(src: dict) -> str:
    """A short source label for narrow tables: "Thomas et al. 2017"."""
    short = re.split(r"[,:]", src["title"])[0].split(" (")[0]
    return f"{short} {src['year']}"


def link(src: dict) -> str:
    title = src["title"].replace('"', "'")
    return f'[{label(src)}]({src["url"]} "{title}")'


def sources(t: dict) -> str:
    return "; ".join(link(t[k]) for k in ("source", "also") if k in t)


def italic(text: str | None) -> str:
    return f" *{text}*" if text else ""


def row(t: dict) -> str:
    evidence = t["finding"] + italic(t.get("caveat")) + (f" ({sources(t)})" if "source" in t else "")
    return f"| {GRADES[t['grade']][0]} | **{t['tip']}** | {evidence} |"


def render(tips: list[dict]) -> str:
    count = {g: sum(t["grade"] == g for t in tips) for g in GRADES}
    out = [
        "# SafeDefaults",
        "",
        f"[![CI]({REPO}/actions/workflows/ci.yml/badge.svg)]({REPO}/actions/workflows/ci.yml) "
        "[![License: CC BY 4.0](https://img.shields.io/badge/license-CC%20BY%204.0-blue.svg)](LICENSE) "
        f"![{len(tips)} tips](https://img.shields.io/badge/tips-{len(tips)}-informational.svg)",
        "",
        "[中文](README.zh-CN.md)",
        "",
        f"**The {len(tips)} security tips experts rank highest, graded by the evidence that they work.**",
        "",
        f"Only **{count['A']}** have measured evidence that they prevent harm. **{count['C']}** have no direct "
        f"evidence yet, and **{count['X']}** popular ones have evidence against them.",
        "",
        "A C grade means no study has shown the tip works, not that it is bad advice: locking your screen "
        "is still worth doing, and backing up (B) certainly is.",
        "",
        f"Every A, B and X grade links to its source. Disagree with one? [Tell us, with evidence]({GRADE_FORM}).",
        "",
        "## Start here: the tips with measured evidence",
        "",
    ]
    for t in (t for t in tips if t["grade"] == "A"):
        out += [f"1. **{t['tip']}.** {t['finding']}{italic(t.get('caveat'))} ({sources(t)})", "",
                f"   **Do this:** {t['do']}", ""]
    out += ["### Next: strong indirect evidence", ""]
    for t in sorted((t for t in tips if t["grade"] == "B" and t.get("do")), key=lambda t: t["rank"]):
        out += [f"- **{t['tip']}.** {t['finding']} ({sources(t)})", "", f"  **Do this:** {t['do']}", ""]
    out += ["## Popular advice the evidence doesn't back", ""]
    for t in (t for t in tips if t["grade"] == "X"):
        out += [f"- **{t['tip']}.** {t['finding']}{italic(t.get('caveat'))} ({sources(t)})",
                "", f"  **Instead:** {t['instead']}", ""]
    out += [
        "## Grades",
        "",
        "| Grade | Meaning |",
        "|---|---|",
        *[f"| {mark} | {meaning} |" for mark, meaning in GRADES.values()],
        "",
        "## Words used here",
        "",
        *[f"- **{word}**: {meaning}." for word, meaning in WORDS],
        "",
        "## All tips",
        "",
        "Within each area, measured tips come first and unmeasured ones last.",
        "",
    ]
    order = "ABXC"
    for area in AREAS:
        rows = sorted((t for t in tips if t["area"] == area), key=lambda t: (order.index(t["grade"]), t["rank"]))
        out += [f"### {area}", "", "| Grade | Tip | What the evidence says |", "|---|---|---|", *map(row, rows), ""]
    out += [
        "## How this was made",
        "",
        "The tips are the top 40 from an expert ranking of 374 pieces of security and privacy advice found on "
        "the web ([Redmiles et al., USENIX Security 2020](https://securityadvice.cs.umd.edu/expert-ranking.html)), "
        "with two near-duplicates merged. That study found experts rated 89% of all the advice as effective, "
        "which leaves people with no way to prioritise. This list adds the missing piece: for each tip, the "
        "best evidence we could find that following it reduces harm, graded as above.",
        "",
        "- Each tip in the ranking was rated by about 3 of 41 experts, and neighbouring ranks are close, so treat "
        "\"top 40\" as a well-regarded set rather than a precise order.",
        "- Evidence types differ: an A can be an observational vendor comparison, which other differences between "
        "users may explain. The caveats say so where it applies.",
        "",
        "- Findings are paraphrased; follow each link for the exact wording.",
        "- A grade describes the evidence, not how sensible a tip sounds.",
        "- The experts' priority rank for each tip is in [`data/tips.yaml`](data/tips.yaml).",
        "- This is for individuals, not organisations, and it is not legal or professional advice.",
        "",
        "## Contributing",
        "",
        f"Think a grade is wrong? [Open a grade issue]({GRADE_FORM}) (a free GitHub account is needed). "
        "Paste a link to the study and the sentence or number that supports your grade; we do the editing. "
        "The rubric and how to edit the data yourself are in [CONTRIBUTING.md](CONTRIBUTING.md).",
        "",
        "## License and citation",
        "",
        "Text and data: [CC BY 4.0](LICENSE). The README is generated from [`data/tips.yaml`](data/tips.yaml). "
        "To cite the list, use [`CITATION.cff`](CITATION.cff) (GitHub's \"Cite this repository\" button).",
        "",
    ]
    return "\n".join(out)


def render_zh(tips: list[dict]) -> str:
    """A Chinese summary: grades, the A and X tips with what to do, and their sources."""
    count = {g: sum(t["grade"] == g for t in tips) for g in GRADES}
    out = [
        "# SafeDefaults",
        "",
        "[English](README.md)",
        "",
        f"**专家最看重的 {len(tips)} 条安全建议，按\u201c有没有证据证明有用\u201d打分。**",
        "",
        f"只有 **{count['A']}** 条有实测证据证明能减少损失；**{count['C']}** 条还没有找到直接证据；"
        f"还有 **{count['X']}** 条流行建议的证据反而不支持。",
        "",
        "C 只说明还没有研究证明它有效，不代表建议不好：离开时锁屏依然值得做，备份数据（B）更是如此。",
        "",
        "## 评分",
        "",
        "| 评分 | 含义 |",
        "|---|---|",
        *[f"| {GRADES[g][0]} | {GRADES_ZH[g]} |" for g in GRADES],
        "",
        "## 先做这几件事：有实测证据的建议",
        "",
    ]
    for t in (t for t in tips if t["grade"] == "A"):
        zh = t["zh"]
        out += [f"1. **{zh['tip']}**：{zh['finding']}（来源：{sources(t)}）", "", f"   **怎么做：** {zh['do']}"]
        out += ["", f"   *{zh['caveat']}*"] if zh.get("caveat") else []
        out += [""]
    out += ["### 接下来：有较强间接证据的建议", ""]
    for t in sorted((t for t in tips if t["grade"] == "B" and t.get("do")), key=lambda t: t["rank"]):
        zh = t["zh"]
        out += [f"- **{zh['tip']}**：{zh['finding']}（来源：{sources(t)}）", "", f"  **怎么做：** {zh['do']}", ""]
    out += ["## 证据并不支持的热门建议", ""]
    for t in (t for t in tips if t["grade"] == "X"):
        zh = t["zh"]
        out += [f"- **{zh['tip']}**：{zh['finding']}（来源：{sources(t)}）", "", f"  **建议改为：** {zh['instead']}"]
        out += ["", f"  *{zh['caveat']}*"] if zh.get("caveat") else []
        out += [""]
    out += [
        "## 方法",
        "",
        "这些建议来自一项专家排名研究"
        "（[Redmiles 等，USENIX Security 2020](https://securityadvice.cs.umd.edu/expert-ranking.html)）"
        f"中排名前 40 的条目，其中两条几乎相同的建议已合并，共 {len(tips)} 条。"
        "该研究发现专家认为 89% 的网上安全建议都\u201c有效\u201d，普通人因此无从取舍。"
        "我们为每条建议找出最好的证据，并按上面的标准打分。"
        "排名中每条建议只由约 41 位专家中的 3 位评分，相邻名次差距很小，"
        "因此\u201c前 40\u201d应理解为一组公认的好建议，而非精确排序。",
        "",
        f"全部 {len(tips)} 条建议及其来源见[英文版完整表格](README.md#all-tips)。"
        "本项目面向个人，不构成专业建议。",
        "",
        "## 参与",
        "",
        f"觉得某个评分不对？可以用中文[提交评分质疑]({GRADE_FORM})，附上研究链接和支持你观点的原文即可。",
        "",
        "## 许可",
        "",
        "文字和数据采用 [CC BY 4.0](LICENSE) 许可。",
        "",
    ]
    return "\n".join(out)


if __name__ == "__main__":
    tips = load()
    (ROOT / "README.md").write_text(render(tips))
    (ROOT / "README.zh-CN.md").write_text(render_zh(tips))
