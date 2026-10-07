"""Chapter 2 figures, added in the order of the manuscript revision."""
from style import Figure, PALE, MID


def composition():
    f = Figure('上下文的信息来源', '五类内容由 Harness 组织为当前调用的信息。行高用于排版。', 580)
    f.text(155, 36, '信息来源', bold=True)
    f.text(495, 36, '进入上下文的内容', bold=True)
    rows = [
        ('开发者与运行配置', '系统提示词', '身份、任务规则、行为要求'),
        ('工具注册与发现', '工具定义', '名称、用途与参数'),
        ('用户', '用户消息', '任务目标、补充要求'),
        ('模型', '模型回复', '回答、判断与工具请求'),
        ('工具执行', '工具结果', '查询数据、执行状态或错误'),
    ]
    for i, (source, title, detail) in enumerate(rows):
        y = 60 + i * 95
        f.box(25, y, 255, 75, source)
        f.path([(280, y+38), (315, y+38)])
        f.box(320, y, 375, 75, title, detail, fill='#ffffff')
    f.text(360, 563, 'Harness 选择并组织这些信息，供模型作出下一步决策。', size=16)
    f.save('fig2-1.svg')


def single():
    f = Figure('单轮请求与响应', 'Harness 提交系统规则与用户问题，模型生成回答，Harness 保存回答。', 425)
    f.box(25, 25, 250, 60, '客户端 Harness')
    f.box(445, 25, 250, 60, '模型服务')
    f.path([(150, 85), (150, 345)], arrow=False, dashed=True)
    f.path([(570, 85), (570, 345)], arrow=False, dashed=True)
    f.text(360, 137, '系统规则 + 用户问题', bold=True)
    f.path([(150, 157), (570, 157)])
    f.text(360, 188, '“你能帮我做什么？”', size=16)
    f.text(360, 248, '模型回复', bold=True)
    f.path([(570, 269), (150, 269)])
    f.text(360, 300, '根据系统规则介绍可提供的帮助', size=16)
    f.box(25, 345, 670, 58, 'Harness 将回答写入历史，供后续调用使用')
    f.save('fig2-2.svg')


def interaction():
    f = Figure('两轮模型调用与两次工具执行', '客户端维护历史，模型选择调用，两项查询独立执行后回传结果。', 660)
    for x, title in [(105, 'Harness'), (355, '模型服务'), (605, '查询工具')]:
        f.box(x-85, 20, 170, 56, title)
        f.path([(x, 76), (x, 590)], arrow=False, dashed=True)
    f.text(225, 117, '任务、规则与工具定义', size=16)
    f.path([(105, 135), (355, 135)])
    f.text(225, 180, '请求查询时间与天气', size=16)
    f.path([(355, 198), (105, 198)])
    f.parts.append('<rect x="185" y="233" width="340" height="27" fill="white"/>')
    f.text(355, 254, '校验参数后，并行执行两项查询', size=17)
    f.path([(105, 273), (605, 273)])
    f.box(505, 298, 190, 84, '执行查询', '当地时间 · 当前天气')
    f.parts.append('<rect x="185" y="388" width="340" height="27" fill="white"/>')
    f.text(355, 409, '两条工具结果，分别关联原请求', size=17)
    f.path([(605, 427), (105, 427)])
    f.text(225, 478, '原有消息 + 工具结果', size=16)
    f.path([(105, 497), (355, 497)])
    f.text(225, 542, '根据结果回答用户', size=16)
    f.path([(355, 560), (105, 560)])
    f.text(360, 625, '模型调用 2 轮；工具执行 2 次。时间沿竖直方向推进。', size=16)
    f.save('fig2-3.svg')


