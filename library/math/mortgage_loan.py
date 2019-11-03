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

    # converts the rate
    def __fix_rate(self):
        return self.r / 12

    def per(self):
        return np.arange(1 * self.t) + 1

    def ipmt(self):
        return np.ipmt(self.r / 12, self.per(), 1 * self.t, self.p)

    def ppmt(self):
        return np.ppmt(self.r / 12, self.per(), 1 * self.t, self.p)

    def pmt_data(self):
        graph_data = []
        for payment in self.per():
            graph_data.append(payment)

        return graph_data

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

    def pmt_schedule(self):
        fmt = '{0:2d}  {1:8.2f}  {2:8.2f}  Principal: {3:8.2f}'

        for payment in self.per():
            index = payment - 1
            principal = self.p + self.ppmt()[index]
            print(fmt.format(payment, self.ppmt()[index], self.ipmt()[index], principal))

        return self.build_bar_graph()

    def get_payment(self):
        return np.pmt(self.r / 12, self.per(), 1 * self.t, self.p)

    def get_interest(self):
        return np.ipmt(self.r / 12, self.per(), 1 * self.t, self.p)

    def get_other(self):
        return np.ppmt(self.r / 12, self.per(), 1 * self.t, self.p)

    def results(self):
        fmt = '{0:2d} {1:8.2f} {2:8.2f} {3:8.2f}'
        per = np.arange(1 * self.t) + 1
        ppmt = np.ppmt(self.r / 12, self.per(), 1 * self.t, self.p)
        ipmt = np.ipmt(self.r / 12, self.per(), 1 * self.t, self.p)
        pmt = np.pmt(self.r / 12, 1 * self.t, self.p)
        it_principal = self.p
        if not np.allclose(ipmt + ppmt, pmt):
            raise Exception("These don\'t match")
        else:
            for payment in per:
                index = payment - 1
                principal = it_principal + ppmt[index]
                print(fmt.format(payment, ppmt[index], ipmt[index], principal))


test_rate = 0.0824
test_months = 12
test_principal = 2500

testMath = MortgageLoan(test_rate, test_months, test_principal)
