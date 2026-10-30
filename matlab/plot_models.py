"""Original AI instructional figures; calculated models, not experimental data.

Reproduces the statics lesson diagrams. Requires NumPy and Matplotlib.
Example: python plot_models.py --output-dir /path/to/chosen/writable/folder
No MATLAB execution is implied. Human scientific review remains pending.
"""
from pathlib import Path
import argparse, tempfile, os
parser=argparse.ArgumentParser(description=__doc__)
parser.add_argument('--output-dir',type=Path,required=True)
args=parser.parse_args()
DEST=args.output_dir.resolve();DEST.mkdir(parents=True,exist_ok=True)
W=DEST
cache=tempfile.TemporaryDirectory(prefix='statics-plot-cache-')
os.environ['MPLCONFIGDIR']=str(Path(cache.name)/'matplotlib')
os.environ['XDG_CACHE_HOME']=str(Path(cache.name)/'cache')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Arc

# All exports go to the explicitly chosen output directory.
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':12,'svg.fonttype':'none','axes.spines.top':False,'axes.spines.right':False})
def arrow(ax,p,q,label,offset=(0,0),color='#b44530'):
    ax.annotate('',xy=q,xytext=p,arrowprops=dict(arrowstyle='->',lw=2.3,color=color))
    ax.text(q[0]+offset[0],q[1]+offset[1],label,color=color,ha='center',va='center')
def save(fig,name):
    svg_path=DEST/(name+'.svg')
    fig.savefig(svg_path,bbox_inches='tight')
    # Matplotlib inserts trailing spaces in SVG path data; keep exports Git-clean.
    svg_path.write_text('\n'.join(line.rstrip() for line in svg_path.read_text().splitlines())+'\n')
    fig.savefig(W/(name+'.png'),dpi=150,bbox_inches='tight');plt.close(fig)

fig,ax=plt.subplots(figsize=(7,5));a=np.deg2rad(30);t=np.array([np.cos(a),np.sin(a)]);n=np.array([-np.sin(a),np.cos(a)])
ax.plot([-.5,3],[-.5*np.tan(a),3*np.tan(a)],color='#52636d',lw=3)
c=np.array([1.1,1.1*np.tan(a)])+.18*n
ax.scatter(*c,s=350,color='#c7dce7',edgecolor='#233744',zorder=3)
arrow(ax,c,c+np.array([1.1,0]),'$P$',(.12,.12))
arrow(ax,c,c+np.array([0,-1.3]),'$Mg$',(.22,-.04))
arrow(ax,c,c+.95*n,'$N$',(-.12,.15))
arrow(ax,c,c+.95*t,'$f$ (signed)',(.3,.08),color='#176e68')
ax.plot([0,.9],[0,0],ls='--',color='gray');ax.add_patch(Arc((0,0),1.1,1.1,theta1=0,theta2=30));ax.text(.62,.1,r'$\theta$')
ax.text(-.4,2.1,'Positive tangent: uphill\nPositive normal: away from plane',fontsize=10)
ax.set(xlim=(-.7,3.2),ylim=(-1,2.6),aspect='equal');ax.axis('off');save(fig,'statics-incline')

fig,ax=plt.subplots(figsize=(7,5));th=np.linspace(0,89.5,400)*np.pi/180;p=np.linspace(0,2,401);TT,PP=np.meshgrid(th,p)
ff=np.sin(TT)-PP*np.cos(TT);nn=np.cos(TT)+PP*np.sin(TT);ok=np.abs(ff)<=.4*nn
ax.contourf(TT*180/np.pi,PP,ok,levels=[-.5,.5,1.5],colors=['#f7f0eb','#a3cec6'])
ax.contour(TT*180/np.pi,PP,np.abs(ff)-.4*nn,levels=[0],colors=['#176e68'],linewidths=1.5)
ax.plot(th*180/np.pi,np.tan(th),'--',color='#51457d',label='$f=0$')
ax.set(xlim=(0,89),ylim=(0,2),xlabel=r'Inclination $\theta$ (degrees)',ylabel=r'Horizontal push $P/(Mg)$',title=r'Force/friction feasibility, $\mu_s=0.4$');ax.legend();ax.text(8,1.8,'Shaded: admissible\nfor the force-only model',fontsize=10)
save(fig,'statics-feasibility')

fig,ax=plt.subplots(figsize=(7,5));q=np.linspace(-.55,.55,100);ax.plot(np.cos(q),np.sin(q),lw=6,color='#89a9b7');d=.36
lo=np.array([np.cos(d),-np.sin(d)]);hi=np.array([np.cos(d),np.sin(d)])
arrow(ax,lo,lo+.65*np.array([-np.sin(d),-np.cos(d)]),'$T$',(-.18,.02))
arrow(ax,hi,hi+.8*np.array([-np.sin(d),np.cos(d)]),'$T+dT$',(-.15,.06))
arrow(ax,(1,0),(1.65,0),'$dN$',(.12,.03))
arrow(ax,(1.06,0),(1.06,-.37),'$df$',(.2,.02),color='#176e68')
ax.plot([0,lo[0]],[0,lo[1]],':',color='gray');ax.plot([0,hi[0]],[0,hi[1]],':',color='gray');ax.add_patch(Arc((0,0),.6,.6,theta1=-d*180/np.pi,theta2=d*180/np.pi));ax.text(.34,0,r'$d\phi$',va='center')
ax.text(.05,-1.5,'Schematic enlarged element; use the differential limit.\nFriction shown for tension increasing upward along the arc.',fontsize=10)
ax.set(xlim=(-.1,2.05),ylim=(-1.65,1.25),aspect='equal');ax.axis('off');save(fig,'statics-capstan-segment')

fig,ax=plt.subplots(figsize=(7,3.4));ax.plot([0,2],[0,0],color='#52636d',lw=9)
arrow(ax,(0,0),(0,1),'$F$',(-.13,.12));arrow(ax,(2,0),(2,-1),'$F$',(.15,-.08))
ax.annotate('',xy=(2,.5),xytext=(0,.5),arrowprops=dict(arrowstyle='<->',color='#176e68'));ax.text(1,.62,'separation $d$',ha='center');ax.text(1,-1.6,'Resultant force = 0; clockwise torque magnitude = $Fd$',ha='center',fontsize=11)
ax.set(xlim=(-.4,2.5),ylim=(-1.85,1.4),aspect='equal');ax.axis('off');save(fig,'statics-couple')

fig,ax=plt.subplots(figsize=(6,6));ax.plot([-.6,3.6],[0,0],color='#88969e',lw=3);ax.plot([3,3],[0,4.7],color='#88969e',lw=3);ax.plot([0,3],[0,4],color='#52636d',lw=6)
arrow(ax,(3,4),(1.8,4),'$N_w$',(-.1,.2));arrow(ax,(0,0),(0,1.5),'$N_f$',(-.3,0));arrow(ax,(0,0),(1.2,0),'$f$',(.1,-.3),color='#176e68');arrow(ax,(1.5,2),(1.5,.8),'$mg$',(.35,-.02))
ax.add_patch(Arc((0,0),1.4,1.4,theta1=0,theta2=np.degrees(np.arctan2(4,3))));ax.text(.73,.35,r'$\theta$');ax.text(1.2,2.9,'$L$',rotation=53)
ax.set(xlim=(-.7,3.7),ylim=(-.6,4.7),aspect='equal');ax.axis('off');save(fig,'statics-ladder')
print('Created 5 original SVG figures and PNG previews in', DEST)
