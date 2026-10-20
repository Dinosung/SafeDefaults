# SafeDefaults

[English](README.md)

**专家最看重的 39 条安全建议，按“有没有证据证明有用”打分。**

只有 **4** 条有实测证据证明能减少损失；**18** 条还没有找到直接证据；还有 **2** 条流行建议的证据反而不支持。

C 只说明还没有研究证明它有效，不代表建议不好：离开时锁屏依然值得做，备份数据（B）更是如此。

## 评分

| 评分 | 含义 |
|---|---|
| 🟢 A | 实测：照做的人被感染、被盗号或被入侵的更少 |
| 🟡 B | 间接：攻击模拟、更新普及率，或威胁有多常见 |
| ⚪ C | 尚未测量：没有找到直接证据，但通常是合理的建议 |
| 🔴 X | 证据不支持：几乎没有实测效果，甚至适得其反 |

## 先做这几件事：有实测证据的建议

1. **开启两步验证（2FA，又称双重认证）**：微软测得多重验证可将账户被盗风险降低 99.22%。谷歌发现，在可疑登录时向辅助手机号发送短信验证码，挡住了 100% 的自动化攻击、96% 的批量钓鱼和 76% 的定向攻击。（来源：[Meyer et al. 2023](https://arxiv.org/abs/2305.00945 "Meyer et al., How effective is multifactor authentication at deterring cyberattacks? (Microsoft)"); [Google Security Blog 2019](https://security.googleblog.com/2019/05/new-research-how-effective-is-basic.html "Google Security Blog: How effective is basic account hygiene")）

   **怎么做：** 先给邮箱开启，再给银行和社交账号开启。能用验证器应用或安全密钥就用；短信验证码也远好于没有。

   *微软的数据来自企业账户（预印本）；谷歌的数据是其自动登录验证，而非用户自己开启的两步验证。短信验证码可能被换卡（SIM 卡劫持）攻击绕过：一项研究测试的美国五家预付费运营商都能被骗办理换卡。*

1. **使用反恶意软件**：微软遥测数据显示，没有杀毒保护的电脑被感染的可能性是有保护电脑的 5.5 倍。（来源：[Microsoft Security Intelligence Report v14 2013](https://isc.sans.edu/diary/15659 "Microsoft Security Intelligence Report v14 (via SANS ISC)"); [Lévesque et al. 2013](https://people.scs.carleton.ca/~soma/pubs/levesque-ccs2013.pdf "Lévesque et al., A Clinical Study of Risk Factors Related to Malware Infections (ACM CCS)")）

   **怎么做：** Windows 上保持自带的 Microsoft Defender 开启即可；Mac、iPhone 和安卓手机都有内置防护，不需要另外购买安全软件。

   *系统自带的防护就算数。这是厂商的观察数据，经第三方转述，有无防护的电脑在其他方面也有差异；一项研究发现 20% 的用户被杀毒软件漏检的程序感染。*

1. **保持杀毒软件更新**：实时防护保持更新的个人和小企业电脑感染率为 0.6%，防护过期的为 2.2%，没有防护的为 2.4%。（来源：[Microsoft Security Intelligence Report v17 2014](https://www.tomsguide.com/us/danger-stale-av-software,news-19928.html "Microsoft Security Intelligence Report v17 (via Tom's Guide)")）

   **怎么做：** 用系统自带的防护就无需操作，它会随系统一起更新；如果用付费杀毒软件，别让订阅过期。

   *厂商的观察数据，经第三方转述。*

1. **只安装可信来源的软件**：只从 Google Play 安装应用的安卓设备，装到有害应用的概率只有其他设备的九分之一。（来源：[Google 2018](https://android-developers.googleblog.com/2018/03/android-security-2017-year-in-review.html "Google, Android Security 2017 Year in Review")）

   **怎么做：** 只从官方应用商店或软件官网安装。在中国大陆，可理解为只用手机厂商自带的官方应用商店，不安装来路不明的 APK。

   *谷歌关于自家商店的观察数据；安装外部应用的设备可能在其他方面也不同。*

### 接下来：有较强间接证据的建议

- **不同账户使用不同密码**：在一项大型攻击模拟中，攻击者只要拿到用户在别的网站泄露的一个密码和少量个人信息，100 次猜测内就能攻破 73% 以上普通用户的账户。（来源：[Wang et al. 2016](https://www.passwordresearch.com/papers/paper763.html "Wang et al., Targeted Online Password Guessing (ACM CCS)")）

  **怎么做：** 让密码管理器为每个账户生成不同的密码，手机或浏览器自带的就可以。先从邮箱和银行账户开始。

- **及时更新设备**：在拥有 1000 台以上电脑的企业中，打补丁最慢的企业（90% 的电脑要 500 天才更新，最快的不到 10 天）遇到的恶意软件更多。（来源：[Kotzias et al. 2019](https://dev.ndss-symposium.org/wp-content/uploads/2019/02/ndss2019_03B-1-2_Kotzias_paper.pdf "Kotzias et al., Mind Your Own Business (NDSS)")）

  **怎么做：** 打开自动更新（iPhone：设置 > 通用 > 软件更新 > 自动更新；Windows：设置 > Windows 更新），提示重启时就重启。

- **定期备份数据**：2024 年的一项勒索软件调查中，78% 的美国州和地方政府受害机构（所有行业为 68%）靠备份恢复了被加密的数据。（来源：[Sophos 2024](https://www.sophos.com/en-us/blog/the-state-of-ransomware-in-state-and-local-government-2024 "Sophos, State of Ransomware in State and Local Government")）

  **怎么做：** 打开手机的云备份（iCloud 或 Google One；国内手机可用厂商云服务），并把家庭照片和重要文件在另一个云服务或移动硬盘上再存一份。

## 证据并不支持的热门建议

- **密码要混合字母、数字和符号**：一项研究跟踪了 154 人约 147 天的真实密码，发现使用符号和数字的密码更容易被重复使用。美国 NIST 指南现已规定服务方“不得”强制这类组合规则。（来源：[Pearman et al. 2017](https://users.ece.cmu.edu/~lbauer/papers/2017/ccs2017-password-reuse.pdf "Pearman et al., Let's go in for a closer look (ACM CCS)"); [NIST SP 800-63B-4 2025](https://pages.nist.gov/800-63-4/sp800-63b.html "NIST SP 800-63B-4, section 3.1.1.2")）

  **建议改为：** 改用长密码：三四个随机单词组成的短语，或者让密码管理器生成。

  *这是小样本中的相关性，不能证明混合字符导致重复使用；就强度而言，长度更重要。*

- **用符号替换密码中的字母**：破解工具早已把“@ 代替 a”这类常见替换考虑在内，几乎不增加强度；例如“pAsswOrd”需要的猜测次数是“p@ssw0rd”的 4000 倍。（来源：[Ur et al. 2016](https://www.cmu.edu/news/stories/archives/2016/july/password-perceptions.html "Ur et al., Do Users' Perceptions of Password Security Match Reality? (CHI), via CMU News")）

  **建议改为：** 与其加符号，不如加长度；密码管理器生成的随机密码比任何替换都强。

  *基于模拟破解，而非真实攻击。*

## 方法

这些建议来自一项专家排名研究（[Redmiles 等，USENIX Security 2020](https://securityadvice.cs.umd.edu/expert-ranking.html)）中排名前 40 的条目，其中两条几乎相同的建议已合并，共 39 条。该研究发现专家认为 89% 的网上安全建议都“有效”，普通人因此无从取舍。我们为每条建议找出最好的证据，并按上面的标准打分。排名中每条建议只由约 41 位专家中的 3 位评分，相邻名次差距很小，因此“前 40”应理解为一组公认的好建议，而非精确排序。

全部 39 条建议及其来源见[英文版完整表格](README.md#all-tips)。本项目面向个人，不构成专业建议。

## 参与

觉得某个评分不对？可以用中文[提交评分质疑](https://github.com/Dinosung/SafeDefaults/issues/new?template=grade.yml)，附上研究链接和支持你观点的原文即可。

## 许可

文字和数据采用 [CC BY 4.0](LICENSE) 许可。
