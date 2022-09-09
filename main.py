import numpy as np
import matplotlib.pyplot as plt

def x_axis_func(x, pos):
   return f'-{x}'

plt.style.use('fivethirtyeight')

fig, ax = plt.subplots()
ax.plot(np.arange(10), linewidth=5.0, alpha=0.25)
ax.set_title('hello')
ax.set_xlabel('a number')
ax.set_ylabel('another number')
ax.grid(True)
plt.show()

fig, ax = plt.subplots()
ax.plot(np.arange(10), linewidth=5.0, alpha=0.25)
ax.set_title('hello')
ax.set_xlabel('a number')
ax.set_ylabel('another number')
ax.grid(True)
x = 5
ax.text(2,4,f'number {x}')
plt.show()


# Fixing random state for reproducibility
np.random.seed(19680801)

fig, ax = plt.subplots()
ax.plot(100*np.random.rand(20))
labels = ax.get_xticklabels()
plt.setp(labels, rotation=45)
ax.axvline(5, ls='--', color='r')
ax.axhline(5, ls='--', color='r')


## Use automatic StrMethodFormatter
ax.yaxis.set_major_formatter('${x:1.2f}')
#
ax.yaxis.set_tick_params(which='major', labelcolor='green',
                         labelleft=False, labelright=True)
ax.grid(True)
ax.xaxis.set_major_formatter(x_axis_func)
plt.show()


# create an array of 5000 normally distributed numbers
x = np.random.randn(5000)

#plot the PDF of x
plt.hist(x, bins=100, density=True, histtype='stepfilled', alpha=0.75)