def growth():
    f = Figure('稳定前缀与消息历史', '两轮调用复用相同规则和工具定义，第二轮加入工具请求及结果。', 570)
    f.text(185, 36, '第 1 次调用', size=20, bold=True)
    f.text(535, 36, '第 2 次调用', size=20, bold=True)
    for x in [25, 375]:
        f.box(x, 60, 320, 75, '系统提示词', '相同的任务规则', fill=MID)
        f.box(x, 150, 320, 75, '工具定义', '相同的时间与天气接口', fill=MID)
        f.box(x, 275, 320, 65, '用户问题：时间与天气')
    f.text(360, 254, '上方为稳定前缀；下方为任务历史', size=16)
    f.box(375, 355, 320, 65, '新增：模型提出两个工具请求', fill='#ffffff')
    f.box(375, 435, 320, 65, '新增：时间和天气的工具结果', fill='#ffffff')
    f.text(185, 403, '随着执行推进，\n新的消息追加到历史末尾。', size=17)
    f.text(360, 548, '下一轮请求继续保留任务所需的历史，并加入最新进展。', size=16)
    f.save('fig2-4.svg')


def local():
    f = Figure('本地模型与客户端工具循环', '模型通过本地服务返回请求，客户端执行工具并把结果加入下一轮上下文。', 555)
    f.box(25, 190, 260, 145, '客户端 Harness', '组织消息，校验参数\n执行工具，保存结果\n决定继续或结束')
    f.box(455, 40, 240, 120, '本地模型服务', 'Ollama 或 vLLM\n加载模型并生成响应')
    f.box(455, 360, 240, 120, '工具与外部数据', '时区数据\n天气服务')
    f.path([(285, 221), (370, 221), (370, 95), (455, 95)])
    f.text(360, 73, '上下文', size=16)
    f.path([(455, 135), (405, 135), (405, 261), (285, 261)])
    f.text(495, 199, '工具请求或回答', size=16)
    f.path([(285, 292), (370, 292), (370, 403), (455, 403)])
    f.text(318, 375, '调用', size=16)
    f.path([(455, 445), (150, 445), (150, 335)])
    f.text(290, 430, '执行结果', size=16)
    f.text(360, 528, '客户端将工具结果写入历史，再调用本地模型。', size=16)
    f.save('fig2-5.svg')



def attention():
    f = Figure('注意力的信息汇总', '四词组教学示意，权重由作者设定，用于说明加权计算。', 505)
    f.box(190, 20, 340, 75, '当前位置：怎么样', 'Query 与各位置的 Key 匹配')
    f.path([(360, 95), (360, 135)])
    f.box(75, 140, 570, 58, '分数经缩放、掩码与 softmax 得到权重')
    for i, (word, weight) in enumerate([('北京', '0.35'), ('的', '0.05'), ('天气', '0.55'), ('怎么样', '0.05')]):
        x = 25+i*175
        f.path([(360, 198), (360, 213), (x+72, 213), (x+72, 230)])
        f.box(x, 230, 145, 85, word, '权重 '+weight, fill=MID if i==2 else PALE)
        f.path([(x+72, 315), (x+72, 345), (360, 345)], arrow=False)
    f.path([(360, 345), (360, 375)])
    f.box(120, 380, 480, 65, '各位置的 Value 按权重求和')
    f.text(360, 480, '权重合计为 1；词组与数值用于解释计算过程。', size=16)
    f.save('fig2-6.svg')


