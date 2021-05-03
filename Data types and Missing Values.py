#DATA TYPES AND MISSING VALUES

import pandas as pd

reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)

from learntools.core import binder; binder.bind(globals())
from learntools.pandas.data_types_and_missing_data import *

dtype = reviews.points.dtype
point_strings = reviews.points.astype('str')
n_missing_prices = pd.isnull(reviews.price).sum()
r = reviews.region_1.fillna("Unknown")
reviews_per_region = r.value_counts().sort_values(ascending=False)
