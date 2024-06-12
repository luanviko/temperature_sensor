# temperature_sensor
A program to read temperature measurements from two Phidgets TEMP_1100_0 thermocouples connected to a Phidgets HUB0000_0 hub. 


## Usage

To start acquisition of temperature using thermocouples install on port 0 and 1, run

```python3 measure_temperature.py <run_number>```

where <run_number> is an integer, such as *10*. The data will automatically saved as *./data/temp_info_0010.csv*.

To start a live plot of the data being taken

```python3 live_plot.py```

To plot an static curve

```python3 plot_temperature.py <file_path>```

where <file_path> is the path to an specific temperature data file, such as *./data/temp_info_0010.csv*.


## Dependencies

measure_temperature.py: [Phiget22](https://www.phidgets.com/docs/OS_-_Linux) libraries and [numpy](https://numpy.org/). 

live_plot.py and plot_temperature.py: [numpy](https://numpy.org/) and [matplotlib](https://matplotlib.org/)
