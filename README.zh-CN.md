# SafeDefaults

[English](README.md)

**专家最看重的 39 条安全建议，按“有没有证据证明有用”打分。**

只有 **5** 条有实测结果支持，且大多来自公司自己的数据；**20** 条没有直接证据或证据互相矛盾，但通常仍是合理的建议；另有 **1** 条流行建议，证据表明它没什么用。

## 评分

| 评分 | 含义 |
|---|---|
| 🟢 A | 实测：照做的人被感染、被盗号或被入侵的更少 |
| 🟡 B | 间接：攻击模拟、更新普及率，或威胁有多常见 |
| ⚪ C | 未证实：没有找到直接证据，或证据互相矛盾；通常仍是合理的建议 |
| 🔴 X | 证据不支持：几乎没有实测效果，甚至适得其反 |

<details><summary>术语</summary>

- **两步验证（2FA）**：输入密码后的第二道验证，例如手机上的验证码。
- **验证器应用**：显示 6 位登录验证码的免费应用，如 Google 或 Microsoft Authenticator。
- **通行密钥（passkey）、安全密钥**：由手机、电脑或小型 USB 密钥替你确认的登录方式，无法被钓鱼。
- **密码管理器**：生成并记住密码的应用，手机和浏览器通常自带。
- **钓鱼**：骗取密码、验证码或钱财的假邮件、短信、电话或网站。
- **恶意软件**：病毒、勒索软件等有害程序。

</details>

## 先做这几件事：有实测证据的建议

