import pandas as pd
import os

ho,ho2,folders = next(os.walk("./rating_data")) #reading all the rating folders
movies = pd.read_csv("./movies.csv") #importing the dataset
movies.drop("genres",axis = 1,inplace = True)
movie = input("Enter the movie name")
no_of_recommended_movies = int(input("Enter the no: of movies you want to get "))
li = []
for i in folders:
    df = pd.read_csv("./rating_data/"+i).drop("Unnamed: 0",axis = 1)
    df = pd.merge(df,movies,on="movieId")
    movie_mat = df.pivot_table(values = "rating",index = "userId",columns = "title")
    selected_movie_rating=movie_mat[movie]
    similar_movies = movie_mat.corrwith(selected_movie_rating) #finding the correlation
    data = pd.DataFrame(similar_movies[similar_movies>0.9].sort_values(ascending = False).head(2)) #filtering the dataframe
    data.dropna(inplace = True)
    data.reset_index(inplace = True)
    data.drop(0,axis = 1,inplace = True )
    li.append(data.loc[0]["title"])
    li.append(data.loc[1]["title"])
    if(len(li)==no_of_recommended_movies): #limiting the results accoring to the users need
        for i in li:
            print(i)
        exit()
