from os import access
import pandas as pd
import numpy as np
from pandas.core.base import SpecificationError
df = pd.read_csv("final.csv")
C = df["vote_average"].mean()
m = df["vote_count"].quanitle(0.9)
q_movies = df.copy().loc[df["vote_count"] >= m]
def weighted_rating(x, m = m, C = C):
    v = x["vote_count"]
    R = x["vote_average"]
    return(v/(v+m)*R) + (m/(m+v)*C)
q_movies["score"] = q_movies.apply(weighted_rating, access = 1)
q_movies = q_movies.sort_values("score", ascending=False)
output = q_movies[["title", "poster_link", "release_date", "runtime", "vote_count", "vote_average", "overview"]].head(20).values.tolist()