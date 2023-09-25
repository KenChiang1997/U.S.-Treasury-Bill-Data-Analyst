import requests
import numpy as np 
import pandas as pd 
import datetime as dt 
from fredapi import Fred 

import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
temp = dict(layout = go.Layout(font = dict(family="Franklin Gothic", size=12), width = 1500))


def get_inflation_dataset(fred):

    consumer_price_index = fred.get_series('CPIAUCSL').reset_index(name = 'CPI')
    consumer_price_index['CPI QoQ'] = consumer_price_index['CPI'].pct_change() * 100
    consumer_price_index['CPI YoY'] = consumer_price_index['CPI'].pct_change(12) * 100


    core_inflation_index = fred.get_series('CPILFESL').reset_index(name = 'Core CPI')
    core_inflation_index['Core CPI QoQ'] = core_inflation_index['Core CPI'].pct_change() * 100
    core_inflation_index['Core CPI YoY'] = core_inflation_index['Core CPI'].pct_change(12) * 100

    consumer_price_index_oil = fred.get_series('CUSR0000SEHE').reset_index(name = "Oil CPI")
    consumer_price_index_oil['Oil CPI QoQ'] = consumer_price_index_oil['Oil CPI'].pct_change() * 100
    consumer_price_index_oil['Oil CPI YoY'] = consumer_price_index_oil['Oil CPI'].pct_change(12) * 100 

    consumer_price_index_electricity = fred.get_series('CUSR0000SEHF01').reset_index(name = "Electricity CPI")
    consumer_price_index_electricity['Electricity CPI QoQ'] = consumer_price_index_electricity['Electricity CPI'].pct_change() * 100
    consumer_price_index_electricity['Electricity CPI YoY'] = consumer_price_index_electricity['Electricity CPI'].pct_change(12) * 100 

    consumer_price_index_housing = fred.get_series("CPIHOSSL").reset_index(name = "Housing CPI")
    consumer_price_index_housing['Housing CPI QoQ'] = consumer_price_index_housing['Housing CPI'].pct_change() * 100
    consumer_price_index_housing['Housing CPI YoY'] = consumer_price_index_housing['Housing CPI'].pct_change(12) * 100 

    consumer_price_index_food = fred.get_series('CPIUFDSL').reset_index(name = 'Food CPI')
    consumer_price_index_food['Food CPI QoQ'] = consumer_price_index_food['Food CPI'].pct_change() * 100
    consumer_price_index_food['Food CPI YoY'] = consumer_price_index_food['Food CPI'].pct_change(12) * 100

    consumer_price_index_energy = fred.get_series('CPIENGSL').reset_index(name = 'Energy CPI')
    consumer_price_index_energy['Energy CPI QoQ'] = consumer_price_index_energy['Energy CPI'].pct_change() * 100
    consumer_price_index_energy['Energy CPI YoY'] = consumer_price_index_energy['Energy CPI'].pct_change(12) * 100

    super_sticky_index = fred.get_series('CRESTKCPIXSLTRM159SFRBATL').reset_index(name = 'Sticky CPI YoY')

    inflation_data = pd.merge(consumer_price_index, core_inflation_index)
    inflation_data = pd.merge(inflation_data, consumer_price_index_electricity)
    inflation_data = pd.merge(inflation_data, consumer_price_index_food)
    inflation_data = pd.merge(inflation_data, consumer_price_index_energy)
    inflation_data = pd.merge(inflation_data, consumer_price_index_oil)
    inflation_data = pd.merge(inflation_data, consumer_price_index_housing)
    inflation_data = pd.merge(inflation_data, super_sticky_index)

    inflation_data[['CPI QoQ', 'CPI YoY', 'Core CPI QoQ', 'Core CPI YoY','Food CPI QoQ','Food CPI YoY', 'Energy CPI QoQ', 'Energy CPI YoY', 'Sticky CPI YoY', 'Electricity CPI QoQ', 'Electricity CPI YoY', 'Oil CPI QoQ', 'Oil CPI YoY', 'Housing CPI QoQ', 'Housing CPI YoY']] = inflation_data[['CPI QoQ', 
                                                                                                                                                                'CPI YoY', 
                                                                                                                                                                'Core CPI QoQ', 
                                                                                                                                                                'Core CPI YoY',
                                                                                                                                                                'Food CPI QoQ',
                                                                                                                                                                'Food CPI YoY',
                                                                                                                                                                'Energy CPI QoQ',
                                                                                                                                                                'Energy CPI YoY',
                                                                                                                                                                'Sticky CPI YoY',
                                                                                                                                                                'Electricity CPI QoQ', 
                                                                                                                                                                'Electricity CPI YoY', 
                                                                                                                                                                'Oil CPI QoQ', 
                                                                                                                                                                'Oil CPI YoY',
                                                                                                                                                                'Housing CPI QoQ', 
                                                                                                                                                                'Housing CPI YoY']].round(decimals = 2)

    return inflation_data


