# Our data set 
import time
start_time = time.time()

data = [3, 16, 156, 47, 246, 176, 233, 140, 130, 
        101, 166, 201, 200, 116, 118, 247, 
        209, 52, 153, 232, 128, 27, 192, 168, 208, 
        187, 228, 86, 30, 151, 18, 254, 
        76, 112, 67, 244, 179, 150, 89, 49, 83, 147, 90, 
        33, 6, 158, 80, 35, 186, 127]

# Delay (lag) range that we are interesting in
lags = range(10)

''' numpy.correlate '''

import numpy

x = numpy.array(data) 

# Mean
mean = numpy.mean(data)

# Variance
var = numpy.var(data)

# Normalized data
ndata = data - mean

acorr = numpy.correlate(ndata, ndata, 'full')[len(ndata)-1:] 
acorr = acorr / var / len(ndata)
#print(acorr)
print("Execution Time: %s" % (time.time() - start_time))
