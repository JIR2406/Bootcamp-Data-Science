import matplotlib.pyplot as plt

def plot_time_series(axes,x,y,color,xlabel,ylabel):
    """
    Plots a time series on the given axes.

    Parameters:
    axes: matplotlib Axes object
    x: x data (time)
    y: y data (variable)
    color: color of the line
    xlabel: label for the x-axis
    ylabel: label for the y-axis
    """
    axes.plot(x, y, color=color)
    axes.set_xlabel(xlabel)
    axes.set_ylabel(ylabel, color=color)
    axes.tick_params(axis='y', labelcolor=color)