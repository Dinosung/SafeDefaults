"""Generate README.md and README.zh-CN.md from data/tips.yaml. Run: python3 scripts/build_readme.py"""
import pathlib
import re

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
REPO = "https://github.com/Dinosung/SafeDefaults"
GRADE_FORM = f"{REPO}/issues/new?template=grade.yml"
REDMILES = "https://www.usenix.org/system/files/sec20-redmiles.pdf"
RANKING = "https://securityadvice.cs.umd.edu/expert-ranking.html"
GRADES = {
    "A": ("🟢 A", "Measured: following it went with fewer infections, hijacks or compromises"),
    "B": ("🟡 B", "Indirect: attack simulations, update uptake, or how common the threat is"),
    "C": ("⚪ C", "Not shown: no direct evidence found, or the evidence is mixed; often still sensible"),
    "X": ("🔴 X", "Evidence against: little or no measured value, or it backfires"),
}
GRADES_ZH = {"A": "实测：照做的人被感染、被盗号或被入侵的更少",
             "B": "间接：攻击模拟、更新普及率，或威胁有多常见",
             "C": "未证实：没有找到直接证据，或证据互相矛盾；通常仍是合理的建议",
             "X": "证据不支持：几乎没有实测效果，甚至适得其反"}
AREAS = ["Accounts", "Updates & software", "Devices", "Network & messaging", "Scams & privacy"]
WORDS = [
    ("2-factor authentication (2FA, MFA, 2-step verification)",
     "a second check after your password, such as a code on your phone"),
    ("Authenticator app", "a free app, such as Google or Microsoft Authenticator, that shows a 6-digit sign-in code"),
    ("Passkey, security key",
     "a sign-in your phone, computer or a small USB key confirms for you; it can't be phished"),
    ("Password manager", "an app, often built into your phone or browser, that creates and remembers passwords"),
    ("Phishing", "fake emails, texts, calls or websites that try to get your password, a code or money"),
    ("Malware", "harmful software, such as viruses or ransomware"),
    ("Update, patch", "a fix from the maker of your software"),
]
WORDS_ZH = [
    ("两步验证（2FA）", "输入密码后的第二道验证，例如手机上的验证码"),
    ("验证器应用", "显示 6 位登录验证码的免费应用，如 Google 或 Microsoft Authenticator"),
    ("通行密钥（passkey）、安全密钥", "由手机、电脑或小型 USB 密钥替你确认的登录方式，无法被钓鱼"),
    ("密码管理器", "生成并记住密码的应用，手机和浏览器通常自带"),
    ("钓鱼", "骗取密码、验证码或钱财的假邮件、短信、电话或网站"),
    ("恶意软件", "病毒、勒索软件等有害程序"),
]
TEAMS = [
    "Require 2-factor authentication on every staff account (Microsoft 365: turn on Security defaults; "
    "Google Workspace: Admin console > Security > 2-Step Verification > enforce).",
    "Give staff a business password manager instead of sharing passwords.",
    "Give staff standard accounts; keep administrator accounts for the one or two people who manage devices.",
    "Turn on automatic updates on every device, and replace devices that no longer get them.",
    "Keep one backup copy that is not permanently connected, so ransomware can't reach it.",
    "Make reporting a suspicious email easy; training alone measurably does little.",
]


def load() -> list[dict]:
    return yaml.safe_load((ROOT / "data" / "tips.yaml").read_text())


def label(src: dict) -> str:
    """A short source label: "Thomas et al. 2017"."""
    short = re.split(r"[,:]", src["title"])[0].split(" (")[0]
    return f"{short} {src['year']}"


def link(src: dict) -> str:
    title = src["title"].replace('"', "'")
    return f'[{label(src)}]({src["url"]} "{title}")'


def sources(t: dict, sep: str = "; ") -> str:
    found = sep.join(link(t[k]) for k in ("source", "also") if k in t)
    return found + (f" · {t['kind']}" if t.get("kind") else "")


def italic(text: str | None) -> str:
    return f" *{text}*" if text else ""


def evidence(t: dict) -> str:
    return t["finding"] + italic(t.get("caveat")) + (f" ({sources(t)})" if "source" in t else "")


def details(text: str, summary: str, indent: str) -> list[str]:
    return [f"{indent}<details><summary>{summary}</summary>", "", f"{indent}{text}", "", f"{indent}</details>", ""]


