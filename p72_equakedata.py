'''
Author: Derek Martin

Assignment: Project 7.2 Earthquake Data CIS 210 Winter 2019

Credits: N/A

Description: Use file processing and data analysis to find and report information about earthquake activity
centered in Eugene, Oregon, over the past 100 years.
'''
import p51_data_analysis

def equake_readf(fname):
    '''
    (str) -> list

    Create and return a list of the earthquake magnitudes from the file 'fname'

    >>> equake_readf('short50.txt')
    ['5.2', '5.1', '6', '5.9']
    >>> equake_readf('short25.txt')
    ['2.53', '2.99', '2.56', '2.83']
    '''
    equake_list = []
    magnitudes = []
    equake_file = open(fname, "r")
    '''
    for line in equake_file: # separate each earthquake in the file
        line.split(',')
        equake_list.append(line)
    '''
    for line in equake_file: # get the magnitude information
        data = line.split(',')
        magnitudes.append(float(data[4]))
    del magnitudes[0] # remove the header information
    return magnitudes

def equake_analysis(magnitudes):
    '''
    (list) -> tuple

    Analyze the magnitude data and return statistics about the data set.

    >>> equake_analysis([5.2, 5.1, 6.0, 5.9])
    (5.55, 5.55, [5.2, 5.1, 6.0, 5.9])
    >>> equake_analysis([2.53, 2.99, 2.56, 2.83])
    (2.73, 2.7, [2.53, 2.99, 2.56, 2.83])
    '''
    mean = round(p51_data_analysis.mean(magnitudes), 2)
    median = round(p51_data_analysis.median(magnitudes), 2)
    mode = p51_data_analysis.mode(magnitudes)
    mmm = (mean, median, mode)
    return mmm

def equake_report(mmm, magnitudes):
    '''
    (tuple), (list) -> None

    Report the number (count) of earthquakes, the mean, median, and mode of magnitudes, and call frequencyTable to report the number of occurrences of each item in magnitudes.

    >>> equake_report((2.73, 2.7, [2.53, 2.99, 2.56, 2.83]),[2.53, 2.99, 2.56, 2.83])
    Number of equakes: 4
    Mean: 2.73
    Median: 2.7
    Mode: [2.53, 2.99, 2.56, 2.83]
    >>> 
    '''
    mean, median, mode = (mmm)
    print("Number of earthquakes:", len(magnitudes))
    print("Mean magnitude:", mean)
    print("Median magnitude:", median)
    print("Mode magnitude:", mode)
    return None
    
def main():
    '''
    () -> None
    Calls: equake_readf, equake_analysis, equake_report
    Top level function for earthquake data analysis.
    Returns None.
    '''
    #fname = 'equakes25f.txt'
    fname = 'equakes50f.txt'

    emags = equake_readf(fname)
    mmm = equake_analysis(emags)
    equake_report(mmm, emags)
    return None

main()
