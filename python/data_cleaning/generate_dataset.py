from datetime import date
import numpy as nßp
import pandas as pd

from GitHub.indigent_burials.python.data_cleaning.utils import DataSource, combine  

def main() -> pd.DataFrame:
    ### Read in each dataframe and normalize column names ###
    #x = pd.read_csv().rename(columns=lambda x: x.strip())

    dig_memorial = pd.read_csv("https://raw.githubusercontent.com/IndigentBurials/indigent-burials/main/python/web-scraping/oregon-and-dignity-memorial/data/dignity-memorial.csv").rename(columns=lambda x: x.strip())
    chicago_burials = pd.read_csv("https://raw.githubusercontent.com/IndigentBurials/indigent-burials/main/python/web-scraping/chicago-cookcounty/data/Medical_Examiner_-_Burial_Locations.csv").rename(columns=lambda x: x.strip())
    chicago_cremations = pd.read_csv("https://raw.githubusercontent.com/IndigentBurials/indigent-burials/main/python/web-scraping/chicago-cookcounty/data/Medical_Examiner_Indigent_Cremations.csv").rename(columns=lambda x: x.strip())  
    king_county = pd.read_csv("https://raw.githubusercontent.com/IndigentBurials/indigent-burials/main/python/web-scraping/KingCounty/data/KingCounty%20Seattle%20Burial%20Names%20%20-%20Sheet1.csv").rename(columns=lambda x: x.strip())    
    bernalillo = pd.read_csv("https://raw.githubusercontent.com/IndigentBurials/indigent-burials/main/python/web-scraping/bernalillo-county/data/bernalillo%20county_indigent_unfilters.csv").rename(columns=lambda x: x.strip())  
    dona_ana =  pd.read_csv("https://raw.githubusercontent.com/IndigentBurials/indigent-burials/main/python/web-scraping/dona-ana-scraping/data/dona-ana-cleaned-v2.csv").rename(columns=lambda x: x.strip())  
    fresno = pd.read_csv("https://raw.githubusercontent.com/IndigentBurials/indigent-burials/main/python/web-scraping/fresno-scraping/data/fresno-cleaned3-v2.csv").rename(columns=lambda x: x.strip())  
    hart_island = pd.read_csv("https://raw.githubusercontent.com/IndigentBurials/indigent-burials/main/python/web-scraping/hart-island-web-scraper/data/output/hart-island.csv").rename(columns=lambda x: x.strip())  
    la_county = pd.read_csv("https://raw.githubusercontent.com/IndigentBurials/indigent-burials/main/python/web-scraping/la-county/data/LA%20Cremation%20Data%20Enhanced.csv").rename(columns=lambda x: x.strip())  
    namus = pd.read_csv("https://raw.githubusercontent.com/IndigentBurials/indigent-burials/main/python/web-scraping/namus/data/unclaimed_states_combined_cleaned.csv").rename(columns=lambda x: x.strip())  
    oregon = pd.read_csv("https://raw.githubusercontent.com/IndigentBurials/indigent-burials/main/python/web-scraping/oregon-and-dignity-memorial/data/oregon.csv").rename(columns=lambda x: x.strip())  
    yakima_county = pd.read_csv("https://raw.githubusercontent.com/IndigentBurials/indigent-burials/main/python/web-scraping/yakima-county/data/Unclaimed%20Remains_Yakima%20County.csv").rename(columns=lambda x: x.strip())  

    ### Map columns for each df
    dig_memorial_dict = _map_dignity_memorial(dig_memorial)
    chicago_burials_dict = _map_chicago_burials(chicago_burials)
    chicago_cremations_dict =  _map_chicago_cremations(chicago_cremations)
    king_county_dict = _map_king_county(king_county)
    bernalillo_dict = _map_bernalillo(bernalillo)
    dona_ana_dict = _map_dona_ana(dona_ana)
    fresno_dict = _map_fresno(fresno)
    hart_island_dict = _map_hart_island(hart_island)
    la_county_dict = _map_la_county(la_county)
    namus_dict = _map_namus(namus)
    oregon_dict = _map_oregon(oregon)
    yakima_county_dict = _map_yakima_county(yakima_county)

    ### Combine all dfs with correct mappings 
    combined_df = combine(
        DataSource(dig_memorial, dig_memorial_dict, "Dignity Memorial"),
        DataSource(chicago_burials, chicago_burials_dict, "Chicago Burials"),
        DataSource(chicago_cremations, chicago_cremations_dict, "Chicago Cremations"),
        DataSource(king_county, king_county_dict, "King County"),
        DataSource(bernalillo, bernalillo_dict, "Bernalillo"),
        DataSource(dona_ana, dona_ana_dict, "Dona Ana"),
        DataSource(fresno, fresno_dict, "Fresno"),
        DataSource(hart_island, hart_island_dict, "Hart Island"),
        DataSource(la_county, la_county_dict, "LA County"),
        DataSource(namus, namus_dict, "National"),
        DataSource(oregon, oregon_dict, "Oregon"),
        DataSource(yakima_county, yakima_county_dict, "Yakima County")
    )

    return combined_df

