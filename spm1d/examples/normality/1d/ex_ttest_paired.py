
import numpy as np
from matplotlib import pyplot
import spm1d




#(0) Load dataset:
dataset      = spm1d.data.uv1d.t2.PlantarArchAngle()
yA,yB        = dataset.get_data()  #normal and fast walking



#(1) Conduct normality test:
np.random.seed(0)
alpha      = 0.05
spmi       = spm1d.stats.normality.ttest_paired(yA, yB).inference(alpha)
print spmi



#(2) Plot
pyplot.close('all')
pyplot.figure(figsize=(14,4))
pyplot.get_current_fig_manager().window.move(0, 0)
ax = pyplot.subplot(131);  ax.plot(yA.T, 'k', lw=0.5);   ax.plot(yB.T, 'r', lw=0.5);   ax.set_title('Data')
ax = pyplot.subplot(132);  ax.plot(spmi.residuals.T, 'k', lw=0.5);   ax.set_title('Residuals')
ax = pyplot.subplot(133);  spmi.plot(ax=ax);   spmi.plot_threshold_label(ax=ax); ax.set_title('Normality test')
pyplot.show()