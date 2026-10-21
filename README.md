# SafeDefaults

[![CI](https://github.com/Dinosung/SafeDefaults/actions/workflows/ci.yml/badge.svg)](https://github.com/Dinosung/SafeDefaults/actions/workflows/ci.yml) [![License: CC BY 4.0](https://img.shields.io/badge/license-CC%20BY%204.0-blue.svg)](LICENSE) ![39 tips](https://img.shields.io/badge/tips-39-informational.svg)

[中文](README.zh-CN.md)

**The 39 security tips experts rank highest, graded by the evidence that they work.**

Only **5** have measured outcomes behind them, mostly from companies' own data. **20** have no direct evidence or mixed evidence: often still sensible, just not shown. **1** popular one has evidence against it.

Every A, B and X grade links to its source and says what kind of study it is. Disagree with a grade? [Tell us, with evidence](https://github.com/Dinosung/SafeDefaults/issues/new?template=grade.yml). Running a small team? See [For small teams](#for-small-teams).

## Grades

| Grade | Meaning |
|---|---|
| 🟢 A | Measured: following it went with fewer infections, hijacks or compromises |
| 🟡 B | Indirect: attack simulations, update uptake, or how common the threat is |
| ⚪ C | Not shown: no direct evidence found, or the evidence is mixed; often still sensible |
| 🔴 X | Evidence against: little or no measured value, or it backfires |

<details><summary>Words used here</summary>

- **2-factor authentication (2FA, MFA, 2-step verification)**: a second check after your password, such as a code on your phone.
- **Authenticator app**: a free app, such as Google or Microsoft Authenticator, that shows a 6-digit sign-in code.
- **Passkey, security key**: a sign-in your phone, computer or a small USB key confirms for you; it can't be phished.
- **Password manager**: an app, often built into your phone or browser, that creates and remembers passwords.
- **Phishing**: fake emails, texts, calls or websites that try to get your password, a code or money.
- **Malware**: harmful software, such as viruses or ransomware.
- **Update, patch**: a fix from the maker of your software.

</details>

## Start here: the tips with measured evidence

1. **Use 2-factor authentication**

   **Do this:** Turn it on for your email first, then banking and social accounts. Apple: Settings > your name > Sign-In & Security (it is often already on). Google: myaccount.google.com/security. Microsoft and Outlook: account.microsoft.com > Security. Elsewhere, look for "2-step verification" or "passkeys" in the account's security settings. Best: a passkey or security key; next: an authenticator app; a text-message code is still far better than none. Never read a code out to anyone who contacts you.

   <details><summary>Why: the evidence</summary>

   Among Microsoft business accounts flagged for suspicious sign-ins, multifactor authentication cut the risk of compromise by 99.22%, and authenticator apps outperformed text-message codes. Google found that challenging suspicious sign-ins with an SMS code to a recovery phone blocked 100% of automated bots, 96% of bulk phishing and 76% of targeted attacks. *Microsoft's data are a preprint on business accounts; Google's are its automatic sign-in challenges, not 2-step verification you turn on. Codes sent by text or shown in an app can still be phished in real time, and text codes can be stolen by SIM swaps; only passkeys and security keys resist phishing (CISA 2024).* ([Meyer et al. 2023](https://arxiv.org/abs/2305.00945 "Meyer et al., How effective is multifactor authentication at deterring cyberattacks? (Microsoft)"); [Google Security Blog 2019](https://security.googleblog.com/2019/05/new-research-how-effective-is-basic.html "Google Security Blog: How effective is basic account hygiene") · vendor data)

   </details>

1. **Don't tell anyone your passwords, even IT**

   **Do this:** No real bank, IT department, Microsoft or Apple will ask for your password or the code they text you. If someone does, by phone, email or chat, stop and contact the organisation on a number you already know.

   <details><summary>Why: the evidence</summary>

   Google found people who had handed their password to a phisher were 400 times more likely to have their account hijacked than a random user. *Google's own data on its own accounts. About disclosure to impostors posing as trusted parties, not to friends or real IT staff.* ([Thomas et al. 2017](https://faculty.cc.gatech.edu/~frankli/papers/google_account_compromise.pdf "Thomas et al., Data breaches, phishing, or malware? Understanding the risks of stolen credentials (ACM CCS)") · vendor data)

   </details>

1. **Use anti-malware software**

   **Do this:** On Windows, Microsoft Defender is built in: open Start, type "Windows Security", and check Virus & threat protection is on. If a trial of McAfee, Norton or similar came with the laptop and asks you to pay, you don't have to: uninstall it (Settings > Apps) and Defender switches back on. Macs, iPhones, iPads and Android phones have protection built in; you don't need to buy an extra app.

   <details><summary>Why: the evidence</summary>

   Microsoft's telemetry found computers without antivirus 5.5 times more likely to be infected. *Observational vendor data, reported second-hand; protected and unprotected PCs differ in other ways too. In a 4-month study of 50 users, 20% were infected by something their antivirus missed. Built-in protection (such as Microsoft Defender) counts.* ([Microsoft Security Intelligence Report v14 2013](https://isc.sans.edu/diary/15659 "Microsoft Security Intelligence Report v14 (via SANS ISC)"); [Lévesque et al. 2013](https://people.scs.carleton.ca/~soma/pubs/levesque-ccs2013.pdf "Lévesque et al., A Clinical Study of Risk Factors Related to Malware Infections (ACM CCS)") · vendor data)

   </details>

1. **Keep antivirus up to date**

   **Do this:** Nothing to do if you use the built-in protection: it updates with your system.

   <details><summary>Why: the evidence</summary>

   Consumer and small-business PCs with up-to-date real-time protection had a 0.6% infection rate; with expired protection, 2.2%; with none, 2.4%. *Observational vendor data, reported second-hand.* ([Microsoft Security Intelligence Report v17 2014](https://www.tomsguide.com/us/danger-stale-av-software,news-19928.html "Microsoft Security Intelligence Report v17 (via Tom's Guide)") · vendor data)

   </details>

1. **Install only trusted software**

   **Do this:** Install apps only from the official store (App Store, Google Play, Microsoft Store) or the maker's own website. On Android, leave "Install unknown apps" switched off.

   <details><summary>Why: the evidence</summary>

   Android devices that installed apps only from Google Play were nine times less likely to get a potentially harmful app. *Google's own observational data about its own store; devices that sideload apps may differ in other ways.* ([Google 2018](https://android-developers.googleblog.com/2018/03/android-security-2017-year-in-review.html "Google, Android Security 2017 Year in Review") · vendor data)

   </details>

### Next: worth doing, with indirect evidence

- **Use unique passwords for different accounts** (🟡 B)

  **Do this:** Use one password manager that works on all your devices and let it create a different password for each account. With an iPhone or iPad and a Windows PC, use Apple's Passwords app and install iCloud for Windows; with Android and Windows, use Google Password Manager in Chrome. Change one account first and check you can sign in on every device, then do email and banking. No need to change a password that already works and isn't reused.

  <details><summary>Why: the evidence</summary>

  With one password leaked from another site plus a few personal details, targeted guessing broke over 73% of normal users' accounts (32% of security-savvy users') within 100 guesses in a large attack simulation. *An attack simulation, not observed compromises.* ([Wang et al. 2016](https://www.passwordresearch.com/papers/paper763.html "Wang et al., Targeted Online Password Guessing (ACM CCS)") · attack simulation)

  </details>

- **Update your devices** (🟡 B)

  **Do this:** Turn on automatic updates and restart when asked. iPhone and iPad: Settings > General > Software Update > Automatic Updates > turn on Automatically Install. Android: Settings > System > Software update. Windows 11: Settings > Windows Update. Windows 10: Settings > Update & Security > Windows Update; Windows 10 now needs Extended Security Updates, free for home users until 12 October 2027, so accept the free enrolment if it is offered. A device that no longer gets updates should not be used for banking or email.

  <details><summary>Why: the evidence</summary>

  Among enterprises with 1,000+ machines, the slowest patchers (500 days to patch 90% of machines, against under 10 for the fastest) encountered more malware. *The paper calls this a simple investigation and reports no malware figures or statistical test, so it is graded B.* ([Kotzias et al. 2019](https://dev.ndss-symposium.org/wp-content/uploads/2019/02/ndss2019_03B-1-2_Kotzias_paper.pdf "Kotzias et al., Mind Your Own Business (NDSS)") · observational study)

  </details>

- **Back up your data regularly** (🟡 B)

  **Do this:** iPhone and iPad: Settings > your name > iCloud > iCloud Backup > turn on. Android: Settings > System > Backup. If Apple or Google says your storage is full, the paid upgrade inside Settings is genuine; never pay through a pop-up or an email. A second copy of photos and documents on a USB drive you already own is a good extra.

  <details><summary>Why: the evidence</summary>

  In a 2024 survey of organisations in 14 countries, 78% of state and local government ransomware victims (68% across all sectors) restored encrypted data from backups. *A vendor survey of organisations with 100-5,000 employees, self-reported; not individuals.* ([Sophos 2024](https://www.sophos.com/en-us/blog/the-state-of-ransomware-in-state-and-local-government-2024 "Sophos, State of Ransomware in State and Local Government") · survey)

  </details>

- **Watch out for phishing** (🟡 B)

  **Do this:** If a call, text, email or pop-up asks for a password, a code, a payment or remote access to your computer, stop. Hang up or close it, then contact the company on a number you already know, such as the one on your card or bill. Real banks, Microsoft and Apple never ask for the code they text you.

  <details><summary>Why: the evidence</summary>

  Phishing victims were 400 times more likely to have their account hijacked than a random Google user, and phishing/spoofing was the most-reported crime type to the FBI in 2024 (193,407 complaints). *Shows the threat is common and costly, not the effect of watching out. Awareness training alone has been measured and found to do little: in a study of over 19,500 hospital employees, recent annual training was not associated with fewer phishing-test failures, and randomised embedded training made very little difference (Ho et al., IEEE S&P 2025). Calling back on a number you know, and passkeys, limit the damage.* ([Thomas et al. 2017](https://faculty.cc.gatech.edu/~frankli/papers/google_account_compromise.pdf "Thomas et al., Data breaches, phishing, or malware? Understanding the risks of stolen credentials (ACM CCS)"); [FBI IC3 2025](https://www.ic3.gov/AnnualReport/Reports/2024_IC3Report.pdf "FBI IC3, 2024 Internet Crime Report") · vendor data; official statistics)

  </details>

**That's it.** The 9 steps above cover what the evidence supports. The rest of the page is for the curious.

## Popular advice the evidence doesn't back

- **Replace letters with symbols in your passwords.** Cracking tools anticipate common substitutions like "@" for "a", so they add little strength; a guessing model predicted "pAsswOrd" would take 4,000 times more guesses to crack than "p@ssw0rd", which people rated stronger. *Based on a guessing model and one example, not observed attacks.* ([Ur et al. 2016](https://www.cmu.edu/news/stories/archives/2016/july/password-perceptions.html "Ur et al., Do Users' Perceptions of Password Security Match Reality? (CHI), via CMU News") · attack simulation)

  **Instead:** Add length rather than symbols: a few random words, or a password your password manager creates. No need to change a password that works and isn't reused.

## For small teams

The tips are written for individuals, and they apply to your staff too. For a team, the evidence above translates into a few rules:

1. Require 2-factor authentication on every staff account (Microsoft 365: turn on Security defaults; Google Workspace: Admin console > Security > 2-Step Verification > enforce).
1. Give staff a business password manager instead of sharing passwords.
1. Give staff standard accounts; keep administrator accounts for the one or two people who manage devices.
1. Turn on automatic updates on every device, and replace devices that no longer get them.
1. Keep one backup copy that is not permanently connected, so ransomware can't reach it.
1. Make reporting a suspicious email easy; training alone measurably does little.

For company-wide controls, see the UK NCSC's [Small Business Guide](https://www.ncsc.gov.uk/collection/small-business-guide) or CISA's [Cyber Essentials](https://www.cisa.gov/cyber-essentials).

## All tips

Within each area, measured tips come first and unmeasured ones last.

### Accounts

| Grade | Tip | What the evidence says |
|---|---|---|
| 🟢 A | **Don't tell anyone your passwords, even IT** | Google found people who had handed their password to a phisher were 400 times more likely to have their account hijacked than a random user. *Google's own data on its own accounts. About disclosure to impostors posing as trusted parties, not to friends or real IT staff.* ([Thomas et al. 2017](https://faculty.cc.gatech.edu/~frankli/papers/google_account_compromise.pdf "Thomas et al., Data breaches, phishing, or malware? Understanding the risks of stolen credentials (ACM CCS)") · vendor data) |
| 🟢 A | **Use 2-factor authentication** | Among Microsoft business accounts flagged for suspicious sign-ins, multifactor authentication cut the risk of compromise by 99.22%, and authenticator apps outperformed text-message codes. Google found that challenging suspicious sign-ins with an SMS code to a recovery phone blocked 100% of automated bots, 96% of bulk phishing and 76% of targeted attacks. *Microsoft's data are a preprint on business accounts; Google's are its automatic sign-in challenges, not 2-step verification you turn on. Codes sent by text or shown in an app can still be phished in real time, and text codes can be stolen by SIM swaps; only passkeys and security keys resist phishing (CISA 2024).* ([Meyer et al. 2023](https://arxiv.org/abs/2305.00945 "Meyer et al., How effective is multifactor authentication at deterring cyberattacks? (Microsoft)"); [Google Security Blog 2019](https://security.googleblog.com/2019/05/new-research-how-effective-is-basic.html "Google Security Blog: How effective is basic account hygiene") · vendor data) |
| 🟡 B | **Use unique passwords for different accounts** | With one password leaked from another site plus a few personal details, targeted guessing broke over 73% of normal users' accounts (32% of security-savvy users') within 100 guesses in a large attack simulation. *An attack simulation, not observed compromises.* ([Wang et al. 2016](https://www.passwordresearch.com/papers/paper763.html "Wang et al., Targeted Online Password Guessing (ACM CCS)") · attack simulation) |
| 🟡 B | **Use strong passwords** | In guessing experiments, long passwords (16+ characters) held up better against a powerful attacker than short passwords with complex rules, though complex 8-character passwords did better against the first guesses. *A lab study with passwords created for the experiment. Supports length, not complexity rules.* ([Kelley et al. 2012](https://users.ece.cmu.edu/~lbauer/papers/2012/oakland2012-guessing.pdf "Kelley et al., Guess Again (and Again and Again) (IEEE S&P)") · attack simulation) |
| 🟡 B | **Don't base passwords on personal information** | Guessing that uses a person's personal details beat the previous best method by 46% against normal users. ([Wang et al. 2016](https://www.passwordresearch.com/papers/paper763.html "Wang et al., Targeted Online Password Guessing (ACM CCS)") · attack simulation) |
| 🟡 B | **Change passwords and security questions on compromised accounts** | Among users of a breach-alerting browser extension, 1.5% of logins used credentials already exposed in a breach, and 26% of warnings led people to change their password. Google found an attacker could guess 19.7% of English speakers' answers to "favourite food" in one try. *Shows exposed passwords are common and guessable answers are weak, not the effect of changing them.* ([Thomas et al. 2019](https://www.usenix.org/system/files/sec19-thomas.pdf "Thomas et al., Protecting accounts from credential stuffing with password breach alerting (USENIX Security)"); [Google Security Blog 2015](https://security.googleblog.com/2015/05/new-research-some-tough-questions-for.html "Google Security Blog: Some tough questions for security questions") · vendor data) |
| 🔴 X | **Replace letters with symbols in your passwords** | Cracking tools anticipate common substitutions like "@" for "a", so they add little strength; a guessing model predicted "pAsswOrd" would take 4,000 times more guesses to crack than "p@ssw0rd", which people rated stronger. *Based on a guessing model and one example, not observed attacks.* ([Ur et al. 2016](https://www.cmu.edu/news/stories/archives/2016/july/password-perceptions.html "Ur et al., Do Users' Perceptions of Password Security Match Reality? (CHI), via CMU News") · attack simulation) |
| ⚪ C | **Encourage others to use strong passwords** | No data on the effect of encouraging others was found. |
| ⚪ C | **Remember your passwords** | No study compares people who memorise passwords with people who don't. Reuse is widespread (the average user had 6.5 passwords, each shared across 3.9 sites), and frequently typed passwords are much more likely to be reused; but frequent typing also helps people remember strong passwords. *Wash et al. also found third-party password managers did not significantly reduce reuse.* ([Florencio & Herley 2007](https://www.www2007.cpsc.ucalgary.ca/papers/paper620.pdf "Florencio & Herley, A Large-Scale Study of Web Password Habits (WWW)"); [Wash et al. 2016](https://www.usenix.org/system/files/conference/soups2016/soups2016-paper-wash.pdf "Wash et al., Understanding Password Choices (SOUPS)")) |
| ⚪ C | **Keep written-down passwords somewhere safe** | Official guidance now tolerates written-down passwords; no outcome data was found. |
| ⚪ C | **Don't store passwords in a file** | NIST lists copied password files as an example threat, without data on how often it happens. |
| ⚪ C | **Be careful typing passwords on public computers** | No data on the behaviour's effect was found. |
| ⚪ C | **Use a mix of letters, numbers and special characters** | The evidence is mixed. In guessing experiments, complex 8-character passwords resisted early guesses better, but long passwords did better against a powerful attacker; in a study of 154 people's real passwords, those with digits and symbols were more often reused. NIST now says services "shall not" require such mixes. *The reuse finding is a correlation: sites that demand symbols may cause both. Length matters more than mixing; there is no need to change a password that works and isn't reused.* ([Pearman et al. 2017](https://users.ece.cmu.edu/~lbauer/papers/2017/ccs2017-password-reuse.pdf "Pearman et al., Let's go in for a closer look (ACM CCS)"); [NIST SP 800-63B-4 2025](https://pages.nist.gov/800-63-4/sp800-63b.html "NIST SP 800-63B-4, section 3.1.1.2")) |
| ⚪ C | **Use a password manager** | The evidence is mixed. People who created passwords with the manager's generator reused fewer passwords, while browser auto-fill went with more reuse; two real-world studies found no significant effect on reuse. *The benefit comes from passwords the manager generates; a manager full of reused passwords helps little.* ([Lyastani et al. 2018](https://www.usenix.org/conference/usenixsecurity18/presentation/lyastani "Lyastani et al., Better managed than memorized? (USENIX Security)"); [Pearman et al. 2017](https://users.ece.cmu.edu/~lbauer/papers/2017/ccs2017-password-reuse.pdf "Pearman et al., Let's go in for a closer look (ACM CCS)")) |
| ⚪ C | **Use single sign-on (SSO)** | No data on the benefit for individuals was found. One study found 89.5% of 95 sites using single sign-on offered no way to end active sessions, so a hijacked sign-in account can be hard to recover from. ([Ghasemisharif et al. 2018](https://www.usenix.org/conference/usenixsecurity18/presentation/ghasemisharif "Ghasemisharif et al., O Single Sign-Off, Where Art Thou? (USENIX Security)")) |

### Updates & software

| Grade | Tip | What the evidence says |
|---|---|---|
| 🟢 A | **Use anti-malware software** | Microsoft's telemetry found computers without antivirus 5.5 times more likely to be infected. *Observational vendor data, reported second-hand; protected and unprotected PCs differ in other ways too. In a 4-month study of 50 users, 20% were infected by something their antivirus missed. Built-in protection (such as Microsoft Defender) counts.* ([Microsoft Security Intelligence Report v14 2013](https://isc.sans.edu/diary/15659 "Microsoft Security Intelligence Report v14 (via SANS ISC)"); [Lévesque et al. 2013](https://people.scs.carleton.ca/~soma/pubs/levesque-ccs2013.pdf "Lévesque et al., A Clinical Study of Risk Factors Related to Malware Infections (ACM CCS)") · vendor data) |
| 🟢 A | **Keep antivirus up to date** | Consumer and small-business PCs with up-to-date real-time protection had a 0.6% infection rate; with expired protection, 2.2%; with none, 2.4%. *Observational vendor data, reported second-hand.* ([Microsoft Security Intelligence Report v17 2014](https://www.tomsguide.com/us/danger-stale-av-software,news-19928.html "Microsoft Security Intelligence Report v17 (via Tom's Guide)") · vendor data) |
| 🟢 A | **Install only trusted software** | Android devices that installed apps only from Google Play were nine times less likely to get a potentially harmful app. *Google's own observational data about its own store; devices that sideload apps may differ in other ways.* ([Google 2018](https://android-developers.googleblog.com/2018/03/android-security-2017-year-in-review.html "Google, Android Security 2017 Year in Review") · vendor data) |
| 🟡 B | **Update your devices** | Among enterprises with 1,000+ machines, the slowest patchers (500 days to patch 90% of machines, against under 10 for the fastest) encountered more malware. *The paper calls this a simple investigation and reports no malware figures or statistical test, so it is graded B.* ([Kotzias et al. 2019](https://dev.ndss-symposium.org/wp-content/uploads/2019/02/ndss2019_03B-1-2_Kotzias_paper.pdf "Kotzias et al., Mind Your Own Business (NDSS)") · observational study) |
| 🟡 B | **Turn on automatic updates** | 21 days after a 2009 release, 97% of Chrome users (silent updates) ran the latest version, against 85% for Firefox (prompted updates) and 24% for a browser that needed a manual reinstall. *Measures how fast updates arrive, not attacks prevented.* ([Duebendorfer & Frei 2009](https://www.darkreading.com/risk/google-chrome-update-scheme-beats-firefox-safari-opera "Duebendorfer & Frei, Why Silent Updates Boost Security (via Dark Reading)") · observational study) |
| 🟡 B | **Don't use an administrator account day to day** | Removing admin rights would have mitigated 56% of critical Microsoft vulnerabilities from 2020. *A vendor of privilege-management software reading Microsoft's advisories, not observed incidents. The experts' wording was "use administrator rights to prevent unauthorized actions"; we read it as limiting who has them.* ([BeyondTrust Microsoft Vulnerabilities Report 2021](https://www.beyondtrust.com/press/beyondtrust-finds-56-percent-of-critical-microsoft-vulnerabilities-can-be-mitigated-by-removing-admin-rights "BeyondTrust Microsoft Vulnerabilities Report") · vendor analysis) |
| 🟡 B | **Read install prompts** | 54% of 3.9 million hosts examined had potentially unwanted programs, much of it installed by other unwanted programs and pay-per-install bundlers. *Shows the threat is common, not the effect of reading prompts.* ([Kotzias et al. 2016](https://www.usenix.org/conference/usenixsecurity16/technical-sessions/presentation/kotzias "Kotzias et al., Measuring PUP Prevalence (USENIX Security)") · observational study) |
| ⚪ C | **Scan attachments for viruses before opening them** | Mail providers and antivirus already scan automatically; no data on manual scanning was found. |
| ⚪ C | **Set antivirus to run periodic full scans** | No data on the behaviour's effect was found. |

### Devices

| Grade | Tip | What the evidence says |
|---|---|---|
| 🟡 B | **Lock your phone with a passcode or fingerprint** | Weighted to the US population, about 1 in 5 adults had snooped on someone else's phone in the past year. *Shows the threat is common, not the effect of a lock.* ([Marques et al. 2016](https://www.usenix.org/conference/soups2016/technical-sessions/presentation/marques "Marques et al., Snooping on Mobile Phones (SOUPS)") · survey) |
| 🟡 B | **Back up your data regularly** | In a 2024 survey of organisations in 14 countries, 78% of state and local government ransomware victims (68% across all sectors) restored encrypted data from backups. *A vendor survey of organisations with 100-5,000 employees, self-reported; not individuals.* ([Sophos 2024](https://www.sophos.com/en-us/blog/the-state-of-ransomware-in-state-and-local-government-2024 "Sophos, State of Ransomware in State and Local Government") · survey) |
| ⚪ C | **Protect devices against power surges** | A reliability measure rather than a security one; no data was found. |
| ⚪ C | **Lock your computer when you step away** | No data on the behaviour's effect was found. |

### Network & messaging

| Grade | Tip | What the evidence says |
|---|---|---|
| ⚪ C | **Use end-to-end encrypted messaging** | CISA recommends it to highly targeted officials after the 2024 compromise of US telecom networks, but cites no measured data on individuals. ([CISA 2024](https://www.cisa.gov/sites/default/files/2024-12/guidance-mobile-communications-best-practices.pdf "CISA, Mobile Communications Best Practice Guidance")) |
| ⚪ C | **Monitor network traffic on your router** | Impractical for most people; no data was found. |
| ⚪ C | **Test your firewall** | No data on the behaviour's effect was found. |
| ⚪ C | **Use a VPN** | No data showing a benefit for typical users was found. Free-to-download VPN apps carry real risks: of 283 such Android apps studied in 2015, 18% tunnelled traffic without encryption and 4% were flagged as malware by more than five scanners (38% by at least one). *At home you don't need one for safety; on public Wi-Fi, sites using https are already encrypted. Our suggestion, not evidence: if you use one, choose a provider with a good reputation over a free app.* ([Ikram et al. 2016](https://research.csiro.au/isp/wp-content/uploads/sites/106/2016/08/paper-1.pdf "Ikram et al., An Analysis of the Privacy and Security Risks of Android VPN Apps (IMC)")) |
| ⚪ C | **Don't do online banking on a public computer** | No data on the behaviour's effect was found. |

### Scams & privacy

| Grade | Tip | What the evidence says |
|---|---|---|
| 🟡 B | **Beware of sharing personal information with people you don't know** | Americans reported losing $2.95 billion to imposter scams in 2024. *About imposter scams in general, not the effect of sharing less.* ([FTC 2025](https://www.ftc.gov/node/87602 "FTC, Consumer Sentinel Network data for 2024") · threat prevalence) |
| 🟡 B | **Watch out for phishing** | Phishing victims were 400 times more likely to have their account hijacked than a random Google user, and phishing/spoofing was the most-reported crime type to the FBI in 2024 (193,407 complaints). *Shows the threat is common and costly, not the effect of watching out. Awareness training alone has been measured and found to do little: in a study of over 19,500 hospital employees, recent annual training was not associated with fewer phishing-test failures, and randomised embedded training made very little difference (Ho et al., IEEE S&P 2025). Calling back on a number you know, and passkeys, limit the damage.* ([Thomas et al. 2017](https://faculty.cc.gatech.edu/~frankli/papers/google_account_compromise.pdf "Thomas et al., Data breaches, phishing, or malware? Understanding the risks of stolen credentials (ACM CCS)"); [FBI IC3 2025](https://www.ic3.gov/AnnualReport/Reports/2024_IC3Report.pdf "FBI IC3, 2024 Internet Crime Report") · vendor data; official statistics) |
| 🟡 B | **Don't click on ads** | Over 80% of the social-engineering download attacks seen on a large network started from ads on sites people visited, mostly pushing adware and unwanted programs. *Shows the threat is common, not the effect of avoiding clicks.* ([Nelms et al. 2016](https://www.usenix.org/conference/usenixsecurity16/technical-sessions/presentation/nelms "Nelms et al., Towards Measuring and Mitigating Social Engineering Software Download Attacks (USENIX Security)") · observational study) |
| ⚪ C | **Don't identify yourself to websites** | No data on the behaviour's effect was found. |
| ⚪ C | **Don't give out your email address without good reason** | No data on the behaviour's effect was found. |
| ⚪ C | **Set rules for your kids about the internet** | The evidence is mixed. In a survey of 25,142 European children, rules were linked with lower online risk (and fewer opportunities and skills); in a US study of 215 parent-teen pairs, more use of monitoring apps and controls was linked with more risk. *Surveys linking parenting styles with exposure to risk, not measured harm. Talking with children about their internet use was linked with less harm.* ([Duerager & Livingstone 2012](https://eprints.lse.ac.uk/42872/ "Duerager & Livingstone, How can parents support children's internet safety? (EU Kids Online, LSE)"); [Ghosh et al. 2018](https://pure.psu.edu/en/publications/a-matter-of-control-or-safety-examining-parental-use-of-technical/ "Ghosh et al., A Matter of Control or Safety? (CHI)")) |

## How this was made

The tips are the top 40 from an expert ranking of 374 pieces of security and privacy advice found on the web ([Redmiles et al., USENIX Security 2020](https://www.usenix.org/system/files/sec20-redmiles.pdf); [ranking](https://securityadvice.cs.umd.edu/expert-ranking.html)), with two near-duplicates merged. That study found experts rated 89% of all the advice as effective, which leaves people with no way to prioritise. This list adds the missing piece: for each tip, the best evidence we could find that following it reduces harm, graded as above.

- Each tip in the ranking was rated by about 3 of 41 experts, and neighbouring ranks are close, so treat "top 40" as a well-regarded set rather than a precise order.
- The grade says what kind of evidence exists, not how strong it is. Each source is labelled: *vendor data* (a company measuring its own users or product), *observational study*, *attack simulation*, *survey* or *threat prevalence*. Vendor data on its own product is the weakest kind of A; the caveats say so.
- Findings are paraphrased; follow each link for the exact wording.
- Not legal or professional advice.

## Contributing

Think a grade is wrong? [Open a grade issue](https://github.com/Dinosung/SafeDefaults/issues/new?template=grade.yml) (a free GitHub account is needed). Paste a link to the study and the sentence or number that supports your grade; we do the editing. The rubric and how to edit the data yourself are in [CONTRIBUTING.md](CONTRIBUTING.md).

## License and citation

Text and data: [CC BY 4.0](LICENSE). You may copy or adapt the list, for example into a staff handbook, as long as you credit SafeDefaults with a link. The README is generated from [`data/tips.yaml`](data/tips.yaml). To cite the list, use [`CITATION.cff`](CITATION.cff).
