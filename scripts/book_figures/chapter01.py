"""Redraw the preface and chapter 1. Run from any working directory."""

from style import Figure, PALE, MID


def core():
    f = Figure('Agent 的三类功能', '三行分别表示模型、上下文和工具的功能；不表示三个独立的软件模块。', 350)
    for y, title, metaphor, detail in [
        (30, 'LLM', '大脑', '理解任务，规划并选择下一步'),
        (130, '上下文', '当前决策视野', '承载指令、观测、历史和任务状态'),
        (230, '工具', '感官和手脚', '获取外部信息，或执行实际操作'),
    ]:
        f.box(30, y, 220, 80, title, metaphor)
        f.rect(275, y, 415, 80, fill='#ffffff')
        f.text(482, y + 46, detail)
    f.save('fig0-1.svg')


def roadmap():
    f = Figure('全书结构', '左列构建 Agent，右列评估并提升能力；各章标题列出阅读顺序。', 620)
    f.text(185, 38, '构建 Agent', size=22, bold=True)
    f.text(535, 38, '评估与能力提升', size=22, bold=True)
    left = ['1  AI Agent 入门', '2  上下文工程', '3  用户记忆和知识库', '4  工具', '5  Coding Agent 与通用 Agent', '6  交互：观测与动作空间']
    right = ['7  Agent 的评估', '8  模型后训练', '9  Agent 的持续进化', '10  多 Agent 协作']
    for i, title in enumerate(left):
        f.box(25, 65 + i * 80, 320, 58, title)
    for i, title in enumerate(right):
        f.box(375, 65 + i * 80, 320, 58, title, fill=MID if i == 0 else PALE)
    f.rect(375, 410, 320, 135, fill='#ffffff', dashed=True)
    f.text(535, 445, '评估贯穿构建与改进', bold=True)
    f.text(535, 479, '后训练更新参数\n持续进化更新系统\n协作改变任务组织', size=16)
    f.text(360, 595, '先理解各部分如何工作，再验证和改进完整系统。', size=16)
    f.save('fig0-2.svg')


def boundary():
    f = Figure('Agent、Model、Harness 与环境', 'Model 与 Harness 同属 Agent，二者不互相包含。环境在 Agent 外，通过工具接口交互。', 580)
    f.rect(20, 20, 455, 540, fill='#ffffff')
    f.text(247, 53, 'Agent', size=22, bold=True)
    f.box(55, 75, 385, 85, 'Model（LLM）', '理解、规划和决策', fill=MID)
    f.rect(55, 230, 385, 300, fill=PALE)
    f.text(247, 265, 'Harness', size=22, bold=True)
    f.box(80, 287, 335, 55, '上下文管理', fill='#ffffff')
    f.box(80, 358, 335, 55, '工具接口与调用调度', fill='#ffffff')
    f.text(247, 455, '运行循环与状态管理', bold=True)
    f.text(247, 495, '约束 · 验证 · 纠正')
    f.path([(140, 230), (140, 160)])
    f.text(133, 196, '上下文', size=16, anchor='end')
    f.path([(355, 160), (355, 230)])
    f.text(362, 196, '决策', size=16, anchor='start')
    f.box(535, 270, 165, 210, '环境', '文件与数据库\n网页与外部服务\n用户、其他 Agent\n物理或仿真世界')
    f.path([(535, 315), (440, 315)])
    f.text(505, 298, '观测', size=16)
    f.path([(440, 386), (535, 386)])
    f.text(505, 371, '行动', size=16)
    f.save('fig1-1.svg')


def learning():
    f = Figure('Agent 能力更新的三条路径', '三条路径按更新对象区分，不表示能力高低或固定先后顺序。', 455)
    items = [
        ('上下文适应', '当前任务', '加入示例、观测和任务状态', '下一次调用据此调整行为'),
        ('外部产物更新', '跨任务', '修改知识、指令、Skill 或程序', '后续任务加载新版本'),
        ('模型参数更新', '训练与部署', '用筛选后的数据进行后训练', '部署并评估新的模型版本'),
    ]
    for i, (title, time, action, outcome) in enumerate(items):
        y = 25 + i * 130
        f.box(25, y, 210, 100, title, time)
        f.path([(235, y + 50), (275, y + 50)])
        f.rect(280, y, 415, 100, fill='#ffffff')
        f.text(487, y + 37, action)
        f.text(487, y + 72, outcome, size=16)
    f.text(360, 439, '三条路径可以配合使用；更新结果都需要验证。', size=16)
    f.save('fig1-2.svg')


def ablation():
    f = Figure('上下文消融实验', 'Kimi K3 于 2026 年 8 月 25 日的五组运行。历史消息消融也移除此前的推理和工具结果。', 565)
    f.box(25, 20, 670, 75, '固定系统提示词、当前任务和工具实现', '同一四币种收入任务；每组最多运行 5 轮')
    f.text(190, 132, '输入条件', bold=True)
    f.text(510, 132, '这次运行的结果', bold=True)
    rows = [
        ('完整上下文', '正确完成'),
        ('不提供工具定义', '未调用工具；说明没有换汇工具'),
        ('工具结果内容置空', '重复调用，达到轮数上限'),
        ('不保留历史推理信息', '正确完成'),
        ('不保留历史消息', '重复调用，达到轮数上限'),
    ]
    for i, (condition, result) in enumerate(rows):
        y = 153 + i * 67
        f.rect(25, y, 275, 52, fill=PALE)
        f.text(162, y + 32, condition, size=17)
        f.path([(300, y + 26), (332, y + 26)])
        f.rect(337, y, 358, 52, fill='#ffffff')
        f.text(516, y + 32, result, size=17)
    f.text(360, 521, '“不保留历史”同时移除此前的模型回复、调用与结果。', size=16)
    f.text(360, 548, '工具定义提供选项，结果提供事实，历史保存进度。', size=16)
    f.save('fig1-3.svg')


