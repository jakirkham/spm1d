
import numpy as np
from matplotlib import pyplot
import spm1d



#(0) Load a dataset containing a circular field:
dataset  = spm1d.data.uv1d.anova1.Weather()
Y,A      = dataset.get_data()
yA,yB    = Y[A==0], Y[A==2]  #Atlantic and Contintental regions



#(1) Conduct non-parametric test:
np.random.seed(0)
alpha      = 0.05
two_tailed = False
circular   = True
snpm       = spm1d.stats.nonparam.ttest2(yA, yB)
snpmi      = snpm.inference(alpha, two_tailed=two_tailed, iterations=1000, circular=circular)
print snpmi
print snpmi.clusters



#(2) Compare with parametric result:
spm        = spm1d.stats.ttest2(yA, yB)
spmi       = spm.inference(alpha, two_tailed=two_tailed, circular=circular)
print spmi
print spmi.clusters



#(3) Plot
pyplot.close('all')
pyplot.figure(figsize=(12,4))
pyplot.get_current_fig_manager().window.move(0, 0)
ax0 = pyplot.subplot(121)
ax1 = pyplot.subplot(122)
for ax,zi in zip([ax0,ax1], [spmi,snpmi]):
	zi.plot(ax=ax)
	zi.plot_threshold_label(ax=ax, fontsize=8)
	zi.plot_p_values(ax=ax, size=10)
pyplot.show()

