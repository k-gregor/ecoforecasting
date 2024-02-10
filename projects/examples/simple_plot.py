import numpy as np
from bokeh.plotting import figure, show

# prepare some data
x = np.arange(0, 20, 0.2)
y = x + [ np.random.normal(0, 1) for i in range(0, 100)]
y *= 0.2
z  = x + [ np.random.normal(0, 1) for i in range(0, 100)]
z *= 0.05


# create a new plot with a title and axis labels
p = figure(title="Sucess of our company",
           x_axis_label='time',
           y_axis_label='sucess in billion euros')


# add a line renderer with legend and line thickness to the plot
p.line(x, y, legend_label="Philli + Konni + etc", line_width=2, color="blue")
p.line(x, z, legend_label="Climate analytics", line_width=2, color="red")

# show the results
show(p)