def measured_attention():
    import numpy as np
    from pathlib import Path
    root = Path(__file__).resolve().parents[2]
    data = np.load(root/'chapter2/attention_visualization/runs/exp2-2-qwen3-0.6b-20260730-v3/attention_matrices.npz')
    f = Figure('实测注意力矩阵', 'Qwen3-0.6B 同一次九 token 输入，各层对 16 个头求平均，线性灰度范围 0 到 1。', 460)
    f.text(360, 30, '输入：“北京 的 天气 怎么样”（9 个 token）', bold=True)
    for panel, layer in enumerate([0, 13, 27]):
        x=40+panel*235; y=95; cell=20
        f.text(x+90, 68, f'第 {layer+1} 层', bold=True)
        m=data[f'simple_layer_{layer}']
        assert m.shape==(9,9) and np.isfinite(m).all()
        assert np.max(np.abs(np.triu(m,1)))==0
        assert np.allclose(m.sum(axis=1),1,atol=.006)
        for r in range(9):
            for c in range(9):
                if c>r:
                    fill='#ededed'
                else:
                    g=round(255*(1-float(m[r,c])));fill=f'#{g:02x}{g:02x}{g:02x}'
                f.parts.append(f'<rect x="{x+c*cell}" y="{y+r*cell}" width="20" height="20" fill="{fill}" stroke="#cccccc" stroke-width="0.5"/>')
                if c>r:
                    f.path([(x+c*cell+7,y+r*cell+7),(x+c*cell+13,y+r*cell+13)],arrow=False)
        for t in [0,4,8]:
            f.text(x+cell*t+10, 298, str(t+1),size=16)
            f.text(x-8, y+cell*t+16,str(t+1),size=16,anchor='end')
    f.text(360, 333, '横轴：被读取的位置　　纵轴：查询位置', size=16)
    for i in range(100):
        g=round(255*(1-i/99));f.parts.append(f'<rect x="{210+i*3}" y="355" width="3" height="16" fill="rgb({g},{g},{g})"/>')
    f.text(195,370,'0',size=16)
    f.text(527,370,'1',size=16)
    f.text(360,402,'三个矩阵使用相同灰度标尺；斜线格为因果掩码区域。',size=16)
    f.text(360,438,'模型：Qwen3-0.6B；每层对 16 个注意力头取平均。',size=16)
    f.save('fig2-7.svg')


def prefix_cache():
    f = Figure('前缀缓存复用', '相同前缀复用已有 KV，首个变化位置及之后重新计算。', 445)
    rows=[('首次请求', ['A','B','C','D'],0), ('追加内容', ['A','B','C','D','E'],4), ('修改 C', ['A','B','C′','D','E'],2)]
    for row,(label,tokens,cached) in enumerate(rows):
        y=55+row*100
        f.text(100,y+34,label,bold=True)
        for j,t in enumerate(tokens):
            f.box(190+j*95,y,80,58,t,fill=MID if j<cached else '#ffffff')
    f.rect(120,370,24,24,fill=MID)
    f.text(155,389,'复用缓存',size=16,anchor='start')
    f.rect(360,370,24,24,fill='#ffffff')
    f.text(395,389,'执行计算',size=16,anchor='start')
    f.text(360,430,'共同前缀截至首个变化位置之前。',size=16)
    f.save('fig2-10.svg')


def template_message():
    f = Figure('聊天模板的消息结构', '用边界、角色、正文展示消息编码方式，具体标记由模型模板规定。', 335)
    f.text(360, 35, '一条消息在模型输入中的结构示意', size=20, bold=True)
    for x,w,title,detail in [(25,125,'起始边界','新消息开始'),(165,125,'角色','内容来源'),(305,250,'正文','消息内容对应的 token'),(570,125,'结束边界','当前消息结束')]:
        f.box(x,85,w,100,title,detail,fill=MID if title!='正文' else '#ffffff')
    f.path([(25,225),(695,225)])
    f.text(360,260,'按模板顺序展开，再转换为模型处理的 token 序列。',size=16)
    f.text(360,306,'图中展示功能位置；实际边界标记采用模型配套模板。',size=16)
    f.save('fig2-8.svg')


def template_conversion():
    f = Figure('消息列表到输入序列', '系统与用户消息按模板展开，随后给出助手生成起点。', 460)
    f.text(160,35,'客户端的消息列表',bold=True)
    f.text(525,35,'模板展开后的输入顺序',bold=True)
    f.box(25,80,265,100,'系统消息','查询实时数据，注明单位')
    f.box(25,230,265,100,'用户消息','温哥华现在几点，天气如何？')
    f.box(385,80,310,100,'系统角色与边界','查询实时数据，注明单位',fill='#ffffff')
    f.box(385,230,310,100,'用户角色与边界','温哥华现在几点，天气如何？',fill='#ffffff')
    f.path([(290,130),(385,130)])
    f.path([(290,280),(385,280)])
    f.path([(540,180),(540,230)])
    f.path([(540,330),(540,370)])
    f.box(385,375,310,55,'助手回复的生成起点',fill=MID)
    f.text(160,385,'同一组消息\n形成一段连续输入',size=17)
    f.save('fig2-9.svg')


