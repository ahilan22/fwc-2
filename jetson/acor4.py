
# Our data set 
data = [3, 16, 156, 47, 246, 176, 233, 140, 130, 
        101, 166, 201, 200, 116, 118, 247, 
        209, 52, 153, 232, 128, 27, 192, 168, 208, 
        187, 228, 86, 30, 151, 18, 254, 
        76, 112, 67, 244, 179, 150, 89, 49, 83, 147, 90, 
        33, 6, 158, 80, 35, 186, 127]

# Delay (lag) range that we are interesting in
lags = range(10)

''' Fourier transform implementation '''

import numpy

# Nearest size with power of 2
size = 2 ** numpy.ceil(numpy.log2(2*len(data) - 1)).astype('int')

# Variance
var = numpy.var(data)

# Normalized data
ndata = data - numpy.mean(data)

# Compute the FFT
fft = numpy.fft.fft(ndata, size)

# Get the power spectrum
pwr = numpy.abs(fft) ** 2

# Calculate the autocorrelation from inverse FFT of the power spectrum
acorr = numpy.fft.ifft(pwr).real / var / len(data)
print(acorr)
