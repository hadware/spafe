import scipy.signal as sg
import numpy as np
import scipy.io.wavfile
import matplotlib.pyplot as plt
import spafe.utils.processing as proc


def visualize(mat, ylabel, xlabel):
    plt.imshow(mat, origin='lower', aspect='auto', interpolation='nearest')
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.show()

def plot(y, ylabel, xlabel):
    plt.plot(y)
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    plt.show()
    
def padding_factor(vec, j):
    s = vec.shape[0] // j  + 1
    f = np.abs(s * j - vec.shape[0]) 
    return s, f 


#read wave file 
fs, sig = scipy.io.wavfile.read('../test.wav')

# plot spectogram 
plt.specgram(sig, NFFT=512, Fs=fs)
plt.ylabel("Frequency (kHz)")
plt.xlabel("Time (s)")
plt.show()


from spafe.features.mfcc import mfcc, imfcc, mfe
# compute mfccs and mfes
mfccs  = mfcc(sig, 13)
imfccs = imfcc(sig, 13)
mfes   = mfe(sig, fs) 

visualize(mfccs, 'MFCC Coefficient Index','Frame Index')
visualize(imfccs, 'IMFCC Coefficient Index','Frame Index')
visualize((np.append(mfes, 0)).reshape(277,13),  'MFE Coefficient Index','Frame Index')


from spafe.features.lfcc import lfcc
# compute mfccs and mfes
lfccs = lfcc(sig, 13)
visualize(lfccs, 'LFCC Coefficient Index','Frame Index')


from spafe.features.gfcc import gfcc
# compute gfccs
gfccs = gfcc(sig, 13) 
visualize(gfccs, 'GFCC Coefficient Index','Frame Index')

from spafe.features.ngcc import ngcc
# compute gfccs
ngccs = ngcc(sig, 13) 
visualize(ngccs, 'NGC Coefficient Index','Frame Index')


from spafe.features.bfcc import bfcc
# compute bfccs
bfccs = bfcc(sig, 13)
visualize(bfccs, 'BFCC Coefficient Index','Frame Index')

from spafe.features.pncc import pncc
# compute bfccs
pnccs = pncc(sig, 13)
visualize(pnccs, 'pnccs Coefficient Index','Frame Index')



from spafe.features.cqcc import cqcc
# compute bfccs
cqccs= cqcc(sig, 13)
plot(cqccs, 'CQC Coefficient Index','Frame Index')




from spafe.features.plp import plp
# compute bfccs
plps = plp(sig, 13)
visualize(plps, 'PLP Coefficient Index','Frame Index')

from spafe.features.rplp import rplp
# compute bfccs
rplps = rplp(sig, 13)
visualize(rplps, 'RPLP Coefficient Index','Frame Index')



from spafe.features.lpc import lpc
from spafe.features.lsp import lsp
# compute lpcs and lsps
lpcs = lpc(sig, 1)

visualize(lpcs, 'LPC Coefficient Index','Frame Index')

lsps = lsp(lpcs)
visualize(lsps, 'LSP Coefficient Index','Frame Index')