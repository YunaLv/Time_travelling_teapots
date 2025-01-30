import json
import csv
import os

#to access every file inside the "people folder"
file_list_every_letter = os.listdir("C:/Users/Yunam/OneDrive/Documents/Spring 25/Python actu/GitHub/People")

#making an empty dictionary to input the cleaned data
musicians = {}
punkgenres = ["punk", "post-hardcore", "garage rock","noise rock"]
#loading the file for each letter 
for file_name in file_list_every_letter:
    with open(f"C:/Users/Yunam/OneDrive/Documents/Spring 25/Python actu/GitHub/People/A_people.json", encoding='utf-8') as file:
        letter_people = json.load(file) 
    #filtering for people listed in the dictionary who have the activestartyear listed
    for person in letter_people:
        if "ontology/activeYearsStartYear" and "ontology/activeYearsEndYear" in person:
            #filtering for person who have occupation listed and keeping those who are listed as "musical artist"
            if 'http://www.w3.org/1999/02/22-rdf-syntax-ns#type_label' in person and any(job == "musical artist" for job in person['http://www.w3.org/1999/02/22-rdf-syntax-ns#type_label']):
                #filtering for people who have the genre_label listed
                if "ontology/genre_label" in person:
                    #adding all relevant information to the dictionary
                    name= person['title']
                    genres= person["ontology/genre_label"]
                    startyear = person["ontology/activeYearsStartYear"]
                    endyear = person["ontology/activeYearsEndYear"]
                    if type(genres) is not list:
                        genres = [genres]
                    if type(startyear) is list:
                        startyear=startyear[0]
                    
                    startyear= int(startyear)

                    if startyear>1900:
                        if endyear == startyear:
                            endyear=2015
                    
                        YearRange=range(startyear, int(endyear)+1)
                        ActiveYears=[] 

                        for year in YearRange:
                            ActiveYears.append(year)                       



                        if len(ActiveYears) > 50:
                            ActiveYears = "NOPE"


                        clean_genres = []
                        genre_group = []
                        
                        for genre in genres:
                            genre = genre.lower()
                            clean_genres.append(genre.replace("-", "_"))
                            if "punk" in genre or genre in punkgenres: 
                                genre_group.append("Punk")
                            elif "rock" in genre:
                                genre_group.append("Rock")
                            elif "metal" in genre: 
                                genre_group.append("Metal")
                            elif "blues" in genre:
                                genre_group.append("Blues")
                        genre_group = set(genre_group)
                        musicians[name] ={
                        'name': name,
                        'genre': clean_genres,
                        'genre_group': list(genre_group),
                        'end_year': endyear,
                        'start_year':startyear,
                        'active_year': ActiveYears
                        }
                    
print(musicians)
                    
#outputting data to above dictionary
#with open('clean_data.json', 'w') as file:
 #   json.dump(musicians, file, indent=4)