### importing packages 
from termios import TAB1
from google.cloud import bigquery
import pandas as pd ## import pandas for general file types 
import json ## imoprt json for json files
import bs4 ## import bs4 for html files
import requests ## import requests for web requests
import geopandas as gpd ## import geopandas for geospatial files
from google.cloud import bigquery ## import bigquery for bigquery files
import matplotlib
import xlrd ## import xlrd for excel files, tab names 



""" Section 1: Find or create 1 excel (.xls) file that contains at least two tabs. Bring in the first tab as a data frame; 
label that dataset as ‘tab1’, and a second data frame that represents the 2nd tab of the excel file, name this 'tab2' """
 
    
    ##  Convert XLS into Data Frames
        df =  pd.read_excel('data/Dataset.xls')
        df 
    ## Convert first two Spreadsheets into Tabs  
        tab1 = pd.read_excel('data/Dataset.xls', sheet_name='Madden 23 Ratings')
        tab1 #Read Tab 1
        tab2 = pd.read_excel('data/Dataset.xls', sheet_name='Data Science Salaries')
        tab2 #Read Tab 2
        

""" - Section 2: Find 1 open source json API via CMS, and bring it in using the 'requests' package ; call the dataset ‘apiDataset’  """
    
    ## Data request from https://data.cms.gov/data-api/v1/dataset/c8a139ee-9e31-444c-976f-bab6b287b871/data
        request_data = requests.get('https://data.cms.gov/data-api/v1/dataset/c8a139ee-9e31-444c-976f-bab6b287b871/data')
    ## load as json 
        apiDataset = request_data.json()

    ## load into dataframe
        df = pd.read_json(apiDataset)
        df # Read json file
        
""" Section 3 (TRY YOUR BEST): Brings in 2 open source bigquery datasets; limit your query to get the first 100 rows from each,
    as either a dataframe or dictionary; please call the first dataset ‘bigquery1’ and the second dataset ‘bigquery2’;"""  
    ##  Connecting to Google BigQuery using json authenfication key  
        client = bigquery.Client.from_service_account_json('.google_bigquery/angel-507-3a181e4f70d4.json')
    ## query public dataset
        query_job = client.query("SELECT * FROM `bigquery-public-data.chicago_crime.crime` LIMIT 100") ## query public dataset
    ## get results
        results = query_job.result() ## get results
    ## putresults into dataframe
        df = pd.DataFrame(results.to_dataframe()) ## put results into dataframe
        df


