
# coding: utf-8

# In[ ]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
from matplotlib.dates import DayLocator
from matplotlib.dates import MonthLocator
from scipy import signal
from datetime import date

data=pd.read_excel(r'G:\201705python\numpy&pandas\eg2\eg2.xlsx')
c=data.close
d=data.日期

y=signal.detrend(c) #去掉股票的线性趋势


alldays=DayLocator()
months=MonthLocator()
month_formatter=MonthLocator('%b %y')

plt.plot(d,c,'m-',d,c-y,'r-')
ax.xaxis.set_minor_locator(alldays)
ax.xaxis.set_major_locator(months)
ax.xaxis.set_major_formatter(month_formatter)

fig.autofmt_xdate()
plt.show()


# In[ ]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
from matplotlib.dates import DayLocator
from matplotlib.dates import MonthLocator
from scipy import signal
from datetime import date

data=pd.read_excel(r'G:\201705python\numpy&pandas\eg2\eg2.xlsx')
c=data.close
d=data.日期

y=signal.detrend(c) #去掉股票的线性趋势

plt.plot(d,c,'m-',d,c-y,'r-')
fig.autofmt_xdate()
plt.show()


# In[ ]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter,DayLocator,MonthLocator
from scipy import signal,fftpack
from datetime import date

amps=np.abs(fftpack.fftshift(fftpack.rfft(y)))
amps[amps<.1*amps.max()]=0
plt.plot(d,y,'o',label='detrended')
plt.plot(d,-fftpack.irfft(fftpack.ifftshift(amps)),label='fitlered')
fig.autofmt_xdate()
plt.legend()
plt.show()