def _map_yakima_county(df: pd.DataFrame):
    df["LastModified"] = date.today()
    df["State"] = "Washington"
    df["Jurisdiction"] = "Yakima County"
    df["SourceURL"] = "https://dhs.lacounty.gov/home-public-resources-locate-deceased-persons/"
    
    df_dict = {
        "LName": "Last Name",
        "FName": "First Name",
        "MName": "Middle Name",
        "DOB": "DOB:",
        "DOD": "DOD:",
        "State": "State",
        "SourceURL": "SourceURL",
        "Jurisdiction": "Jurisdiction",
        "LastModified": "LastModified",
    }
    return df_dict

def _map_oregon(df: pd.DataFrame):
    df["LastModified"] = date.today()
    df["State"] = "Oregon"
    
    df_dict = {
        "LName": "Last Name",
        "FName": "First Name",
        "MName": "Middle Name",
        "BD": "Buried",
        "State": "State",
        "SourceURL": "Source URL",
        "Jurisdiction": "Jurisdicition",
        "LastModified": "LastModified",
    }
    return df_dict

def _map_namus(df: pd.DataFrame):
    df["LastModified"] = date.today()
    
    df_dict = {
        "LName": "Last Name",
        "FName": "First Name",
        "DOD": "DBF",
        "RaceEthnicity": "Race/Ethnicity",
        "Sex": "Sex",
        "City": "City",
        "County": "County",
        "State": "State",
        "SourceURL": "Source URL",
        "Jurisdiction": "Jurisdicition",
        "LastModified": "LastModified",
    }
    return df_dict

def _map_la_county(df: pd.DataFrame):
    df["LastModified"] = date.today()
    
    df_dict = {
        "LName": "Last.Ne",
        "FName": "First.Ne",
        "MName": "Middle.Ne",
        "BD": "Date.of.Cremation..mm.dd.yyyy.",
        "SourceURL": "Source URL",
        "Jurisdiction": "Jurisdiction",
        "LastModified": "LastModified",
    }
    return df_dict

def _map_hart_island(df: pd.DataFrame):
    df["LastModified"] = date.today()
    
    df_dict = {
        "LName": "LName",
        "FName": "FName",
        "DOD": "DOD",
        "Age": "Age",
        "Sex": "Sex",
        "SourceURL": "SourceURL",
        "Jurisdiction": "Jurisdiction",
        "LastModified": "LastModified",
    }
    return df_dict

def _map_fresno(df: pd.DataFrame):
    df["LastModified"] = date.today()
    
    df_dict = {
        "LName": "Last Name",
        "FName": "First Name",
        "MName": "Middle Name",
        "DOB": "DOB",
        "DOD": "DOD",
        "Age": "Age",
        "Sex": "Sex",
        "SourceURL": "Source URL",
        "Jurisdiction": "Jurisdiction",
        "LastModified": "LastModified",
    }
    return df_dict

