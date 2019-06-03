import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Import both data tables into python using pandas. Set the index column to "MESS_DATUM" and parse the column values as dates. [1P]
garmisch  = 
zugspitze = 

# Clip the tables to the year 2018: [1P]
garmisch  = 
zugspitze = 

# Resample the temperature data to monthly averages (" TMK") and the precipitation data to monthly sums (" RSK"): [1P]
garmisch_agg  = 
zugspitze_agg = 

# Define a plotting function that draws a simple climate diagram
# Add the arguments as mentioned in the docstring below [1P]
# Set the default temperature range from -15°C to 20°C and the precipitation range from 0mm to 370mm [1P]
def create_climate_diagram(...):
    """
    Draw a climate diagram.
    
    Parameters
    ----------
    df : pd.DataFrame
        Dataframe with values to plot from
    temp_col : str
        Name of temperature column
    prec_col : str
        Name of precipitation column
    title : String
        The title for the figure
    filename : String
        The name of the output figure
    temp_min : Number
        The minimum temperature value to display
    temp_max : Number
        The maximum temperature value to display
    prec_min : Number
        The minimum precipitation value to display
    prec_max : Number
        The maximum precipitation value to display

    Returns
    -------
    The figure
    
    """

    fig = plt.figure(figsize=(10,8))
    plt.rcParams['font.size'] = 16

    ax2 = fig.add_subplot(111)
    ax1 = ax2.twinx()

    # Draw temperature values as a red line and precipitation values as blue bars: [1P]
    # Hint: Check out the matplotlib documentation how to plot barcharts. Try to directly set the correct
    #       x-axis labels (month shortnames).
    ax2.bar(...)
    ax1.plot(...)
    
    # Set appropiate limits to each y-axis using the function arguments: [1P]
    ax2.
    ax1.
    
    # Set appropiate labels to each y-axis: [1P]
    ax2.
    ax1.

    # Give your diagram the title from the passed arguments: [1P]
    plt.title(...)

    # Save the figure as png image in the "output" folder with the given filename. [1P]
    
    return fig

# Use this function to draw a climate diagram for 2018 for both stations and save the result: [1P]
create_climate_diagram(...)
create_climate_diagram(...)