def row(t: dict) -> str:
    tip = f"**{t['tip']}**" + (f"<br>*Ranked as: {t['original']}*" if t.get("original") else "")
    return f"| {GRADES[t['grade']][0]} | {tip} | {evidence(t)} |"


def actions(tips: list[dict]) -> tuple[list[dict], list[dict]]:
    proven = [t for t in tips if t["grade"] == "A"]
    nxt = sorted((t for t in tips if t["grade"] == "B" and t.get("do")), key=lambda t: t["rank"])
    return proven, nxt


def render(tips: list[dict]) -> str:
    count = {g: sum(t["grade"] == g for t in tips) for g in GRADES}
    proven, nxt = actions(tips)
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
        f"Only **{count['A']}** have measured outcomes behind them, mostly from companies' own data. "
        f"**{count['C']}** have no direct evidence or mixed evidence: often still sensible, just not shown. "
        f"**{count['X']}** popular " + ("one has evidence against it." if count["X"] == 1
                                         else "ones have evidence against them."),
        "",
        f"Every A, B and X grade links to its source and says what kind of study it is. "
        f"Disagree with a grade? [Tell us, with evidence]({GRADE_FORM}). Running a small team? "
        "See [For small teams](#for-small-teams).",
        "",
        "## Grades",
        "",
        "| Grade | Meaning |",
        "|---|---|",
        *[f"| {mark} | {meaning} |" for mark, meaning in GRADES.values()],
        "",
        "<details><summary>Words used here</summary>",
        "",
        *[f"- **{word}**: {meaning}." for word, meaning in WORDS],
        "",
        "</details>",
        "",
        "## Start here: the tips with measured evidence",
        "",
    ]
    for t in proven:
        out += [f"1. **{t['tip']}**", "", f"   **Do this:** {t['do']}", ""]
        out += details(evidence(t), "Why: the evidence", "   ")
    out += ["### Next: worth doing, with indirect evidence", ""]
    for t in nxt:
        out += [f"- **{t['tip']}** ({GRADES[t['grade']][0]})", "", f"  **Do this:** {t['do']}", ""]
        out += details(evidence(t), "Why: the evidence", "  ")
    out += [
        f"**That's it.** The {len(proven) + len(nxt)} steps above cover what the evidence supports. "
        "The rest of the page is for the curious.",
        "",
        "## Popular advice the evidence doesn't back",
        "",
    ]
    for t in (t for t in tips if t["grade"] == "X"):
        out += [f"- **{t['tip']}.** {evidence(t)}", "", f"  **Instead:** {t['instead']}", ""]
    out += [
        "## For small teams",
        "",
        "The tips are written for individuals, and they apply to your staff too. For a team, the evidence above "
        "translates into a few rules:",
        "",
        *[f"1. {rule}" for rule in TEAMS],
        "",
        "For company-wide controls, see the UK NCSC's [Small Business Guide]"
        "(https://www.ncsc.gov.uk/collection/small-business-guide) or CISA's "
        "[Cyber Essentials](https://www.cisa.gov/cyber-essentials).",
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
        f"The tips are the top 40 from an expert ranking of 374 pieces of security and privacy advice found on "
        f"the web ([Redmiles et al., USENIX Security 2020]({REDMILES}); [ranking]({RANKING})), with two "
        "near-duplicates merged. That study found experts rated 89% of all the advice as effective, which leaves "
        "people with no way to prioritise. This list adds the missing piece: for each tip, the best evidence we "
        "could find that following it reduces harm, graded as above.",
        "",
        "- Each tip in the ranking was rated by about 3 of 41 experts, and neighbouring ranks are close, so treat "
        "\"top 40\" as a well-regarded set rather than a precise order.",
        "- The grade says what kind of evidence exists, not how strong it is. Each source is labelled: *vendor "
        "data* (a company measuring its own users or product), *observational study*, *attack simulation*, "
        "*survey* or *threat prevalence*. Vendor data on its own product is the weakest kind of A; the caveats "
        "say so.",
        "- Findings are paraphrased; follow each link for the exact wording.",
        "- Not legal or professional advice.",
        "",
        "## Contributing",
        "",
        f"Think a grade is wrong? [Open a grade issue]({GRADE_FORM}) (a free GitHub account is needed). "
        "Paste a link to the study and the sentence or number that supports your grade; we do the editing. "
        "The rubric and how to edit the data yourself are in [CONTRIBUTING.md](CONTRIBUTING.md).",
        "",
        "## License and citation",
        "",
        "Text and data: [CC BY 4.0](LICENSE). You may copy or adapt the list, for example into a staff handbook, "
        "as long as you credit SafeDefaults with a link. The README is generated from "
        "[`data/tips.yaml`](data/tips.yaml). To cite the list, use [`CITATION.cff`](CITATION.cff).",
        "",
    ]
    return "\n".join(out)


