"""Diseño editorial de la figura de salario mínimo."""
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.ticker import FuncFormatter
def dibujar(root,years,values,rates,proposal):
    navy,orange,gray='#243B53','#C76A32','#52616F'
    plt.rcParams.update({'font.family':'DejaVu Sans','font.size':10,'pdf.fonttype':42})
    fig,axs=plt.subplots(2,1,figsize=(7.2,5.6),sharex=True)
    fig.subplots_adjust(left=.09,right=.96,top=.89,bottom=.09,hspace=.48)
    fig.legend(handles=[Line2D([0],[0],color=navy,lw=2,label='Histórico'),
        Line2D([0],[0],color=orange,lw=2,ls='--',marker='o',label='Escenario 2027: 7%')],
        loc='upper center',ncol=2,frameon=False,fontsize=10)
    for ax,data,end,title in zip(axs,[rates,values/1e6],[7,proposal/1e6],
        ['A. Aumento nominal anual (%)','B. Salario básico mensual (millones de pesos)']):
        ax.set_title(title,loc='left',color=navy,weight='bold',fontsize=10.5,pad=10)
        ax.set_axisbelow(True); ax.grid(axis='y',color='#E4E9ED',lw=.6)
        for side in ['top','right','left']:ax.spines[side].set_visible(False)
        ax.spines['bottom'].set_color('#BFC9D2')
        ax.tick_params(length=0,labelsize=9,labelcolor=gray)
        ax.axvspan(2026.5,2027.7,color=orange,alpha=.08,lw=0)
        ax.plot(years,data,color=navy,lw=2,marker='o',mfc='white',ms=4)
        ax.plot([2026,2027],[data[-1],end],color=orange,lw=2,ls='--')
        ax.scatter([2027],[end],s=40,color=orange,zorder=5)
        ax.set_xlim(2013.6,2027.7)
        ax.set_xticks([2014,2016,2018,2020,2022,2024,2026,2027])
        ax.yaxis.set_major_formatter(FuncFormatter(lambda v,_:f'{v:g}'.replace('.',',')))
    axs[0].tick_params(labelbottom=True)
    axs[0].set_ylim(0,29);axs[0].set_yticks([0,10,20])
    for year in [2014,2016,2018,2020,2021,2022,2023,2024,2025,2026]:
        val=rates[list(years).index(year)]
        axs[0].annotate(f'{val:.1f}'.replace('.',','),(year,val),xytext=(0,8),
            textcoords='offset points',ha='center',fontsize=9,color=navy)
    axs[0].annotate('7,0%',(2027,7),xytext=(-2,10),textcoords='offset points',
        ha='center',color=orange,weight='bold',fontsize=11)
    axs[1].set_ylim(.4,2.22);axs[1].set_yticks([.5,1,1.5,2])
    for year in [2014,2021,2023,2026]:
        val=values[list(years).index(year)]
        axs[1].annotate('$'+f'{val:,.0f}'.replace(',','.'),(year,val/1e6),
            xytext=(0,10 if year!=2026 else -19),textcoords='offset points',
            ha='left' if year==2014 else 'center',fontsize=9,color=navy)
    axs[1].annotate('$1.873.468',(2027,proposal/1e6),xytext=(-2,13),
        textcoords='offset points',ha='right',fontsize=11,weight='bold',color=orange)
    for ext in ['pdf','png']:
        fig.savefig(root/f'Paper/figures/serie_salario_minimo_2027_7pct.{ext}',dpi=300)
    plt.close(fig)

