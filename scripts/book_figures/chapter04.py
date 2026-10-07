"""Grayscale teaching figures for Chapter 4."""
from style import Figure, MID


def mcp_flow():
    f=Figure('MCP 工具发现与调用流程','宿主中的客户端取得工具定义，模型提出调用，经宿主检查后由服务器执行，再将结果送回模型。',740)
    for x,w,title in [(20,160,'模型'),(245,230,'宿主／客户端'),(535,165,'MCP 服务器')]:
        f.box(x,25,w,65,title,fill=MID)
        f.path([(x+w/2,90),(x+w/2,680)],arrow=False,dashed=True)
    def msg(a,b,y,label):
        f.path([(a,y),(b,y)])
        f.text((a+b)/2,y-12,label,size=16)
    msg(360,617,150,'取得可用工具定义')
    msg(617,360,215,'返回定义')
    msg(360,100,280,'提供当前所需定义')
    msg(100,360,345,'提出调用与参数')
    f.box(255,375,210,60,'检查参数与权限')
    msg(360,617,475,'发送工具调用')
    f.box(540,500,155,55,'检查并执行')
    msg(617,360,590,'返回结果与状态')
    msg(360,100,650,'组织结果进入上下文')
    f.text(360,714,'宿主管理模型交互；客户端承担协议通信。',size=16)
    f.save('fig4-1.svg')


if __name__ == '__main__':
    mcp_flow()
