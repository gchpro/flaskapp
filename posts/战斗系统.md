title: 战斗系统
date: 2016-12-17 16:25:00
summary: 一场战斗默认最多30回合(round)

===

# 战斗系统

一场战斗默认最多30回合（round）。

步骤：

1. 根据速度计算出手顺序。包括判断"Speed","DSpeed"加速，减速buff.如果速度相同则根绝战力排序。
2. 确定出手顺序后，设置出手的角色<code>self.pkpid = pid</code>；每一轮的战斗数据记录在<code>self.turnlog.append({'t':i,'round':i,'act':[]})</code>里。
3. "JiFeng","LianNu"可以出手两次,_roundNu += 1



## 战斗规则
* "JiFeng","Liannu"技能出手次数加1
* "XuanYun"状态下无法出手，但士气值上升30点
* 如果士气值(Mor)达到100，且没有被沉默("ChenMo")则使用技能；否则检查是否有被动技能('bdskill')，执行技能，记入战斗日志。
* 技能结束则，删除技能状态。
* 