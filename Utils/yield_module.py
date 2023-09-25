import numpy as np 
import pandas as pd 



def get_treasury_data(fred):

    three_month_yield = fred.get_series("DGS3MO").reset_index(name = '3M')
    six_month_yield = fred.get_series("DGS6MO").reset_index(name = '6M')

    one_year_yield = fred.get_series("DGS1").reset_index(name = '1Y')
    two_year_yield = fred.get_series("DGS2").reset_index(name = '2Y')
    three_year_yield = fred.get_series("DGS3").reset_index(name = '3Y')

    five_year_yield = fred.get_series("DGS5").reset_index(name = '5Y')
    ten_year_yield = fred.get_series("DGS10").reset_index(name = '10Y')
    thirty_year_yield = fred.get_series("DGS30").reset_index(name = '30Y')

    us_treasury_yield_df = pd.merge(three_month_yield, six_month_yield)
    us_treasury_yield_df = pd.merge(us_treasury_yield_df, one_year_yield)
    us_treasury_yield_df = pd.merge(us_treasury_yield_df, two_year_yield)
    us_treasury_yield_df = pd.merge(us_treasury_yield_df, three_year_yield)
    us_treasury_yield_df = pd.merge(us_treasury_yield_df, five_year_yield)
    us_treasury_yield_df = pd.merge(us_treasury_yield_df, ten_year_yield)
    us_treasury_yield_df = pd.merge(us_treasury_yield_df, thirty_year_yield)

    return us_treasury_yield_df


def get_yield_change_df(us_treasury_yield_df):

    date = us_treasury_yield_df.iloc[-1]['index']

    yield_dod_change = pd.DataFrame(us_treasury_yield_df.drop(['index'], axis = 1).pct_change(1).iloc[-1]) 
    yield_wow_change = pd.DataFrame(us_treasury_yield_df.drop(['index'], axis = 1).pct_change(5).iloc[-1]) 
    yield_mom_change = pd.DataFrame(us_treasury_yield_df.drop(['index'], axis = 1).pct_change(22).iloc[-1]) 
    yield_yoy_change = pd.DataFrame(us_treasury_yield_df.drop(['index'], axis = 1).pct_change(252).iloc[-1]) 

    yield_change_df = pd.concat([yield_dod_change, yield_wow_change, yield_mom_change, yield_yoy_change], axis = 1)
    yield_change_df.columns = ['1 Day Change', '1 Week(5 days) Change', '1 Month(22 days) Change', '1 Year(252 days) Change']

    yield_change_df = yield_change_df * 100
    yield_change_df = yield_change_df.round(decimals = 2)
    
    return yield_change_df 