def skills_discovery():
    f=Figure('Skills 渐进式披露','先查看目录，选中演示文稿能力后加载核心流程，再按步骤读取资料。',520)
    f.text(360,35,'目录：先知道有哪些能力',bold=True)
    for x,t in [(25,'文档处理'),(260,'演示文稿'),(495,'表格分析')]:
        f.box(x,60,200,65,t,fill=MID if x==260 else PALE)
    f.path([(360,125),(360,190)])
    f.text(380,163,'任务需要制作演示文稿',size=16,anchor='start')
    f.box(110,195,500,95,'加载核心流程','阅读论文 → 安排页面 → 制作 → 检查')
    f.path([(360,290),(360,330)])
    f.text(360,358,'执行到具体步骤，再读取相关资料',bold=True)
    for x,t in [(25,'图表规范'),(260,'文件格式说明'),(495,'预览与检查方法')]:
        f.box(x,390,200,60,t,fill='#ffffff')
    f.text(360,495,'目录用于选择；核心流程指导推进；参考资料补充细节。',size=16)
    f.save('fig2-11.svg')


def skills_history():
    f=Figure('Skills 在任务历史中的加载顺序','每个步骤给出本轮新增的信息，之前的相关消息继续保留。',545)
    rows=[('任务开始','用户要求 + 可用 Skills 目录'),('选择能力','模型选择演示文稿 Skill'),('加载流程','Harness 加入核心指令'),('执行任务','按需读取参考资料，执行工具'),('检查产物','加入页面预览与检查结果')]
    for i,(stage,detail) in enumerate(rows):
        y=25+i*95
        f.box(25,y,175,60,stage)
        f.box(255,y,440,60,detail,fill='#ffffff')
        f.path([(200,y+30),(255,y+30)])
        if i<4:f.path([(475,y+60),(475,y+95)])
    f.text(360,520,'新信息随任务进入历史，为下一步决策提供依据。',size=16)
    f.save('fig2-12.svg')


def skills_cache():
    f=Figure('Skills 加载与缓存复用','前三轮请求用等宽块示意内容追加，块宽不表示 token 数量。',425)
    names=['规则与目录','已有任务','核心流程','参考资料']
    for r,(title,count,cached) in enumerate([('任务开始',2,0),('加载 Skill',3,2),('读取细则',4,3)]):
        y=45+r*95
        f.text(78,y+36,title,bold=True)
        for c in range(count):f.box(165+c*132,y,122,62,names[c],fill=MID if c<cached else '#ffffff')
    f.rect(110,340,24,24,fill=MID);f.text(145,359,'复用已有前缀',size=16,anchor='start')
    f.rect(385,340,24,24,fill='#ffffff');f.text(420,359,'首次处理新增内容',size=16,anchor='start')
    f.text(360,407,'框宽仅用于示意顺序；后续请求继续使用已经加载的内容。',size=16)
    f.save('fig2-13.svg')


def status_architecture():
    f=Figure('Agent 状态栏架构','可信记录形成状态摘要，模型据此决策，执行层用真实计数检查调用。',570)
    for x,t in [(25,'通话与工具记录'),(260,'任务进度'),(495,'当前环境')]:
        f.box(x,30,200,60,t)
        f.path([(x+100,90),(x+100,120),(360,120)],arrow=False)
    f.path([(360,120),(360,155)])
    f.box(100,160,520,100,'Harness 汇总最新状态','三次通话已完成；退款待到账核实',fill=MID)
    f.path([(230,260),(170,310),(170,345)])
    f.path([(490,260),(550,310),(550,345)])
    f.box(25,350,285,100,'模型选择下一步','等待、查询进展或联系用户')
    f.box(410,350,285,100,'执行层检查','按身份、次数与业务规则校验')
    f.path([(310,400),(410,400)])
    f.text(360,382,'请求',size=16)
    f.text(360,497,'状态摘要提供决策依据；执行检查落实操作限制。',size=16)
    f.text(360,537,'新执行结果进入记录，再更新下一轮状态。',size=16)
    f.save('fig2-14.svg')


