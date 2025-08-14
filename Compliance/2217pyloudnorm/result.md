Files downloaded from https://github.com/csteinmetz1/pyloudnorm/tree/master/tests/data  
to compare with the results of pyloudnorm  
  
Results as not supported were problem of file's metadata.  
They didn't have the metadata implying 'Microsoft PCM'  

| File | target | Result with ./BS1770 | Result with PyLoudNorm |
|------|--------|--------|--------|
| 1770-2_Comp_23LKFS_1000Hz_2ch.wav | -23 | -22.993305005064524. | -23.03 |
| 1770-2_Comp_23LKFS_100Hz_2ch.wav | -23 | -22.99345290978285. | -23.03 |
| 1770-2_Comp_23LKFS_2000Hz_2ch.wav |-23 | -22.992263252995311. | -23.03 |
| 1770-2_Conf_Mono_Voice+Music-24LKFS.wav | -24 | Not Supported | -24.03 |
| 1770-2_Comp_AbsGateTest.wav | -69.5 | -71.459488600132914. | -69.49 |
| 1770-2_Comp_24LKFS_25Hz_2ch.wav | -24 | -23.993283512795077. | -24.00 |
| 1770-2_Comp_23LKFS_10000Hz_2ch.wav | -23 | -22.993176338263382. | -23.04 |
| 1770-2_Comp_24LKFS_500Hz_2ch.wav | -24 | -23.993116524736294. | -24.04 |
| 1770-2_Comp_18LKFS_FrequencySweep.wav | -18 | -17.990261729608196. | -18.03 |
| 1770-2_Comp_RelGateTest.wav | -10 | -10.028539500711215. | -10.07 |
| 1770-2_Conf_Stereo_VinL+R-23LKFS.wav | -23 | -22.978617374570145. | -23.02 |
| 1770-2_Comp_24LKFS_2000Hz_2ch.wav | -24 | -23.99321265840976. | -24.04 |
| 1770-2_Conf_Stereo_VinL+R-24LKFS.wav | -24 | Not Supported | -24.02 |
| 1770-2_Comp_23LKFS_500Hz_2ch.wav | -23 | -22.993370457389865. | -23.04 |
| 1770-2_Conf_Mono_Voice+Music-23LKFS.wav | -23 | -22.990346050143319. | -23.03 |
| 1770-2_Comp_24LKFS_1000Hz_2ch.wav | -24 | -23.993508739136871. | -24.04 |
| 1770-2_Comp_23LKFS_25Hz_2ch.wav | -23 | -22.993243603061071. | -23.00 |
| 1770-2_Comp_24LKFS_10000Hz_2ch.wav | -24 | -23.993423172102968. | -24.04 |
| 1770-2_Comp_24LKFS_100Hz_2ch.wav | -24 | -23.993387910656825. | -24.03 |

*'Not Supported' were problem of file's metadata.*  
*They didn't have the metadata implying 'Microsoft PCM'*  

