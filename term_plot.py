def make_col(y,max_height):
    #requires positive value
    col_list = []
    for i in range(max_height):
        if i >= y:
            col_list.append(' ')
        else:
            col_list.append('\u25cf')
    return col_list

def make_neg_col(y,max_height):
    #requires negative value
    col_list = []
    for i in reversed(range(max_height)):
        if y >= -i:
            col_list.append(' ')
        else:
            col_list.append('\u25cf')
    return col_list

def plot(x, plot_size=5):
    x = scale_data(x, plot_size)

    max_pos = max(x)
    max_neg = abs(min(x))

    hist_array = []
    neg_array = []

    for i in x:
        hist_array.append(make_col(i, max_pos))

    for i in x:
        neg_array.append(make_neg_col(i, max_neg))

    for i in range(len(neg_array)):
        neg_array[i].extend(hist_array[i])

    for i in reversed(range(len(neg_array[0]))):
        for j in range(len(neg_array)):
            print(neg_array[j][i], end='')
        print('')

def scale_data(x, plot_height):
    result = []
    z = [abs(i) for i in x]
    for i in x:
        temp = i/max(z)
        temp2 = temp*plot_height
        result.append(int(temp2))
    return result