def status_context():
    f=Figure('最新状态的上下文位置','规则、相关历史和最新状态组成一次请求，末尾状态由 Harness 生成。',560)
    f.box(55,25,610,70,'稳定规则与工具定义',fill=MID)
    f.box(55,120,610,110,'任务历史','用户要求、模型请求、通话与搜索结果')
    f.box(55,255,610,120,'Harness 生成的最新状态','已拨打三次，达到上限\n退款仍在处理；下一步核实到账',fill='#ffffff')
    f.path([(360,375),(360,425)])
    f.box(175,430,370,65,'模型基于本轮上下文继续决策')
    f.text(360,537,'状态注明来源与更新时间，随任务推进更新。',size=16)
    f.save('fig2-15.svg')

def compression_boundary():
    f=Figure('上下文压缩与缓存边界','稳定前缀可继续复用，旧历史形成摘要，从改动处开始重新处理。原始记录单独归档。',580)
    f.text(180,32,'压缩前',bold=True)
    f.text(540,32,'压缩后',bold=True)
    for x in [30,390]: f.box(x,60,300,65,'稳定规则与工具定义',fill=MID)
    f.box(30,155,300,210,'已完成阶段的历史','搜索页面、工具结果\n中间判断与处理记录')
    f.box(390,155,300,105,'阶段摘要','结论、理由、来源与待办')
    f.path([(330,205),(390,205)])
    f.box(30,395,300,75,'当前步骤所需细节',fill='#ffffff')
    f.box(390,290,300,75,'当前步骤所需细节',fill='#ffffff')
    f.path([(330,430),(360,430),(360,330),(390,330)])
    f.box(390,405,300,65,'上下文外：原始记录归档',fill='#ffffff')
    f.path([(330,330),(345,330),(345,490),(540,490),(540,470)])
    f.text(540,390,'按来源回查原文',size=16)
    f.text(360,529,'灰色前缀保持一致，可按缓存条件复用。',size=16)
    f.text(360,558,'摘要改变历史，从首次改动位置开始重新处理。',size=16)
    f.save('fig2-16.svg')


def compression_strategies():
    f=Figure('六种压缩策略的处理流程','六行分别呈现无压缩、逐页、合并、任务感知、带引用和窗口化的处理过程。',650)
    rows=[('无压缩','各页原文','完整保留'),
          ('逐页摘要','逐页分别提炼','各页摘要'),
          ('合并摘要','汇集页面后提炼','综合摘要'),
          ('任务感知','结合问题与进展','面向任务的摘要'),
          ('带引用','保留事实与来源关联','摘要 + 来源'),
          ('窗口化','达到阈值后批量整理','原文 → 历史摘要')]
    for i,(name,operation,result) in enumerate(rows):
        y=30+i*93
        f.box(20,y,140,63,name,fill=MID)
        f.box(200,y,260,63,operation,fill='#ffffff')
        f.box(500,y,200,63,result)
        f.path([(160,y+31),(200,y+31)])
        f.path([(460,y+31),(500,y+31)])
    f.text(360,614,'材料组织、摘要目标、来源追溯与整理时机可以组合。',size=16)
    f.save('fig2-17.svg')


if __name__ == '__main__':
    composition()
    single()
    interaction()
    growth()
    local()
    attention()
    measured_attention()
    prefix_cache()
    template_message()
    template_conversion()
    skills_discovery()
    skills_history()
    skills_cache()
    status_architecture()
    status_context()
    compression_boundary()
    compression_strategies()
