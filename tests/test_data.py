import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / "scripts"))
import build_readme  # noqa: E402

TIPS = build_readme.load()


def test_fields_and_grades():
    for t in TIPS:
        assert t["grade"] in build_readme.GRADES, t["tip"]
        assert t["area"] in build_readme.AREAS, t["tip"]
        assert t["tip"] and t["finding"], t


def test_graded_tips_cite_a_source():
    for t in TIPS:
        if t["grade"] in "ABX":
            src = t.get("source") or {}
            assert src.get("url", "").startswith("https://"), t["tip"]
            assert src.get("title") and src.get("year"), t["tip"]


def test_ranks_are_unique():
    ranks = [t["rank"] for t in TIPS]
    assert len(ranks) == len(set(ranks))


def test_readme_is_up_to_date():
    readme = (build_readme.ROOT / "README.md").read_text()
    assert readme == build_readme.render(TIPS), "run: python3 scripts/build_readme.py"
    zh = (build_readme.ROOT / "README.zh-CN.md").read_text()
    assert zh == build_readme.render_zh(TIPS), "run: python3 scripts/build_readme.py"


def test_a_and_x_tips_have_chinese_text():
    for t in TIPS:
        if t["grade"] in "AX":
            assert t.get("zh", {}).get("tip") and t["zh"].get("finding"), t["tip"]
