import pandas as pd
import warnings
warnings.filterwarnings("ignore")

def wrangle_df1(filepath):
    
    df1=pd.read_excel(filepath)
    
    # removing the unnecessary characters and changing the column data type
    df1.price_usd=df1.price_usd.str.replace("$", "").str.replace(",", "").astype(float)
    
    # dropping unnamed column which is not necessary.
    df1.drop(columns="Unnamed: 0", inplace=True)
    
    return df1


def wrangle_df2(filepath):
    
    df2=pd.read_excel(filepath)
    
    # converting 'price_mxn' columns from mxn to usd currency as per other dataframe and assging the result to a new column.
    df2["price_usd"]=df2.price_mxn/19
    
    #converting mxn currency to to usd currency.
    df2.drop(columns=["price_mxn", "Unnamed: 0"], inplace=True)
    
    return df2

def wrangle_df3(filepath):
    
    df3=pd.read_excel(filepath)
    
    # splitting lat-lon to get 2 columns.
    df3[["lat","lon"]]=df3["lat-lon"].str.split(",", expand=True)
    
    # spliting 'place_with_parent_names' to extract the district column.
    df3["state"]=df3.place_with_parent_names.str.split("|", expand=True)[2]
    
    # dropping duplicate columns
    df3.drop(columns=["lat-lon","place_with_parent_names","Unnamed: 0"], inplace=True)
    
    return df3    

def main():
        
    frames=[wrangle_df1("data\mexico-real-estate-1.xlsx"), wrangle_df2("data\mexico-real-estate-2.xlsx"), wrangle_df3("data\mexico-real-estate-3.xlsx")]
    
    pd.set_option("display.max_columns", None)
    
    df=pd.concat(frames) 

    df.dropna(inplace=True)     
           
    return df.to_csv("data\Mexico-real-estate-clean.csv", index=False)
