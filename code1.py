import pandas as pd 
import os 

# Creating a data :

data = {"Name" : ["Yashraj" , "Sahil" , "Dhruv" , "Arpit"],
        "Age" : [18,19,20,21],
        "State" : ["Rajasthan"  , "Haryana" , "Harayana" , "Biahr"]
}

df = pd.DataFrame(data)

# adding a data :
new_row_loc = {"Name" : "Alka" , "Age" : 19 , "State" : "Rajasthan" }
df.loc[len(df.index)] = new_row_loc

#adding another data :
new_row_loc2 = {"Name" : "Aish" , "Age" : 20 , "State" : "Rajasthan"}
df.loc[len(df.index)] = new_row_loc2

data_dir = "data"
os.makedirs(data_dir , exist_ok = True)

file_path = os.path.join(data_dir , 'sample_data.csv')

df.to_csv(file_path , index = False)

print("Csv file save to path {file_path} ")