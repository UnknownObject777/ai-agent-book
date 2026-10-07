# 黑白灰度插图

这里保存中文书稿重绘图的源代码。生成器使用 Python 标准库输出 SVG，图片不依赖在线服务。正文图题留在 Markdown 中，SVG 的 `title` 和 `desc` 提供无障碍说明。

```bash
python scripts/book_figures/chapter01.py
rsvg-convert -b white -w 1100 book/images/fig1-1.svg -o /tmp/fig1-1.png
```

默认画布宽 720 单位、印刷宽 150 mm，正文标签使用 18 单位（缩放后约 10.6 pt），最小标签 16 单位（约 9.4 pt）。这是绘制基准；最终字号仍以实际 PDF 为准。

生成后必须渲染查看：节点和标签不能相撞，箭头必须指向正确对象，包含框不能暗示错误归属。源文件检查不能替代图文和版式验收。全书进度见 `docs/editorial-revision.md` 和 `docs/figure-inventory.json`。

第 2 章运行 `python scripts/book_figures/chapter02.py`。实测图2-7 使用 NumPy 读取配套固定矩阵，完整保留数据并按统一线性灰度输出 SVG；其余图使用标准库。

第 3 章运行 `python scripts/book_figures/chapter03.py`，目前已生成图3-1～3-15，出版版式仍需结合最终书页检查。

第 4 章运行 `python scripts/book_figures/chapter04.py`，目前生成图4-1。
