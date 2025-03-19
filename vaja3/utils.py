import numpy as np
import matplotlib.pyplot as plt
import timeit as t
from timeit import default_timer as timer

# Class for algorithm testing
class Algorithm:

    name = "Algorithm"
    count_op = 0
    count_operations = []
    run_ntimes = 1

    input_data = []
    input_params = []
    data_params = {}
    result_data = []
    output = []

    def __init__(self):
        self.count_operations = []
        #self.my_globals.update({'self':self, 'result_data':self.result_data})

    def start_timer(self):
        return

    def create_data(self):
        return

    def run_once(self):
        # In this method add counting of operations
        self.count_op+=10
        print("Algorithm.run_once, operations: ", self.count_op)
        return []

    def run(self, ntimes = 0):
        if ntimes > 0:
            self.run_ntimes = ntimes

        self.count_operations = []
        result = {}
        output = []
        start = timer()
        for self.iter in range(0,self.run_ntimes):
            iter_start = timer()
            self.create_data()

            self.count_op = 0
            output = self.run_once()
            iter_end = timer()

            self.count_operations.append(self.count_op)
            print(" >> ", self.iter, ", msec: {:.3f}".format((iter_end-iter_start)*1000.0), ", operations: ", self.count_op)
        end = timer()
        avg_msec = (end-start)/self.run_ntimes*1000.0
        print(' >>> ', self.name, ' > Total run() sec: ', end-start, ' Avg iter msec:',  avg_msec)

        result["name"] = self.name
        result["avg_msec"] = avg_msec
        result["avg_O"] = sum(self.count_operations)/self.run_ntimes
        result["niter"] = self.run_ntimes
        result["output"] = output

        # print(self.count_operations)
        return result



class AlgorithmBenchmark:
    @staticmethod
    def plot_complexity(n_list, operations, reference_curves=None, title='Algorithm Complexity', ymax = None, yscale='linear'):
        """Plot algorithm complexity with optional reference curves."""
        plt.figure(figsize=[6,3])
        plt.plot(n_list, operations)
        
        if reference_curves:
            for label, curve in reference_curves.items():
                plt.plot(n_list, curve, '--', label=label)
            plt.legend(loc='upper left')
            
        plt.xlabel('Size')
        plt.ylabel('Operations')
        plt.title(title)
        plt.yscale(yscale)
        if ymax:
            plt.ylim(0, ymax)
        
        plt.show()

    @staticmethod
    def generate_reference_curves(n_list, num_curves=3):
        """Generate common complexity reference curves."""

        res = {}
        if num_curves >= 1:
            res['O(n)'] = [1.0 * n for n in n_list]
        if num_curves >= 2:
            res['O(n log n)'] = [n * np.log10(n) for n in n_list]
        if num_curves >= 3:
            res['O(n²)'] = [np.float_power(n, 2.0) for n in n_list]
        if num_curves >= 4:
            res['O(2^n)'] = [np.float_power(2.0, n) for n in n_list]

        return res
    

class DataGenerator:
    @staticmethod
    def create_dataset(size=10, data_type='random'):
        """Generate dataset for sorting algorithms.
        
        Args:
            size: Number of elements
            data_type: 'sorted', 'reverse', 'random'
        """
        if data_type == 'sorted':
            return np.linspace(1, size, size).tolist()
        elif data_type == 'reverse':
            return np.linspace(size, 1, size).tolist()
        else:
            return (np.trunc(np.absolute(size*10/2.0 + size*10/5.0*np.random.randn(size)))/10).tolist()
