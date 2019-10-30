import numpy as np
import matplotlib.pyplot as plt

rate = 0.075/12
months = 12 * 15
principal = 200000

np.pmt(rate, months, principal)
