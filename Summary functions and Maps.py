#SUMMARY FUNCTIONS AND MAPS

import pandas as pd
pd.set_option("display.max_rows", 5)
reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)

from learntools.core import binder; binder.bind(globals())
from learntools.pandas.summary_functions_and_maps import *
print("Setup complete.")

reviews.head()

median_points = reviews.points.median()
countries = reviews.country.unique()
reviews_per_country = reviews.country.value_counts()

centered_price = reviews.price - reviews.price.mean()

bargain_idx = (reviews.points / reviews.price).idxmax()
bargain_wine = reviews.loc[bargain_idx, 'title']

t = reviews.description.map(lambda desc: "tropical" in desc).sum()
f = reviews.description.map(lambda desc: "fruity" in desc).sum()
descriptor_counts = pd.Series([t,f], index=['tropical', 'fruity'])
