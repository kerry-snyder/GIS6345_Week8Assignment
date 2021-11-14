#Stackplots
#Data obtained from https://sciencebase.usgs.gov/nabat/#/home 

import numpy as np
import matplotlib.pyplot as plt

#Data for bat Mobile Acoustic Regords
month = ['Jan', 'Feb', 'March', 'April', 'May', 'June', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
organization = {
    'Midwest Bat Hub': [100900,162384,204417,204520,247605,252961,252961,339905,339905,352268,352520,355015],
    'Iowa Department of Natural Resources': [1025,62458,64016,64016,64016,64016,64016,64016,64016,66175,66220,66220],
    'Wisconsin Department of Natural Resources': [0,0,25106,25106,25106,25106,25106,25106,25106,25106,25106,25106],
    'Illinois Bat Conservation Program': [0,0,6312,6312,6312,6312,6312,6312,6312,6312,6340,6340],
    'Georgian Bay Biosphere Reserve': [1330,1330,1330,1330,1330,1330,1330,1330,1330,1330,1330,1330],
}


fig, ax = plt.subplots()
ax.stackplot(month, organization.values(),
             labels= organization.keys())
ax.legend(loc='upper left')
ax.set_title('Bat Mobile Acoustic Records')
ax.set_xlabel('Month (2020)')
ax.set_ylabel('Number of records')
plt.tight_layout()
