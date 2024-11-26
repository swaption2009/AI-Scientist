import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

def plot_strategy_comparison(blue_ocean_data, red_ocean_data, metric_name):
    """
    Plot comparison between blue ocean and red ocean strategies for a given metric
    """
    plt.figure(figsize=(10, 6))
    
    # Create box plots
    data = [blue_ocean_data, red_ocean_data]
    labels = ['Blue Ocean Strategy', 'Red Ocean Strategy']
    
    plt.boxplot(data, labels=labels)
    plt.title(f'{metric_name} Comparison: Blue Ocean vs Red Ocean Strategies')
    plt.ylabel(metric_name)
    
    return plt

def plot_time_series(dates, blue_ocean_values, red_ocean_values, metric_name):
    """
    Plot time series comparison of strategies
    """
    plt.figure(figsize=(12, 6))
    
    plt.plot(dates, blue_ocean_values, label='Blue Ocean Strategy', color='blue')
    plt.plot(dates, red_ocean_values, label='Red Ocean Strategy', color='red')
    
    plt.title(f'{metric_name} Over Time: Strategy Comparison')
    plt.xlabel('Date')
    plt.ylabel(metric_name)
    plt.legend()
    
    return plt

def plot_innovation_matrix(market_creation, value_innovation):
    """
    Create a scatter plot showing market creation vs value innovation
    """
    plt.figure(figsize=(10, 10))
    
    plt.scatter(market_creation, value_innovation)
    plt.xlabel('Market Creation Index')
    plt.ylabel('Value Innovation Score')
    plt.title('Innovation Matrix: Market Creation vs Value Innovation')
    
    return plt

def save_plots(output_dir):
    """
    Save all generated plots to the specified directory
    """
    # Implementation will depend on the actual plots generated
    pass