def render_zh(tips: list[dict]) -> str:
    """A Chinese page: grades, what to do, and the evidence behind it."""
    count = {g: sum(t["grade"] == g for t in tips) for g in GRADES}
    proven, nxt = actions(tips)
    out = [
        "# SafeDefaults",
        "",
        "[English](README.md)",
        "",
        f"**专家最看重的 {len(tips)} 条安全建议，按“有没有证据证明有用”打分。**",
        "",
        f"只有 **{count['A']}** 条有实测结果支持，且大多来自公司自己的数据；"
        f"**{count['C']}** 条没有直接证据或证据互相矛盾，但通常仍是合理的建议；"
        f"另有 **{count['X']}** 条流行建议，证据表明它没什么用。",
        "",
        "## 评分",
        "",
        "| 评分 | 含义 |",
        "|---|---|",
        *[f"| {GRADES[g][0]} | {GRADES_ZH[g]} |" for g in GRADES],
        "",
        "<details><summary>术语</summary>",
        "",
        *[f"- **{word}**：{meaning}。" for word, meaning in WORDS_ZH],
        "",
        "</details>",
        "",
        "## 先做这几件事：有实测证据的建议",
        "",
    ]

    def why(t: dict, indent: str) -> list[str]:
        zh = t["zh"]
        text = zh["finding"] + (f" *{zh['caveat']}*" if zh.get("caveat") else "") + f"（来源：{sources(t, '；')}）"
        return details(text, "依据", indent)

    for t in proven:
        out += [f"1. **{t['zh']['tip']}**", "", f"   **怎么做：** {t['zh']['do']}", ""] + why(t, "   ")
    out += ["### 接下来：值得做，有间接证据", ""]
    for t in nxt:
        out += [f"- **{t['zh']['tip']}**（{GRADES[t['grade']][0]}）", "", f"  **怎么做：** {t['zh']['do']}", ""]
        out += why(t, "  ")
    out += [f"**就这些。** 以上 {len(proven) + len(nxt)} 步涵盖了证据支持的做法。", "",
            "## 证据并不支持的热门建议", ""]
    for t in (t for t in tips if t["grade"] == "X"):
        zh = t["zh"]
        out += [f"- **{zh['tip']}**：{zh['finding']}（来源：{sources(t, '；')}）", "",
                f"  **建议改为：** {zh['instead']}", ""]
    out += [
        "## 方法",
        "",
        f"这些建议来自一项专家排名研究（[Redmiles 等，USENIX Security 2020]({REDMILES})）中排名前 40 的条目，"
        f"其中两条几乎相同的建议已合并，共 {len(tips)} 条。该研究发现专家认为 89% 的网上安全建议都“有效”，"
        "普通人因此无从取舍。我们为每条建议找出最好的证据，并按上面的标准打分。"
        "排名中每条建议只由约 41 位专家中的 3 位评分，"
        "相邻名次差距很小，因此“前 40”应理解为一组公认的好建议，而非精确排序。",
        "",
        "评分说明的是有哪类证据，而不是证据有多强；公司测量自家产品的数据是最弱的一类 A。"
        "部分谷歌来源在中国大陆可能无法直接访问。"
        f"全部 {len(tips)} 条建议及其来源见[英文版完整表格](README.md#all-tips)。本项目不构成专业建议。",
        "",
        "## 参与",
        "",
        f"觉得某个评分不对？可以用中文[提交评分质疑]({GRADE_FORM})，附上研究链接和支持你观点的原文即可。",
        "",
        "## 许可",
        "",
        "文字和数据采用 [CC BY 4.0](LICENSE) 许可：注明出处并附链接，即可复制或改编（例如用于员工手册）。",
        "",
    ]
    return "\n".join(out)


if __name__ == "__main__":
    tips = load()
    (ROOT / "README.md").write_text(render(tips))
    (ROOT / "README.zh-CN.md").write_text(render_zh(tips))
