import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def mystery_scatter(n=100, var=200, random=False):
    
    '''Randomly generate data, one of which is quadratic, another is exponential,
       and a third is linear.
       Plot all sets of data side-by-side, then return a pandas dataframe'''
    
    if random == False:
        np.random.seed(7182818)
    
    '''Generate some data, not much rhyme or reason to these numbers, just wanted everything 
       to be on the same scale and the two curved datasets should be hard to tell apart'''
    
    x = np.random.uniform(5, 100, n)
    y1 = 11.45 * x ** 2 - 234.15 * x + 5000 + np.random.normal(0, var, n) * np.sqrt(x)
    y2 = 5000 * 1.03 ** x + np.random.normal(0, var, n) * np.sqrt(x)
    y3 = 5000 * x ** 1.9 + np.random.normal(0, 20 * var, n) * x
    y4 = 856.16 * x - 10107.3 + np.random.normal(0, 6 * var, n)
    
    
    '''Graph the plots'''
    
    plt.figure(figsize=(14, 14), )
    
    plt.subplot(2,2,1)
    sns.scatterplot(x, y1)
    plt.title('Mystery #1')
    
    plt.subplot(2,2,2)
    sns.scatterplot(x, y2)
    plt.title('Mystery #2')
    
    plt.subplot(2,2,3)
    sns.scatterplot(x, y3)
    plt.title('Mystery #3')
    
    plt.subplot(2,2,4)
    sns.scatterplot(x, y4)
    plt.title('Linear')
    
    plt.suptitle('Mystery Challenge: \nOne of these is Exponential, one is Power, \nand the other is Quadratic, but which is which?')
    plt.show()
    plt.savefig('mystery_growth.png')
    plt.close()
    
    df = pd.DataFrame([x, y1, y2, y3, y4]).T
    df.columns = ['x', 'mystery_1', 'mystery_2', 'mystery_3', 'linear']
    df.sort_values('x', inplace=True)
    df.reset_index(drop=True, inplace=True)
    return df