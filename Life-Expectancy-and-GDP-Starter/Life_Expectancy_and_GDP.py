import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
from matplotlib import ticker as mtick
from scipy import stats


df = pd.read_csv('all_data.csv')



#Renaming column for easier access
df.rename(columns={'Life expectancy at birth (years)': 'Life_Expectancy'}, inplace = True)



#Seperating data by country

chile = df[df.Country == 'Chile'].reset_index()
china = df[df.Country == 'China'].reset_index()
germany = df[df.Country == 'Germany'].reset_index()
mexico = df[df.Country == 'Mexico'].reset_index()
usa = df[df.Country == 'United States of America'].reset_index()
zimbabwe = df[df.Country == 'Zimbabwe'].reset_index()



def linereg(df, dfx, dfy):
    #Line Reg stats
    slope, intercept,rval, pval, err = stats.linregress(df[dfx], df[dfy])
    
    #Let's normalize the GDP for each country so that the slope of the line doesnt look ridiculously small.
    #If the GDP is within the given range, the slope will be normalized for easier compairson to the other plots.
    if df[dfx].mean() < 1000000000:
        slope = round(slope * 1e8, 3)
    elif df[dfx].mean() >= 1000000000 and df[dfx].mean() < 10000000000:
        slope = round(slope*1e9, 3)
    elif df[dfx].mean() >= 10000000000 and df[dfx].mean() < 100000000000:
        slope = round(slope* 1e10, 3)
    elif df[dfx].mean() >= 100000000000 and df[dfx].mean() < 1000000000000:
        slope = round(slope * 1e11, 3)
    elif df[dfx].mean() >= 1000000000000 and df[dfx].mean() < 10000000000000:
        slope = round(slope * 1e12, 3)
    elif df[dfx].mean() >= 10000000000000 and df[dfx].mean() < 100000000000000:
        slope = round(slope * 1e13, 3)
        
    #Round intercept to 3 decimal places
    intercept = round(intercept, 3)
    
    #Rval shows how 'good' your data is, closer to 1 is better. Typically reject data < 95 R^2 val.
    rval = round(rval, 3)
    
    #Set fig size, and save ax in case we need to change axis ticks or labels later
    fig, ax = plt.subplots(figsize = (12, 10))
    
    
    #Lets set some style
    sns.set_style('white')
    sns.set_palette('Set1')
    
    #Plot a regression plot, data is dataframe(the ones seperated above), x is GDP, y is Life Expectency. 
    #Line_kws sets parameters for the regline. Label will be the line formula y = mx + b where m is the slope and b is the intercept.
    #Show the Rval with the label, set the color to red and the linewidth scale to 0.8.
    sns.regplot(data = df, x = dfx, y = dfy, line_kws={'label': 'y = {}*x + {}.\nR^2 Value: {}.\nSlope has been normalized based on country\'s GDP'.format(slope, intercept, rval), 'color': 'blue', 'alpha': 0.7, 'lw': .8})

    #Extract the name of the country from the data frame being plotted.
    name = df.Country[0]
    
    #Use that name in the title.
    plt.title('{}\'s Life Expectancy Compared to GDP'.format(name))
    
    #This sets the GDP label, specifically the units for the GDP, correct based on the countries mean GDP.
    if df[dfx].mean() < 1000000000:
        plt.xlabel('GDP (Hundreds of Millions of Dollars')
    elif df[dfx].mean() >= 1000000000 and df[dfx].mean() < 10000000000:
        plt.xlabel('GDP (Billions of Dollars)')
    elif df[dfx].mean() >= 10000000000 and df[dfx].mean() < 100000000000:
        plt.xlabel('GDP (Tens of Billions of Dollars')
    elif df[dfx].mean() >= 100000000000 and df[dfx].mean() < 1000000000000:
        plt.xlabel('GDP (Hundreds of Billions of Dollars)')
    elif df[dfx].mean() >= 1000000000000 and df[dfx].mean() < 10000000000000:
        plt.xlabel('GDP (Trillions of Dollars)')
    elif df[dfx].mean() >= 10000000000000 and df[dfx].mean() < 100000000000000:
        plt.xlabel('GDP (Tens of Trillions of Dollars)')
        
    #Change axis labels. Can be changed based on what your regplot is.
    plt.ylabel('Life Expectancy (Years)')
    
    #Used to show the legend we created when we called 'label' in the sns.regplot(line_kws={}).
    plt.legend()
    
    #Show and close the plot
    plt.show()
    plt.clf()

#Call the function with the dataframe, x-axis, and y-axis.
linereg(chile, 'GDP', 'Life_Expectancy')
linereg(china, 'GDP', 'Life_Expectancy')
linereg(germany, 'GDP', 'Life_Expectancy')
linereg(mexico, 'GDP', 'Life_Expectancy')
linereg(usa, 'GDP', 'Life_Expectancy')
linereg(zimbabwe, 'GDP', 'Life_Expectancy')


#As GDP increaces over the years, so does life expectancy. The same code can be used with modificationsin order to look at the 'Year' vs 'Life expectancy'
#I expect to see the same kind of positive trend as we see with GDP increace.
