import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1,8])
ypoints = np.array([3,10])

plt.plot(xpoints,ypoints,'o')
plt.show()

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1,2,6,8])
ypoints = np.array([3,8,1,10])

plt.plot(xpoints,ypoints, )
plt.show()

import matplotlib.pyplot as plt
import numpy as np


ypoints = np.array([3,8,1,10])

plt.plot(ypoints, marker = 'o', ms = 20, mec='r')
plt.show()


import matplotlib.pyplot as plt
import numpy as np


ypoints = np.array([3,8,1,10])

plt.plot(ypoints, linetyle = 'dotted')
plt.show()