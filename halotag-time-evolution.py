import matplotlib.pyplot as plt
import numpy as np

def plot_time_evo(axs, inp_name, title):
    with open(inp_name, 'r') as inp_file:
        inp_data = [inp_line.split()[5:] for inp_line in inp_file]
    dim1 = len(inp_data[1:]) 
    dim2 = len(inp_data[0]) 
    qn_arr = np.zeros((dim1, dim2))

    for i, idata in enumerate(inp_data[1:]):
        offset = dim2 - len(idata)
        jdata = idata + ['0']*offset
        qn_arr[i] = np.array(jdata)

    axs.matshow(qn_arr.T, cmap='jet', origin='lower', interpolation='gaussian')
    axs.set_title(title)
    axs.set_aspect(2.5)
    axs.set_xticks([])

if __name__ == '__main__':
    fig, axs = plt.subplots(2)
    plot_time_evo(axs[0], "native-non-native-contacts-coordist-tmd-pull.dat.merged", "Native")
    plot_time_evo(axs[1], "native-non-native-contacts-coordist-nn-tmd-pull.dat.merged", "Non-Native")
    
plt.show()