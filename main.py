import matplotlib.pyplot as plt
import pandas as pd

df = pd.DataFrame([[1,2,3],[7,0,3],[1,2,2]],columns=['col1','col2','col3'])

df.plot()

plt.savefig('myfile.pdf')
