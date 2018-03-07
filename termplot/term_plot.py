#!/usr/bin/env python3

from __future__ import print_function

def make_col(y,max_height, plot_char):
    #requires positive value
    col_list = []
    for i in range(max_height):
        if i >= y:
            col_list.append(' ')
        else:
            col_list.append(plot_char)
    return col_list

def make_neg_col(y,max_height, plot_char):
    #requires negative value
    col_list = []
    for i in reversed(range(max_height)):
        if y >= -i:
            col_list.append(' ')
        else:
            col_list.append(plot_char)
    return col_list

def scale_data(x, plot_height):
    '''scales list data to allow for floats'''
    result = []
    z = [abs(i) for i in x]
    for i in x:
        temp = i/float(max(z))
        temp2 = temp*plot_height
        result.append(int(temp2))
    return result

def plot(x, plot_height=10, plot_char=u'\u25cf'):
    ''' takes a list of ints or floats x and makes a simple terminal histogram.
        This function will make an inaccurate plot if the length of data list is larger than the number of columns
        in the terminal.'''
    x = scale_data(x, plot_height)

    max_pos = max(x)
    max_neg = abs(min(x))

    hist_array = []
    neg_array = []

    for i in x:
        hist_array.append(make_col(i, max_pos, plot_char))

    for i in x:
        neg_array.append(make_neg_col(i, max_neg, plot_char))

    for i in range(len(neg_array)):
        neg_array[i].extend(hist_array[i])

    for i in reversed(range(len(neg_array[0]))):
        for j in range(len(neg_array)):
            print(neg_array[j][i], end='')
        print('')
