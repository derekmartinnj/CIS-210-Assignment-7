'''
Author: Derek Martin

Assignment: CIS 210 Project 7.1 Who is in CIS 210? Winter 2019

Credits: N/A

Description: Use file processing and data analysis to find and report information about the range of majors
represented in CIS 210 in Winter 2019.
'''
import p51_data_analysis

def majors_readf(fname):
    '''
    (str) -> list

    Open the given file and create a list of the majors in the file

    >>> majors_readf('majors_short.txt')
    ['CIS','CIS','EXPL','COLT','EXPL']
    >>> majors_readf('majors_short2.txt')
    ['CIS','EXPL','EXPL','CIS']
    '''
    majors_list = []
    majors_file = open(fname, "r")
    for line in majors_file:
        majors_list.append(line.strip())
    majors_list.remove("CIS 210 WINTER 2019")
    majors_list.remove("Major")
    return majors_list

def majors_analysis(majorsli):
    '''
    (list) -> tuple

    Analyze the given list of majors and determine the most common major, and the count of different majors

    >>> majors_analysis(['CIS', 'CIS', 'EXPL', 'COLT', 'EXPL'])
    (['CIS', 'EXPL'], 3)
    >>> majors_analysis(['CIS','EXPL','EXPL','CIS'])
    (['CIS', 'EXPL'], 2)
    '''
    shortened_list = [] # create another list to catch duplicate values in majorsli
    majors_mode = str(p51_data_analysis.mode(majorsli))
    majors_ct = 0
    for major in majorsli:
        if (major not in shortened_list):
            shortened_list.append(major)
            majors_ct += 1 # count the number of unique majors
    return (majors_mode, majors_ct)

def majors_report(majors_mode, majors_ct, majorsli):
    '''
    (tup)(int)(list) -> None

    Report and display the results of analyzing the majors file.

    >>> majors_report(['CIS', 'EXPL'], 3, ['CIS', 'CIS', 'EXPL', 'COLT', 'EXPL'])
    3 majors are represented in CIS 210 this term.
    The most represented major(s): CIS EXPL
    ITEM FREQUENCY
    CIS 2
    COLT 1
    EXPL 2
    '''
    print(majors_ct, "majors are represented in CIS 210 this term.")
    print("The most represented major(s):", majors_mode)
    print()
    p51_data_analysis.frequencyTable(majorsli)
    return None

def main():
    '''
    () -> None
    Calls: majors_readf, majors_analysis, majors_report
    Top level function for analysis of CIS 210 majors data.
    '''
    #fname = 'short_file.txt'
    fname = 'majors_cis210w19.txt'

    majorsli = majors_readf(fname) # read
    majors_mode, majors_ct = majors_analysis(majorsli) # analyze
    majors_report(majors_mode, majors_ct, majorsli) # report
    return None

main()
