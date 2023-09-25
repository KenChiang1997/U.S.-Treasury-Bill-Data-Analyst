import numpy as np 
import pandas as pd 


def get_economic_outlook_data(fred):

    ism_inventory_data = pd.read_excel("/Users/chen-lichiang/Desktop/King's Hedge Fund Society/EM Credit Risk Modeling/Data/ISM_Data.xlsx").dropna()

    real_personal_income = fred.get_series('W875RX1').reset_index(name = 'real personal income excluding transfer')
    real_personal_consumption_expenditure = fred.get_series('PCEC96').reset_index(name = 'real personal consumption expenditure')

    private_household_wage_and_salary = fred.get_series('LNU02032190').reset_index(name = 'Household Wage & Salary')
    Michigan_Consumer_Confident = fred.get_series("UMCSENT").reset_index(name = 'Michigan: Consumer Sentiment')

    economic_outlook_data = real_personal_income.copy()
    economic_outlook_data = pd.merge(economic_outlook_data, real_personal_consumption_expenditure)
    economic_outlook_data = pd.merge(economic_outlook_data, private_household_wage_and_salary )
    economic_outlook_data = pd.merge(economic_outlook_data, Michigan_Consumer_Confident )
    economic_outlook_data = pd.merge(economic_outlook_data, ism_inventory_data)

    economic_outlook_data['Real Personal Income(excluding transfer) YoY'] = economic_outlook_data['real personal income excluding transfer'].pct_change(12) * 100
    economic_outlook_data['Real Personal Income Expenditure YoY'] = economic_outlook_data['real personal consumption expenditure'].pct_change(12) * 100
    economic_outlook_data['Household Wage & Salary YoY'] = economic_outlook_data['Household Wage & Salary'].pct_change(12) * 100

    return economic_outlook_data

def get_us_gdp_data(fred):

    real_gpd = fred.get_series('GDPC1').reset_index(name = 'real gross domestic product')
    nominal_gpd = fred.get_series('GDP').reset_index(name = 'nominal gross domestic product')

    gdp_df = pd.merge(real_gpd, nominal_gpd)
    gdp_df['Real GDP QoQ'] = gdp_df['real gross domestic product'].pct_change() * 100
    gdp_df['Real GDP YoY'] = gdp_df['real gross domestic product'].pct_change(4) * 100
    gdp_df['Nominal GDP QoQ'] = gdp_df['nominal gross domestic product'].pct_change() * 100
    gdp_df['Nominal GDP YoY'] = gdp_df['nominal gross domestic product'].pct_change(4) * 100

    gdp_df[['Real GDP QoQ', 'Real GDP YoY', 'Nominal GDP QoQ', 'Nominal GDP YoY']] = gdp_df[['Real GDP QoQ', 'Real GDP YoY', 'Nominal GDP QoQ', 'Nominal GDP YoY']].round(decimals = 2)

    return gdp_df