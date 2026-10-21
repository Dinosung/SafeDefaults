# Contributing

The point of this list is that every grade can be checked, so grades move on evidence.

## Not a programmer? Just open an issue

[Open a grade issue](https://github.com/Dinosung/SafeDefaults/issues/new?template=grade.yml) (a free GitHub
account is needed) with:

1. **The tip**, as it appears in the list.
2. **The best evidence you know**: a link to a study, official dataset or large vendor dataset, and, if
   you can, the sentence or number that supports your grade.
3. **The grade it supports**, using the rubric below.

We do the editing. Experience and opinions are welcome too, and help us look for evidence, but on their
own they can't move a grade above C. Issues in Chinese are fine.

## The rubric

- **A**: a measured outcome (fewer infections, hijacks or compromises) tied to the behaviour itself.
- **B**: indirect evidence: attack simulations, how fast fixes arrive, or how common the threat is.
- **C**: no direct evidence found, or the evidence is mixed.
- **X**: evidence of little or no measured value, or of harm.

## Editing the data yourself

Everything comes from [`data/tips.yaml`](data/tips.yaml). Edit it, then regenerate both READMEs and
run the checks:

```sh
python3 scripts/build_readme.py
pip install pyyaml pytest && pytest -q
```

A, B and X tips need a source with a link and year, and a `kind` saying what sort of evidence it is
(vendor data, observational study, randomised trial, attack simulation, survey, threat prevalence).
Apply the rubric the same way to every tip: mixed or null evidence is C. A tips need a `do` line (what to do, in plain
words) and X tips an `instead` line; give a Chinese version of both under `zh`.
