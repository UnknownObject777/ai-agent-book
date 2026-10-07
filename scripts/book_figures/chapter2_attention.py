"""Plot chapter 2 attention evidence in grayscale; never synthesize matrix values."""
from pathlib import Path
import json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
from matplotlib.font_manager import FontProperties

ROOT = Path(__file__).resolve().parents[2]
RUN = ROOT / 'chapter2/attention_visualization/runs/exp2-2-qwen3-0.6b-20260730-v3'
FONT = FontProperties(fname='/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc')
plt.rcParams.update({'font.family': FONT.get_name(), 'font.size': 9, 'axes.unicode_minus': False})

def main():
    matrices = np.load(RUN / 'attention_matrices.npz')
    evidence = json.loads((RUN / 'evidence.json').read_text())
    thinking = min(evidence['generated']['regions']['thinking'])
    answer = min(evidence['generated']['regions']['answer'])
    fig, axes = plt.subplots(3, 2, figsize=(5.9, 8.2))
    fig.subplots_adjust(left=.10, right=.96, top=.94, bottom=.13, wspace=.38, hspace=.43)
    cmap = plt.get_cmap('Greys').copy()
    cmap.set_bad('white')
    for row, layer in enumerate([0, 13, 27]):
        for col, kind in enumerate(['simple', 'generated']):
            ax = axes[row,col]
            data = matrices[f'{kind}_layer_{layer}']
            im = ax.imshow(np.ma.masked_less_equal(data, 0), cmap=cmap,
                           norm=LogNorm(vmin=1e-4, vmax=1), interpolation='nearest', rasterized=True)
            ax.set_title(f'{"短句" if col == 0 else "推理与回答"} · 第 {layer} 层', fontsize=10)
            ax.set_xlabel('Key 位置', fontsize=9)
            ax.set_ylabel('Query 位置', fontsize=9)
            ticks = [0,4,8] if col == 0 else [0,200,400,579]
            ax.set_xticks(ticks);ax.set_yticks(ticks)
            ax.tick_params(labelsize=9)
            if col:
                ax.text(.98,.94, '输入：0–47\n推理：48–565\n回答：566–579', transform=ax.transAxes, ha='right', va='top', fontsize=9, bbox={'facecolor':'white','edgecolor':'none','pad':1.5})
                for boundary, style in [(thinking, '--'), (answer, ':')]:
                    ax.axhline(boundary-.5, color='#777777', linestyle=style, linewidth=.65)
                    ax.axvline(boundary-.5, color='#777777', linestyle=style, linewidth=.65)
    cax=fig.add_axes([.20,.055,.60,.016])
    cb=fig.colorbar(im,cax=cax,orientation='horizontal',ticks=[1e-4,1e-3,1e-2,1e-1,1])
    cb.set_ticklabels(['0.0001','0.001','0.01','0.1','1'])
    cb.ax.minorticks_off()
    cb.set_label('注意力权重（对数灰度）',fontsize=9)
    fig.savefig(ROOT/'book/images/fig2-7.png',dpi=350,facecolor='white')
    plt.close(fig)

if __name__ == '__main__':
    main()
