# This entrypoint file to be used in development. Start by reading README.md
import time_series_visualizer
from unittest import main


# Test your function by calling it here
time_series_visualizer.draw_line_plot()
time_series_visualizer.draw_bar_plot()
time_series_visualizer.draw_box_plot()

# Run unit tests automatically
main(module='test_module', exit=False)

import pandas as pd

df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

df = df[(df['value'] >= df['value'].quantile(0.025)) & 
(df['value'] <= df['value'].quantile(0.975))]
  
import matplotlib.pyplot as plt

def draw_line_plot():
    plt.figure(figsize=(10,5))
    plt.plot(df.index, df['value'], color='red', linewidth=1)
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.grid(True)
    plt.show()
draw_line_plot()

    def draw_bar_plot():
        df['year'] = df.index.year
        df['month'] = df.index.month
        df_group = df.groupby(['year', 'month'])['value'].mean()

        df_group.unstack().plot(kind='bar', figsize=(12, 10))
        plt.xlabel('Years')
        plt.ylabel('Average Page Views')
        plt.legend(title='Months', labels=['January', 'February', 'March', 'April', 'May', 'June', 'July',
                                           'August', 'September', 'October', 'November', 'December'])
        plt.show()

    draw_bar_plot()

    import seaborn as sns

    def draw_box_plot():
        df['date'] = df.index.to_period('M')

        fig, axes = plt.subplots(1, 2, figsize=(20, 10))
        fig.suptitle('Page Views Box Plots')

        sns.boxplot(ax=axes[0], x=df['year'], y=df['value'])
        axes[0].set_title('Year-wise Box Plot (Trend)')
        axes[0].set_xlabel('Year')
        axes[0].set_ylabel('Page Views')

        sns.boxplot(ax=axes[1], x=df['date'].dt.month, y=df['value'])
        axes[1].set_title('Month-wise Box Plot (Seasonality)')
        axes[1].set_xlabel('Month')
        axes[1].set_ylabel('Page Views')

        plt.show()

    draw_box_plot()
    ```

   

    