def trajectory():
    f = Figure('三笔收入的简化轨迹', '每次调用都带上稳定前缀和截至当前的消息。三笔收入示例包含三次模型调用、三次工具调用。', 700)
    f.box(25, 20, 670, 65, '每次调用：稳定前缀 + 截至当前的轨迹消息')
    f.text(185, 122, '模型本轮看到的信息', bold=True)
    f.text(535, 122, '模型输出与实际执行', bold=True)
    inputs = [
        ('第 1 次调用', '任务：三笔收入汇总\n250 万美元、210 万欧元\n180 万英镑'),
        ('第 2 次调用', '此前消息 + 两条换汇结果\n欧元折合 2,282,608.70 美元\n英镑折合 2,278,481.01 美元'),
        ('第 3 次调用', '此前消息 + 计算结果\n总额 7,061,089.71 美元\n平均 2,353,696.57 美元'),
    ]
    outputs = [
        ('请求两次换汇', 'Harness 调度换汇工具\n结果写入两条工具消息'),
        ('请求一次代码计算', 'Harness 调度代码工具\n计算总额与平均值'),
        ('返回最终答案', '总额 7,061,089.71 美元\n平均 2,353,696.57 美元'),
    ]
    for i, ((title, detail), (result, execution)) in enumerate(zip(inputs, outputs)):
        y = 145 + i * 175
        f.box(25, y, 320, 137, title, detail)
        f.path([(345, y + 66), (375, y + 66)])
        f.box(380, y, 315, 137, result, execution, fill='#ffffff')
        if i < 2:
            f.path([(535, y + 137), (535, y + 157), (185, y + 157), (185, y + 175)])
    f.text(360, 677, '共 3 次模型调用、3 次工具调用；连线表示消息进入下一轮。', size=16)
    f.save('fig1-4.svg')


def hosted():
    f = Figure('客户端循环与服务端托管循环', '两种方式都由模型决定调用。区别在于谁负责循环；工具执行和模型推理是不同职责。', 560)
    for y, title in [(25, '实验 1-2：客户端组织循环'), (290, '实验 1-3：服务端组织循环')]:
        f.text(360, y, title, size=20, bold=True)
    f.box(25, 100, 185, 100, '客户端 Harness', '请求模型\n调度工具并回传结果')
    f.rect(320, 55, 375, 190, fill='#ffffff', dashed=True)
    f.text(507, 85, 'Moonshot 服务端', bold=True)
    f.box(350, 100, 315, 52, 'Kimi K3：生成调用请求')
    f.box(350, 174, 315, 52, 'Formula：执行搜索')
    f.path([(210, 115), (350, 115)])
    f.path([(350, 140), (210, 140)])
    f.text(265, 98, '请求／决策', size=16)
    f.path([(210, 175), (350, 190)])
    f.path([(350, 215), (210, 199)])
    f.text(265, 238, '调用／结果', size=16)
    f.box(25, 355, 145, 120, '客户端', '提交任务\n接收回答')
    f.rect(280, 320, 415, 210, fill='#ffffff', dashed=True)
    f.text(487, 350, 'Responses API 服务端', bold=True)
    f.box(305, 375, 155, 120, '托管 Harness', '维护调用循环\n回传工具结果')
    f.box(500, 368, 170, 55, '模型决策')
    f.box(500, 445, 170, 63, '托管工具', fill=MID)
    f.path([(170, 390), (280, 390)])
    f.path([(280, 422), (170, 422)])
    f.text(226, 371, '任务／回答', size=16)
    f.path([(460, 389), (500, 389)])
    f.path([(500, 408), (460, 408)])
    f.path([(460, 463), (500, 463)])
    f.path([(500, 485), (460, 485)])
    f.save('fig1-5.svg')


def loop():
    f = Figure('自主 Agent 的执行循环', '先判断响应类型，再执行工具或返回回复；最终输出工具在工具执行后结束，不能走无调用分支。', 635)
    f.box(40, 25, 435, 65, '组织上下文，调用模型')
    f.box(40, 135, 435, 65, '检查本轮响应与运行状态')
    f.path([(257, 90), (257, 135)])
    f.path([(475, 166), (540, 166)])
    f.box(540, 118, 155, 103, '回复或暂停', '无工具调用\n或需用户补充', fill='#ffffff')
    f.path([(257, 200), (257, 265)])
    f.text(270, 239, '有工具调用', size=16, anchor='start')
    f.box(40, 265, 435, 82, 'Harness 校验并调度', '工具执行，结果写回轨迹')
    f.path([(257, 347), (257, 400)])
    f.box(40, 400, 435, 80, '检查完成条件与运行预算', '完成验证；最终输出工具；轮数或错误上限')
    f.path([(475, 440), (540, 440)])
    f.box(540, 395, 155, 96, '结束或升级', '返回结果\n报告错误／转人工', fill='#ffffff')
    f.text(507, 421, '满足', size=16)
    f.path([(257, 480), (257, 525), (15, 525), (15, 58), (40, 58)])
    f.text(290, 521, '继续', size=16, anchor='start')
    f.text(360, 572, '工具调用被拒绝或执行失败时，也要记录明确结果。', size=16)
    f.text(360, 604, '是否重试、等待或转人工，由错误类型和运行规则决定。', size=16)
    f.save('fig1-6.svg')


if __name__ == '__main__':
    for draw in (core, roadmap, boundary, learning, ablation, trajectory, hosted, loop):
        draw()
