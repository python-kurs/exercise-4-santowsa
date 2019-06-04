from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Import both data tables into python using pandas. Set the index column to "MESS_DATUM" and parse the column values as dates. [1P]
mainDir = Path("C:/Users/Admin/Documents/GitHub/exercise-4-santowsa/")
data_dir = mainDir / "data"
zugspitze = pd.read_csv(data_dir / "produkt_klima_tag_20171010_20190412_05792.txt", parse_dates=["MESS_DATUM"], index_col=["MESS_DATUM"], sep=";", na_values=-999.0)
garmisch = pd.read_csv(data_dir / "produkt_klima_tag_20171010_20190412_01550.txt", parse_dates=["MESS_DATUM"], index_col=["MESS_DATUM"], sep=";", na_values=-999.0)
# Clip the tables to the year 2018: [1P]
garmisch  = garmisch.loc["2018-01-01" : "2018-12-31"]
zugspitze = zugspitze.loc["2018-01-01" : "2018-12-31"]

# Resample the temperature data to monthly averages (" TMK") and the precipitation data to monthly sums (" RSK"): [1P]
zugspitze_agg = zugspitze.loc[:,[" TMK"," RSK"]].resample("1M").agg({" TMK": "mean"," RSK": "sum"})
garmisch_agg = garmisch.loc[:,[" TMK"," RSK"]].resample("1M").agg({" TMK": "mean"," RSK": "sum"})

# Define a plotting function that draws a simple climate diagram
# Add the arguments as mentioned in the docstring below [1P]
# Set the default temperature range from -15°C to 20°C and the precipitation range from 0mm to 370mm [1P]
def create_climate_diagram(df,
                           temp_col,
                           prec_col,
                           title,
                           filename,
                           temp_min=-15,
                           temp_max=20,
                           prec_min=0,
                           prec_max=370):
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
    days = mdates.DayLocator(bymonthday=1)
    monthFmt = mdates.DateFormatter("%b")
    ax2.xaxis.set_major_locator(days)
    ax2.xaxis.set_major_formatter(monthFmt)
    ax1.xaxis.set_major_locator(days)
    ax1.xaxis.set_major_formatter(monthFmt)
    
    ax2.bar(df.index, height=df[prec_col], color="blue", width=20, label="precipitation")
    ax1.plot(df[temp_col], color="red", label="temperature")
    
    # Set appropiate limits to each y-axis using the function arguments: [1P]
    ax2.set_ylim(prec_min, prec_max)
    ax1.set_ylim(temp_min, temp_max)
    
    # Set appropiate labels to each y-axis: [1P]
    ax2.set_ylabel("precipitation in mm")
    ax1.set_ylabel("temperature in °C")

    # Give your diagram the title from the passed arguments: [1P]
    plt.title(title)

    # Save the figure as png image in the "output" folder with the given filename. [1P]
    plt.savefig(filename)
    return fig

# Use this function to draw a climate diagram for 2018 for both stations and save the result: [1P]

create_climate_diagram(garmisch_agg, " TMK", " RSK", "Garmisch-Partenkirchen/Germany, \n 47°29'N/11°05'E, 705 m a.s.l. \n year 2018", mainDir / "Garmisch-Partenkirchen.png" )
create_climate_diagram(zugspitze_agg, " TMK", " RSK", "Zugspitze/Germany, \n 47°25'N/10°59'E, 2962 m a.s.l. \n year 2018", mainDir / "Zugspitze.png" )