1. **开启两步验证（2FA）**

   **怎么做：** 邮箱、微信、支付宝、QQ、银行等应用：在“账号与安全”或“安全中心”里开启登录保护或设备锁。iPhone：设置 > 你的名字 > 登录与安全（通常已开启）。谷歌账户：myaccount.google.com/security。能用通行密钥或安全密钥最好，其次是验证器应用；短信验证码也远好于没有。验证码绝不告诉任何主动联系你的人。

   <details><summary>依据</summary>

   在被标记为可疑登录的微软企业账户中，两步验证将账户被盗风险降低了 99.22%，验证器应用的效果优于短信验证码。谷歌发现，在可疑登录时向辅助手机号发送短信验证码，挡住了 100% 的自动化攻击、96% 的批量钓鱼和 76% 的定向攻击。 *微软的数据是企业账户的预印本研究；谷歌的数据是其自动登录验证，而非用户自己开启的两步验证。短信和应用里的验证码仍可能被实时骗走，短信还可能因换卡被截获；只有通行密钥（passkey）和安全密钥能防钓鱼。*（来源：[Meyer et al. 2023](https://arxiv.org/abs/2305.00945 "Meyer et al., How effective is multifactor authentication at deterring cyberattacks? (Microsoft)")；[Google Security Blog 2019](https://security.googleblog.com/2019/05/new-research-how-effective-is-basic.html "Google Security Blog: How effective is basic account hygiene") · vendor data）

   </details>

1. **不要把密码告诉任何人，包括“IT 人员”**

   **怎么做：** 真正的银行、IT 部门、微软或苹果都不会索要你的密码或发给你的验证码。有人这样要求时（电话、邮件或聊天），停下，并通过你已知的官方号码联系对方核实。

   <details><summary>依据</summary>

   谷歌发现，把密码交给钓鱼者的人，账户被盗的可能性是普通用户的 400 倍。 *谷歌关于自家账户的数据；指的是交给冒充可信方的骗子，而非朋友或真正的 IT 人员。*（来源：[Thomas et al. 2017](https://faculty.cc.gatech.edu/~frankli/papers/google_account_compromise.pdf "Thomas et al., Data breaches, phishing, or malware? Understanding the risks of stolen credentials (ACM CCS)") · vendor data）

   </details>

1. **使用反恶意软件**

   **怎么做：** Windows 自带 Microsoft Defender：在开始菜单搜索“Windows 安全中心”，确认“病毒和威胁防护”已开启。电脑预装的杀毒软件试用版到期要求付费时，不必续费，卸载后 Defender 会自动开启。Mac 和 iPhone 有内置防护；国内安卓手机一般有厂商自带的安全检测，不需要另外购买安全软件。

   <details><summary>依据</summary>

   微软遥测数据显示，没有杀毒保护的电脑被感染的可能性是有保护电脑的 5.5 倍。 *系统自带的防护就算数。这是厂商的观察数据，经第三方转述，有无防护的电脑在其他方面也有差异；一项研究发现 20% 的用户被杀毒软件漏检的程序感染。*（来源：[Microsoft Security Intelligence Report v14 2013](https://isc.sans.edu/diary/15659 "Microsoft Security Intelligence Report v14 (via SANS ISC)")；[Lévesque et al. 2013](https://people.scs.carleton.ca/~soma/pubs/levesque-ccs2013.pdf "Lévesque et al., A Clinical Study of Risk Factors Related to Malware Infections (ACM CCS)") · vendor data）

   </details>

1. **保持杀毒软件更新**

   **怎么做：** 用系统自带的防护就无需操作，它会随系统一起更新。

   <details><summary>依据</summary>

   实时防护保持更新的个人和小企业电脑感染率为 0.6%，防护过期的为 2.2%，没有防护的为 2.4%。 *厂商的观察数据，经第三方转述。*（来源：[Microsoft Security Intelligence Report v17 2014](https://www.tomsguide.com/us/danger-stale-av-software,news-19928.html "Microsoft Security Intelligence Report v17 (via Tom's Guide)") · vendor data）

   </details>

1. **只安装可信来源的软件**

   **怎么做：** 只从官方应用商店或软件官网安装。在中国大陆，可理解为只用手机厂商自带的官方应用商店，不安装来路不明的 APK。

   <details><summary>依据</summary>

   只从 Google Play 安装应用的安卓设备，装到有害应用的概率只有其他设备的九分之一。 *谷歌关于自家商店的观察数据；国内厂商应用商店没有同类公开数据，“只用厂商官方商店”是推论。*（来源：[Google 2018](https://android-developers.googleblog.com/2018/03/android-security-2017-year-in-review.html "Google, Android Security 2017 Year in Review") · vendor data）

   </details>

### 接下来：值得做，有间接证据

- **不同账户使用不同密码**（🟡 B）

  **怎么做：** 选一个在你所有设备上都能用的密码管理器，让它为每个账户生成不同的密码。先改一个账户，确认每台设备都能登录，再改邮箱和银行。没有重复使用、能正常用的密码不必改。

  <details><summary>依据</summary>

  在一项大型攻击模拟中，攻击者只要拿到用户在别的网站泄露的一个密码和少量个人信息，100 次猜测内就能攻破 73% 以上普通用户的账户。（来源：[Wang et al. 2016](https://www.passwordresearch.com/papers/paper763.html "Wang et al., Targeted Online Password Guessing (ACM CCS)") · attack simulation）

  </details>

- **及时更新设备**（🟡 B）

  **怎么做：** 打开自动更新，提示重启时就重启。iPhone/iPad：设置 > 通用 > 软件更新 > 自动更新 > 开启“自动安装”。安卓/鸿蒙手机：打开设置，搜索“软件更新”，开启自动下载并安装。Windows：设置 > Windows 更新。不再收到更新的旧设备，不要再用来登录银行或邮箱。

  <details><summary>依据</summary>

  在拥有 1000 台以上电脑的企业中，打补丁最慢的企业（90% 的电脑要 500 天才更新，最快的不到 10 天）遇到的恶意软件更多。 *论文称这只是一项简单的比较，没有给出恶意软件数量或统计检验，因此评为 B。*（来源：[Kotzias et al. 2019](https://dev.ndss-symposium.org/wp-content/uploads/2019/02/ndss2019_03B-1-2_Kotzias_paper.pdf "Kotzias et al., Mind Your Own Business (NDSS)") · observational study）

  </details>

- **定期备份数据**（🟡 B）

  **怎么做：** iPhone/iPad：设置 > 你的名字 > iCloud > iCloud 云备份 > 开启。安卓/鸿蒙手机：使用厂商云服务（华为云空间、小米云服务、OPPO/vivo 云服务）。云空间不足时，只在系统设置里付费升级，不要通过弹窗或邮件付款。再用一个现有的 U 盘或移动硬盘存一份照片和文件更好。

  <details><summary>依据</summary>

  2024 年一项覆盖 14 个国家的勒索软件调查中，78% 的州和地方政府受害机构（全球所有行业为 68%）靠备份恢复了被加密的数据。（来源：[Sophos 2024](https://www.sophos.com/en-us/blog/the-state-of-ransomware-in-state-and-local-government-2024 "Sophos, State of Ransomware in State and Local Government") · survey）

  </details>

- **警惕钓鱼和诈骗**（🟡 B）

  **怎么做：** 任何电话、短信、邮件或弹窗索要密码、验证码、转账或远程控制电脑，一律停下：挂断或关闭，再通过你已知的官方号码（如银行卡背面的电话）核实。自称客服、公检法要求转账的，都是诈骗。软件只从官网或手机自带应用商店下载，别点下载站的“高速下载”按钮，安装时取消勾选捆绑软件。

  <details><summary>依据</summary>

  被钓鱼骗走密码的人，账户被盗的可能性是普通谷歌用户的 400 倍；2024 年美国 FBI 收到最多的投诉类型就是钓鱼/仿冒（193,407 起）。（来源：[Thomas et al. 2017](https://faculty.cc.gatech.edu/~frankli/papers/google_account_compromise.pdf "Thomas et al., Data breaches, phishing, or malware? Understanding the risks of stolen credentials (ACM CCS)")；[FBI IC3 2025](https://www.ic3.gov/AnnualReport/Reports/2024_IC3Report.pdf "FBI IC3, 2024 Internet Crime Report") · vendor data; official statistics）

  </details>

**就这些。** 以上 9 步涵盖了证据支持的做法。

## 证据并不支持的热门建议

- **用符号替换密码中的字母**：破解工具早已把“@ 代替 a”这类常见替换考虑在内，几乎不增加强度；一个猜测模型预测，人们以为更强的“p@ssw0rd”反而比“pAsswOrd”少 4000 倍的猜测次数就会被破解。（来源：[Ur et al. 2016](https://www.cmu.edu/news/stories/archives/2016/july/password-perceptions.html "Ur et al., Do Users' Perceptions of Password Security Match Reality? (CHI), via CMU News") · attack simulation）

  **建议改为：** 与其加符号，不如加长度：几个随机词语（拼音或英文均可）拼在一起，或用密码管理器生成。没有重复使用、能正常用的密码不必改。

## 方法

这些建议来自一项专家排名研究（[Redmiles 等，USENIX Security 2020](https://www.usenix.org/system/files/sec20-redmiles.pdf)）中排名前 40 的条目，其中两条几乎相同的建议已合并，共 39 条。该研究发现专家认为 89% 的网上安全建议都“有效”，普通人因此无从取舍。我们为每条建议找出最好的证据，并按上面的标准打分。排名中每条建议只由约 41 位专家中的 3 位评分，相邻名次差距很小，因此“前 40”应理解为一组公认的好建议，而非精确排序。

评分说明的是有哪类证据，而不是证据有多强；公司测量自家产品的数据是最弱的一类 A。部分谷歌来源在中国大陆可能无法直接访问。全部 39 条建议及其来源见[英文版完整表格](README.md#all-tips)。本项目不构成专业建议。

## 参与

觉得某个评分不对？可以用中文[提交评分质疑](https://github.com/Dinosung/SafeDefaults/issues/new?template=grade.yml)，附上研究链接和支持你观点的原文即可。

## 许可

文字和数据采用 [CC BY 4.0](LICENSE) 许可：注明出处并附链接，即可复制或改编（例如用于员工手册）。
