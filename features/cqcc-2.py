from scipy.io.wavfile import read
from spafe.features.cqcc import cqcc
from spafe.utils.vis import show_features

# read audio
fpath = "../../../test.wav"
fs, sig = read(fpath)

# compute cqccs
cqccs  = cqcc(sig,
              fs=fs,
              pre_emph=1,
              pre_emph_coeff=0.97,
              win_len=0.030,
              win_hop=0.015,
              win_type="hamming",
              nfft=2048,
              low_freq=0,
              high_freq=fs/2,
              normalize="mvn")

# visualize features
show_features(cqccs, "Constant Q-Transform Cepstral Coefﬁcients", "CQCC Index", "Frame Index")