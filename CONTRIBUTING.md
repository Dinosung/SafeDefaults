# Contributing

The point of this list is that every grade can be checked. To change a grade or add a tip, open an
issue or pull request with:

1. **The tip**, in plain words.
2. **The best evidence you know**: a link to a study, official dataset or large vendor dataset, the
   year, and the sentence or number that supports your grade.
3. **The grade it supports**, using the rubric:
   - **A**: a measured outcome (fewer infections, hijacks or compromises) tied to the behaviour itself.
   - **B**: indirect evidence: attack simulations, how fast fixes arrive, or how common the threat is.
   - **C**: no direct evidence found.
   - **X**: evidence of little or no measured value, or of harm.

Edit `data/tips.yaml`, then run `python3 scripts/build_readme.py` to regenerate the README.
Opinions and blog posts without data are welcome in discussion, but can't move a grade above C.
