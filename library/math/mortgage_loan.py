import numpy as np
import matplotlib.pyplot as plt
import locale
plt.rcdefaults()


class MortgageLoan:

    def __init__(self, rate, time, principal):
        self.r = rate
        self.t = time
        self.p = principal
        self.calculations = []

    def currency_formatting(self):
        pass

    # converts the rate
    def __fix_rate(self):
        return self.r / 12

    def __per(self):
        return np.arange(1 * self.t) + 1

    def __ipmt(self):
        return np.ipmt(self.r/12, self.__per(), 1 * self.t, self.p)

    def __ppmt(self):
        return np.ppmt(self.r/12, self.__per(), 1 * self.t, self.p)

    def pmt_data(self):
        graph_data = []
        for payment in self.__per():
            graph_data.append(payment)

        return graph_data

    def pmt_schedule(self):
        fmt = '{0:2d} {1:8.2f} {2:8.2f} {3:8.2f}'

        for payment in self.__per():
            index = payment - 1
            principal = self.p + self.__ppmt()[index]
            print(fmt.format(payment, self.__ppmt()[index], self.__ipmt()[index], principal))

    def build_bar_graph(self):
        months = self.pmt_data()
        y_pos = np.arange(len(months))
        payments = self.pmt_data()
        # labels = ["label%d" % i for i in range(len(payments))]

        # graph setup
        plt.bar(y_pos, payments, align='center', alpha=0.5)
        plt.xticks(y_pos, months)
        plt.ylabel('Months')
        plt.title('Mortgage Loan Payment Schedule')
        plt.show()

    def get_math_data(self):
        pass