def get_detail_commodity_data(fred):

    used_car = fred.get_series("CUSR0000SETA02").reset_index(name = "Used Cars and Trucks in U.S. City Average")
    owner_rent = fred.get_series("CUSR0000SEHC").reset_index(name = "Owners' Equivalent Rent") 
        
    detail_commodity_data = pd.merge(owner_rent, used_car)
    detail_commodity_data["Owners' Equivalent Rent QoQ"] = detail_commodity_data["Owners' Equivalent Rent"].pct_change() * 100
    detail_commodity_data["Used Cars and Trucks in U.S. City Average QoQ"] = detail_commodity_data["Used Cars and Trucks in U.S. City Average"].pct_change() * 100
    detail_commodity_data[["Owners' Equivalent Rent QoQ", "Used Cars and Trucks in U.S. City Average QoQ"]] = detail_commodity_data[["Owners' Equivalent Rent QoQ", "Used Cars and Trucks in U.S. City Average QoQ"]] * 12 


    wti_crude_oil = fred.get_series("DCOILWTICO").reset_index(name = "Crude Oil West Texas Intermediate (WTI)") 

    return detail_commodity_data, wti_crude_oil


def get_organized_cpi_data(inflation_data):
        
    organized_cpi_data = inflation_data[['CPI', 'Food CPI', 'Energy CPI', 'Oil CPI', 'Electricity CPI', 'Core CPI', 'Housing CPI']]
    organized_cpi_data.index = inflation_data['index'] 

    organized_cpi_table_data = organized_cpi_data.pct_change().tail(7).T * 100
    organized_cpi_table_data = organized_cpi_table_data.round(1)
    organized_cpi_table_data.columns = [ str(cols)[:7] + " MoM" for cols in organized_cpi_table_data.columns]

    organized_cpi_yoy_data = pd.DataFrame(organized_cpi_data.pct_change(12).tail(1).T * 100)
    organized_cpi_yoy_data.columns = ['YoY Change']
    organized_cpi_yoy_data = organized_cpi_yoy_data.round(decimals = 1)


    organized_cpi_table_data = pd.concat([organized_cpi_table_data, organized_cpi_yoy_data ], axis = 1)
    
    return organized_cpi_table_data

def get_pce_data(fred, inflation_data):

    pce_data = fred.get_series("PCEPI").reset_index(name = "PCE")

    pce_data['PCE MoM'] = pce_data['PCE'].pct_change() * 100
    pce_data['PCE YoY'] = pce_data['PCE'].pct_change(12) * 100

    pce_data = pd.merge(pce_data, inflation_data[['index', 'CPI', "CPI YoY", "CPI QoQ"]])
    pce_data['CPI MoM - PCE MoM'] = pce_data['CPI QoQ'] - pce_data['PCE MoM']

    pce_data['PCE MoM Rolling Volatility(12M)'] = pce_data['PCE MoM'].rolling(window = 12).std()
    pce_data['CPI MoM Rolling Volatility(12M)'] = pce_data['CPI QoQ'].rolling(window = 12).std()
    pce_data['CPI MoM - PCE MoM Rolling Volatility(12M)'] = pce_data['CPI MoM - PCE MoM'].rolling(window = 12).std()


    return pce_data

def get_organized_pce_data(pce_data):

    organized_pce_data = pce_data[['PCE MoM', 'PCE YoY']].tail(7)
    organized_pce_data.index = pce_data['index'].tail(7)

    organized_pce_data = organized_pce_data.T
    organized_pce_data.columns = [ str(cols)[:7] for cols in organized_pce_data.columns]

    return organized_pce_data.round(decimals = 1)