def _map_dona_ana(df: pd.DataFrame):
    df["LastModified"] = date.today()
    
    df_dict = {
        "LName": "Last Name",
        "FName": "First Name",
        "MName": "Middle Name",
        "DOB": "DOB",
        "DOD": "DOD",
        "Age": "Age",
        "SourceURL": "Source URL",
        "Jurisdiction": "Jurisdiction",
        "LastModified": "LastModified",
    }
    return df_dict

def _map_bernalillo(df: pd.DataFrame):
    df["Jurisdiction"] = "Bernalill0"
    df["LastModified"] = date.today()
    df["isVeteran"] = df["Veteran"].replace({"Yes": 1, "No": 0})
    
    df_dict = {
        "LName": "Last Name",
        "FName": "First Name",
        "MName": "Middle Name",
        "OName": "Maiden Name",
        "DOB": "Date of Birth",
        "DOD": "Date of Death",
        "BD": "Cremation Date",
        "isVeteran": "isVeteran",
        "MilitaryAffiliation": "Military Branch",
        "Jurisdiction": "Jurisdiction",
        "LastModified": "LastModified",
    }
    return df_dict

def _map_king_county(df: pd.DataFrame):
    df["Jurisdiction"] = "King County"
    df["LastModified"] = date.today()
    
    df_dict = {
        "LName": "Last Name",
        "FName": "First Name",
        "MName": "Middle Name",
        "BD": "Year of Burial",
        "SourceURL": "Source URL",
        "Jurisdiction": "Jurisdiction",
        "LastModified": "LastModified",
    }
    
    return df_dict

def _map_chicago_cremations(df: pd.DataFrame):
    df["Jurisdiction"] = "Chicago, Cook County"
    df["LastModified"] = date.today()
    
    df_dict = {
        "LName": "LastName",
        "FName": "Name",
        "MName": "MiddleName",
        "Age": "Age",
        "Sex": "Sex",
        "RaceEthnicity": "Race",
        "BD": "Cremation Date",
        "DOD": "Date of Death",
        "SourceURL": "SourceURL",
        "Jurisdiction": "Jurisdiction",
        "LastModified": "LastModified",
    }
        
    return df_dict

def _map_dignity_memorial(df: pd.DataFrame):
    df["isVeteran"] = 1
    df["LastModified"] = date.today()
    df["DOB"] = pd.to_datetime(df["DOB"], utc=True, errors='coerce').dt.date
        
    df_dict = {
        "LName": "Last Name",
        "FName": "First Name",
        "MName": "Middle Name",
        "DOB": "DOB",
        "DOD": "DOD",
        "Jurisdiction": "Jurisdicition",
        "SourceURL": "Source URL",
        "DateScraped": "Date Scraped",
        "LastModified": "LastModified",
        "isVeteran": "isVeteran",
        "MilitaryAffiliation": "Department Of Defense"
    }
    
    return df_dict

def _map_chicago_burials(df: pd.DataFrame):
    df["Jurisdiction"] = "Chicago, Cook County"
    df["LastModified"] = date.today()
    
    df_dict = {
        "LName": "LastName",
        "FName": "FirstName",
        "MName": "MiddleName",
        "Age": "Age",
        "Sex": "Sex",
        "RaceEthnicity": "Race",
        "BD": "Burial Date",
        "DOD": "Date of Death",
        "Jurisdiction": "Jurisdiction",
        "LastModified": "LastModified",
    }
        
    return df_dict
            
def _map_yakima_county(df: pd.DataFrame):
    df["LastModified"] = date.today()
    df["State"] = "Washington"
    df["Jurisdiction"] = "Yakima County"
    df["SourceURL"] = "https://dhs.lacounty.gov/home-public-resources-locate-deceased-persons/"
    
    df_dict = {
        "LName": "Last Name",
        "FName": "First Name",
        "MName": "Middle Name",
        "DOB": "DOB:",
        "DOD": "DOD:",
        "State": "State",
        "SourceURL": "SourceURL",
        "Jurisdiction": "Jurisdiction",
        "LastModified": "LastModified",
    }
    return df_dict

if __name__ == "__main__":
    main()
    