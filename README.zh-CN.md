# SafeDefaults

[English](README.md)

**专家最看重的 39 条安全建议，按“有没有证据证明有用”打分。**

只有 **5** 条有实测证据证明能减少损失；**16** 条还没有找到直接证据；**4** 条（其中几条出现在热门清单上）的证据反而不支持。

C 只说明还没有研究证明它有效，不代表建议不好：离开时锁屏依然值得做，备份数据（B）更是如此。

## 评分

| 评分 | 含义 |
|---|---|
| 🟢 A | 实测：照做的人被感染、被盗号或被入侵的更少 |
| 🟡 B | 间接：攻击模拟、更新普及率，或威胁有多常见 |
| ⚪ C | 尚未测量：没有找到直接证据，但通常是合理的建议 |
| 🔴 X | 证据不支持：几乎没有实测效果，甚至适得其反 |

## 先做这几件事：有实测证据的建议

1. **开启两步验证（2FA，又称双重认证）**：谷歌发现，仅向辅助手机号发送短信验证码，就挡住了 100% 的自动化攻击、96% 的批量钓鱼和 76% 的定向攻击；微软测得开启后账户被盗风险降低 99% 以上。（来源：[Google Security Blog 2019](https://security.googleblog.com/2019/05/new-research-how-effective-is-basic.html "Google Security Blog: How effective is basic account hygiene"); [Meyer et al. 2023](https://arxiv.org/abs/2305.00945 "Meyer et al., How effective is multifactor authentication (Microsoft)")）

   **怎么做：** 先给邮箱开启，再给银行和社交账号开启。能用验证器应用或安全密钥就用；短信验证码也远好于没有。

   *短信验证码可能被换卡（SIM 卡劫持）攻击绕过：一项研究发现美国五大运营商都能被骗办理换卡。*

1. **及时更新设备**：在 2.8 万家企业的 8200 万台电脑上，及时打补丁与遇到恶意软件的次数显著相关。（来源：[Kotzias et al. 2019](https://dev.ndss-symposium.org/wp-content/uploads/2019/02/ndss2019_03B-1-2_Kotzias_paper.pdf "Kotzias et al., Mind Your Own Business (NDSS)")）

   **怎么做：** 打开自动更新（iPhone：设置 > 通用 > 软件更新 > 自动更新；Windows：设置 > Windows 更新），提示重启时就重启。

   *数据来自企业电脑；作者称这只是一项简单的比较。*

1. **使用反恶意软件**：微软遥测数据显示，没有杀毒保护的电脑被感染的可能性是有保护电脑的 5.5 倍。（来源：[Microsoft Security Intelligence Report v14 2013](https://isc.sans.edu/diary/15659 "Microsoft Security Intelligence Report v14 (via SANS ISC)")）

   **怎么做：** Windows 上保持自带的 Microsoft Defender 开启即可；Mac、iPhone 和安卓手机都有内置防护，不需要另外购买安全软件。

   *系统自带的防护就算数。这是厂商的观察数据，经第三方转述。*

1. **保持杀毒软件更新**：实时防护保持更新的电脑感染率为 0.6%，防护过期的为 2.2%。（来源：[Microsoft Security Intelligence Report v17 2014](https://www.tomsguide.com/us/danger-stale-av-software,news-19928.html "Microsoft Security Intelligence Report v17 (via Tom's Guide)")）

   **怎么做：** 用系统自带的防护就无需操作，它会随系统一起更新；如果用付费杀毒软件，别让订阅过期。

   *厂商的观察数据，经第三方转述。*

1. **只安装可信来源的软件**：只从 Google Play 安装应用的安卓设备，装到有害应用的概率只有其他设备的九分之一。（来源：[Google 2018](https://android-developers.googleblog.com/2018/03/android-security-2017-year-in-review.html "Google, Android Security 2017 Year in Review")）

   **怎么做：** 只从官方应用商店或软件官网安装。在中国大陆，可理解为只用手机厂商自带的官方应用商店，不安装来路不明的 APK。

## 证据并不支持的热门建议

- **把密码记在脑子里**：靠记忆管理密码的人最终会重复使用密码：一项大型研究发现，普通用户平均只有 6.5 个密码，每个用在 3.9 个网站上。（来源：[Florencio & Herley 2007](https://www.www2007.cpsc.ucalgary.ca/papers/paper620.pdf "Florencio & Herley, A Large-Scale Study of Web Password Habits (WWW)"); [Wash et al. 2016](https://www.usenix.org/system/files/conference/soups2016/soups2016-paper-wash.pdf "Wash et al., Understanding Password Choices (SOUPS)")）

  **建议改为：** 让密码管理器替你生成和记住密码，手机或浏览器自带的（iCloud 钥匙串、谷歌密码管理器）就可以。

- **密码要混合字母、数字和符号**：美国 NIST 数字身份指南规定，服务方“不得”强制这类组合规则；长度和排查已泄露密码更重要。（来源：[NIST SP 800-63B-4 2025](https://pages.nist.gov/800-63-4/sp800-63b.html "NIST SP 800-63B-4, section 3.1.1.2")）

  **建议改为：** 改用长密码：三四个随机单词组成的短语，或者让密码管理器生成。

- **用符号替换密码中的字母**：破解工具会优先尝试“@ 代替 a”这类常见替换，几乎不增加强度。（来源：[Ur et al. 2016](https://www.cmu.edu/news/stories/archives/2016/july/password-perceptions.html "Ur et al., password perceptions study (CHI), CMU News")）

  **建议改为：** 与其加符号，不如加长度；密码管理器生成的随机密码比任何替换都强。

- **使用 VPN**：一项研究分析了 283 款安卓 VPN 应用：38% 至少被一款 VirusTotal 引擎报告为恶意软件（被 5 款以上报告的只有 4%），18% 的应用使用不加密的隧道协议。我们没有找到证明 VPN 对普通用户有益的数据。（来源：[Ikram et al. 2016](https://research.csiro.au/isp/wp-content/uploads/sites/106/2016/08/paper-1.pdf "Ikram et al., An Analysis of the Privacy and Security Risks of Android VPN Apps (IMC)")）

  **建议改为：** 在家上网不需要为安全使用 VPN；公共 Wi-Fi 上，https 网站本身已经加密。如果确实要用，选知名公司的付费服务，避开免费 VPN 应用。

  *这里说的是 VPN 应用市场的安全风险，不涉及访问用途；口碑好的付费 VPN 属于 C（没有证据说明好坏）。*

## 方法

这些建议来自一项专家排名研究（[Redmiles 等，USENIX Security 2020](https://securityadvice.cs.umd.edu/expert-ranking.html)）中排名前 40 的条目，其中两条几乎相同的建议已合并，共 39 条。该研究发现专家认为 89% 的网上安全建议都“有效”，普通人因此无从取舍。我们为每条建议找出最好的证据，并按上面的标准打分。

全部 39 条建议及其来源见[英文版完整表格](README.md#all-tips)。本项目面向个人，不构成专业建议。

## 参与

觉得某个评分不对？可以用中文[提交评分质疑](https://github.com/Dinosung/SafeDefaults/issues/new?template=grade.yml)，附上研究链接和支持你观点的原文即可。

## 许可

文字和数据采用 [CC BY 4.0](LICENSE) 许可。
