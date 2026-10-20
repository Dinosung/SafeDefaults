# SafeDefaults

[![CI](https://github.com/Dinosung/safedefaults/actions/workflows/ci.yml/badge.svg)](https://github.com/Dinosung/safedefaults/actions/workflows/ci.yml) [![License: CC BY 4.0](https://img.shields.io/badge/license-CC%20BY%204.0-blue.svg)](LICENSE) ![39 tips](https://img.shields.io/badge/tips-39-informational.svg)

[中文](README.zh-CN.md)

**The 39 security tips experts rank highest, graded by the evidence that they work.**

Only **5** have measured proof that they prevent harm. **16** have no direct evidence at all. **4**, several of them on popular checklists, have evidence against them.

Every grade links to its source. Disagree with one? [Open an issue with better evidence](CONTRIBUTING.md).

## Grades

| Grade | Meaning |
|---|---|
| 🟢 A | Measured: following it means fewer infections, hijacks or compromises |
| 🟡 B | Indirect: attack simulations, update uptake, or how common the threat is |
| ⚪ C | No direct evidence found that it helps: often sensible, just unmeasured |
| 🔴 X | Evidence against: little or no measured value, or it backfires |

## Start here: the tips with measured proof

1. **Use 2-factor authentication**: Google found an SMS code to a recovery phone blocked 100% of automated bots, 96% of bulk phishing and 76% of targeted attacks; Microsoft measured MFA cutting compromise risk by over 99%.
1. **Update your devices**: Across 82 million client hosts in 28,000 enterprises, patching applications on time had a significant effect on malware encounters.
1. **Use anti-malware software**: Microsoft's telemetry found computers without antivirus 5.5 times more likely to be infected.
1. **Keep antivirus up to date**: PCs with up-to-date real-time protection had a 0.6% infection rate; with expired protection, 2.2%.
1. **Install only trusted software**: Android devices that installed apps only from Google Play were nine times less likely to get a potentially harmful app.

## Popular advice the evidence doesn't back

- **Remember your passwords**: People who memorise passwords end up reusing them; a large study found the average user had 6.5 passwords shared across 3.9 sites each. Memorising at scale works against unique passwords. *Wash et al. measured 134 people for six weeks and found they mostly reuse the passwords they type often. Reuse on low-value sites can be a reasonable trade-off.*
- **Use a mix of letters, numbers and special characters**: NIST's digital identity guidelines say services "shall not" impose composition rules like these; length and checks against known-breached passwords matter more.
- **Replace letters with symbols in your passwords**: Cracking tools try common substitutions like "@" for "a" first, so they add little strength.
- **Use a VPN**: Of 283 Android VPN apps studied, 38% had at least one malware report on VirusTotal and 18% sent traffic without encryption. We found no data showing a benefit for typical users. *About the VPN app market; a well-chosen paid VPN would be C (no evidence either way).*

## All tips

Rank is the experts' priority in the source study (1 = most important).

### Accounts

| Grade | Tip | What the evidence says | Source | Rank |
|---|---|---|---|---|
| 🟢 A | **Use 2-factor authentication** | Google found an SMS code to a recovery phone blocked 100% of automated bots, 96% of bulk phishing and 76% of targeted attacks; Microsoft measured MFA cutting compromise risk by over 99%. *Prefer an authenticator app or security key over SMS; a study found all five major US carriers could be tricked into SIM swaps (Lee et al., SOUPS 2020).* | [Google Security Blog: How effective is basic account hygiene, 2019](https://security.googleblog.com/2019/05/new-research-how-effective-is-basic.html); [Meyer et al., How effective is multifactor authentication (Microsoft), 2023](https://arxiv.org/abs/2305.00945) | 22 |
| 🟡 B | **Use unique passwords for different accounts** | With one leaked password from another site, targeted guessing broke over 73% of normal users' accounts in a large attack simulation. *An attack simulation, not observed compromises.* | [Wang et al., Targeted Online Password Guessing (ACM CCS), 2016](https://www.passwordresearch.com/papers/paper763.html) | 1 |
| 🟡 B | **Don't tell anyone your passwords, even IT** | Google found people who had handed their password to a phisher were 400 times more likely to have their account hijacked than a random user. *About disclosure to impostors posing as trusted parties, not to friends or real IT staff.* | [Thomas et al., Data breaches, phishing, or malware? Understanding the risks of stolen credentials (ACM CCS), 2017](https://research.google/pubs/data-breaches-phishing-or-malware-understanding-the-risks-of-stolen-credentials/) | 7 |
| 🟡 B | **Use strong passwords** | In guessing experiments, long passwords (16+ characters) resisted a powerful attacker better than short passwords with complex rules. *Supports length, not complexity rules.* | [Kelley et al., Guess Again (and Again and Again) (IEEE S&P), 2012](https://users.ece.cmu.edu/~lbauer/papers/2012/oakland2012-guessing.pdf) | 15 |
| 🟡 B | **Don't base passwords on personal information** | Guessing that uses only a person's public details beat the previous best method by 46% against normal users. | [Wang et al., Targeted Online Password Guessing (ACM CCS), 2016](https://www.passwordresearch.com/papers/paper763.html) | 20 |
| 🟡 B | **Use a password manager** | Password managers changed password strength, but whether for the better depended on whether people used the built-in generator. *The benefit comes from generated passwords; a manager full of reused passwords helps little.* | [Lyastani et al., Better managed than memorized? (USENIX Security), 2018](https://www.usenix.org/conference/usenixsecurity18/presentation/lyastani) | 31 |
| 🟡 B | **Change passwords and security questions on compromised accounts** | About 1.5% of logins on the web use credentials already exposed in breaches, so leaked passwords are actively tried. *Shows the threat is common, not the effect of changing passwords.* | [Thomas et al., Protecting accounts from credential stuffing (USENIX Security), 2019](https://www.usenix.org/conference/usenixsecurity19/presentation/thomas) | 39 |
| 🔴 X | **Remember your passwords** | People who memorise passwords end up reusing them; a large study found the average user had 6.5 passwords shared across 3.9 sites each. Memorising at scale works against unique passwords. *Wash et al. measured 134 people for six weeks and found they mostly reuse the passwords they type often. Reuse on low-value sites can be a reasonable trade-off.* | [Florencio & Herley, A Large-Scale Study of Web Password Habits (WWW), 2007](https://www.www2007.cpsc.ucalgary.ca/papers/paper620.pdf); [Wash et al., Understanding Password Choices (SOUPS), 2016](https://www.usenix.org/system/files/conference/soups2016/soups2016-paper-wash.pdf) | 9 |
| 🔴 X | **Use a mix of letters, numbers and special characters** | NIST's digital identity guidelines say services "shall not" impose composition rules like these; length and checks against known-breached passwords matter more. | [NIST SP 800-63B-4, section 3.1.1.2, 2025](https://pages.nist.gov/800-63-4/sp800-63b.html) | 24 |
| 🔴 X | **Replace letters with symbols in your passwords** | Cracking tools try common substitutions like "@" for "a" first, so they add little strength. | [Ur et al., password perceptions study (CHI), CMU News, 2016](https://www.cmu.edu/news/stories/archives/2016/july/password-perceptions.html) | 32 |
| ⚪ C | **Encourage others to use strong passwords** | No data on the effect of encouraging others was found. |  | 6 |
| ⚪ C | **Keep written-down passwords somewhere safe** | Official guidance now tolerates written-down passwords; no outcome data was found. |  | 10 |
| ⚪ C | **Don't store passwords in a file** | NIST lists copied password files as an example threat, without data on how often it happens. |  | 14 |
| ⚪ C | **Be careful typing passwords on public computers** | No data on the behaviour's effect was found. |  | 17 |
| ⚪ C | **Use single sign-on (SSO)** | No data on the benefit for individuals was found. One study found 89.5% of 95 sites using single sign-on offered no way to end active sessions, so a hijacked sign-in account can be hard to recover from. | [Ghasemisharif et al., O Single Sign-Off, Where Art Thou? (USENIX Security), 2018](https://www.usenix.org/conference/usenixsecurity18/presentation/ghasemisharif) | 33 |

### Updates & software

| Grade | Tip | What the evidence says | Source | Rank |
|---|---|---|---|---|
| 🟢 A | **Update your devices** | Across 82 million client hosts in 28,000 enterprises, patching applications on time had a significant effect on malware encounters. *Enterprise hosts; the authors call the comparison a simple investigation.* | [Kotzias et al., Mind Your Own Business (NDSS), 2019](https://dev.ndss-symposium.org/wp-content/uploads/2019/02/ndss2019_03B-1-2_Kotzias_paper.pdf) | 2 |
| 🟢 A | **Use anti-malware software** | Microsoft's telemetry found computers without antivirus 5.5 times more likely to be infected. *Observational vendor data, reported second-hand. Built-in protection (such as Microsoft Defender) counts.* | [Microsoft Security Intelligence Report v14 (via SANS ISC), 2013](https://isc.sans.edu/diary/15659) | 3 |
| 🟢 A | **Keep antivirus up to date** | PCs with up-to-date real-time protection had a 0.6% infection rate; with expired protection, 2.2%. *Observational vendor data, reported second-hand.* | [Microsoft Security Intelligence Report v17 (via Tom's Guide), 2014](https://www.tomsguide.com/us/danger-stale-av-software,news-19928.html) | 12 |
| 🟢 A | **Install only trusted software** | Android devices that installed apps only from Google Play were nine times less likely to get a potentially harmful app. | [Google, Android Security 2017 Year in Review, 2018](https://android-developers.googleblog.com/2018/03/android-security-2017-year-in-review.html) | 18 |
| 🟡 B | **Turn on automatic updates** | 21 days after a release, 97% of Chrome users (silent updates) ran the latest version, against 24% for a browser that needed a manual reinstall. *Measures how fast updates arrive, not attacks prevented.* | [Duebendorfer & Frei, Why Silent Updates Boost Security (via Dark Reading), 2009](https://www.darkreading.com/risk/google-chrome-update-scheme-beats-firefox-safari-opera) | 16 |
| 🟡 B | **Don't use an administrator account day to day** | Removing admin rights would have mitigated 56% of critical Microsoft vulnerabilities from 2020. *Vendor analysis of vulnerabilities, not incidents.* | [BeyondTrust Microsoft Vulnerabilities Report, 2021](https://www.beyondtrust.com/press/beyondtrust-finds-56-percent-of-critical-microsoft-vulnerabilities-can-be-mitigated-by-removing-admin-rights) | 19 |
| 🟡 B | **Read install prompts** | Over half of the hosts examined had potentially unwanted programs, mostly bundled into other installers. *Shows the threat is common, not the effect of reading prompts.* | [Kotzias et al., Measuring PUP Prevalence (USENIX Security), 2016](https://www.usenix.org/conference/usenixsecurity16/technical-sessions/presentation/kotzias) | 29 |
| ⚪ C | **Scan attachments for viruses before opening them** | Mail providers and antivirus already scan automatically; no data on manual scanning was found. |  | 4 |
| ⚪ C | **Set antivirus to run periodic full scans** | No data on the behaviour's effect was found. |  | 35 |

### Devices

| Grade | Tip | What the evidence says | Source | Rank |
|---|---|---|---|---|
| 🟡 B | **Lock your phone with a passcode or fingerprint** | An estimated 31% of people in an online sample had snooped on someone else's phone in the past year. *Shows the threat is common, not the effect of a lock.* | [Marques et al., Snooping on Mobile Phones (SOUPS), 2016](https://www.usenix.org/conference/soups2016/technical-sessions/presentation/marques) | 21 |
| 🟡 B | **Back up your data regularly** | In a ransomware survey of public-sector victims, 68% recovered data from backups. *Organisations, not individuals.* | [Sophos, State of Ransomware in State and Local Government, 2024](https://www.sophos.com/en-us/blog/the-state-of-ransomware-in-state-and-local-government-2024) | 27 |
| ⚪ C | **Protect devices against power surges** | A reliability measure rather than a security one; no data was found. |  | 26 |
| ⚪ C | **Lock your computer when you step away** | No data on the behaviour's effect was found. |  | 37 |

### Network & messaging

| Grade | Tip | What the evidence says | Source | Rank |
|---|---|---|---|---|
| 🔴 X | **Use a VPN** | Of 283 Android VPN apps studied, 38% had at least one malware report on VirusTotal and 18% sent traffic without encryption. We found no data showing a benefit for typical users. *About the VPN app market; a well-chosen paid VPN would be C (no evidence either way).* | [Ikram et al., An Analysis of the Privacy and Security Risks of Android VPN Apps (IMC), 2016](https://research.csiro.au/isp/wp-content/uploads/sites/106/2016/08/paper-1.pdf) | 30 |
| ⚪ C | **Use end-to-end encrypted messaging** | CISA recommends it after the 2024 compromise of US telecom networks, but cites no measured data on individuals. | [CISA, Mobile Communications Best Practice Guidance, 2024](https://www.cisa.gov/sites/default/files/2024-12/guidance-mobile-communications-best-practices.pdf) | 8 |
| ⚪ C | **Monitor network traffic on your router** | Impractical for most people; no data was found. |  | 13 |
| ⚪ C | **Test your firewall** | No data on the behaviour's effect was found. |  | 25 |
| ⚪ C | **Don't do online banking on a public computer** | No data on the behaviour's effect was found. |  | 38 |

### Scams & privacy

| Grade | Tip | What the evidence says | Source | Rank |
|---|---|---|---|---|
| 🟡 B | **Beware of sharing personal information with people you don't know** | Americans reported losing $2.95 billion to imposter scams in 2024. *Shows the threat is common, not the effect of the behaviour.* | [FTC, Consumer Sentinel Network data for 2024, 2025](https://www.ftc.gov/node/87602) | 34 |
| 🟡 B | **Watch out for phishing** | Phishing victims were 400 times more likely to have their account hijacked than a random Google user, and phishing was the most-reported crime type to the FBI in 2024 (193,407 complaints). *The threat is well measured; the usual defence, awareness training, is not. In a study of over 19,500 hospital employees, recent training made no significant difference to phishing test failures (Ho et al., IEEE S&P 2025). 2-factor authentication blocked 96% of bulk phishing in Google's study.* | [Thomas et al., Data breaches, phishing, or malware? Understanding the risks of stolen credentials (ACM CCS), 2017](https://research.google/pubs/data-breaches-phishing-or-malware-understanding-the-risks-of-stolen-credentials/); [FBI IC3, 2024 Internet Crime Report, 2025](https://www.ic3.gov/AnnualReport/Reports/2024_IC3Report.pdf) | 36 |
| 🟡 B | **Don't click on ads** | Over 80% of the social-engineering download attacks seen on a large network started from ads on sites people visited, mostly pushing adware and unwanted programs. *Shows the threat is common, not the effect of avoiding clicks.* | [Nelms et al., Towards Measuring and Mitigating Social Engineering Software Download Attacks (USENIX Security), 2016](https://www.usenix.org/conference/usenixsecurity16/technical-sessions/presentation/nelms) | 40 |
| ⚪ C | **Don't identify yourself to websites** | No data on the behaviour's effect was found. |  | 11 |
| ⚪ C | **Don't give out your email address without good reason** | No data on the behaviour's effect was found. |  | 23 |
| ⚪ C | **Set rules for your kids about the internet** | The evidence is mixed. In a survey of 25,142 European children, rules were linked with lower online risk (and fewer opportunities); in a US study of 215 parent-teen pairs, more parental control was linked with more risk. *Associations with exposure to risk, not measured harm.* | [Duerager & Livingstone, How can parents support children's internet safety? (EU Kids Online, LSE), 2012](https://eprints.lse.ac.uk/42872/); [Ghosh et al., A Matter of Control or Safety? (CHI), 2018](https://pure.psu.edu/en/publications/a-matter-of-control-or-safety-examining-parental-use-of-technical/) | 28 |

## How this was made

The tips are the top 40 from an expert ranking of 374 pieces of security advice found on the web ([Redmiles et al., USENIX Security 2020](https://securityadvice.cs.umd.edu/expert-ranking.html)), with two near-duplicates merged. That study found experts rated 89% of all the advice as effective, which leaves people with no way to prioritise. This list adds the missing piece: for each tip, the best evidence we could find that following it reduces harm, graded by the rubric above.

- Findings are paraphrased; follow each link for the exact wording.
- A grade describes the evidence, not how sensible a tip sounds. Many C tips may well be good advice; nobody has measured them.
- This is for individuals, not organisations, and it is not legal or professional advice.

## Contributing

Grades move on evidence. To challenge one, [open a grade issue](https://github.com/Dinosung/safedefaults/issues/new?template=grade.yml) with the source and the exact sentence or number; see [CONTRIBUTING.md](CONTRIBUTING.md) for the rubric.

## License and citation

Text and data: [CC BY 4.0](LICENSE). The README is generated from [`data/tips.yaml`](data/tips.yaml). To cite the list, use [`CITATION.cff`](CITATION.cff) (GitHub's "Cite this repository" button).
