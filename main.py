#%%
import pandas as pd

#%% We'll also import seaborn, a Python graphing library
import warnings # current version of seaborn generates a bunch of warnings that we'll ignore
warnings.filterwarnings("ignore")
import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="white", color_codes=True)

#%% Next, we'll load the Iris flower dataset, which is in the "../input/" directory
iris = pd.read_csv("./data/iris_csv.csv") # the iris dataset is now a Pandas DataFrame

#%%
iris.head()

#%%
iris["class"].value_counts()

#%%
iris.plot(kind="scatter", x="sepallength", y="sepalwidth")

#%%
sns.jointplot(x="sepallength", y="sepalwidth", data=iris, size=5)