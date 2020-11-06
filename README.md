# Mutiband-HIFIGAN

**An Easy Implementation of HIFIGAN with muit-band.**

**This project is based on:**

- Offical implementation of [HIFI-GAN](https://github.com/jik876/hifi-gan) by jik876
- Unoffical implementation of [ParallelWaveGAN](https://github.com/kan-bayashi/ParallelWaveGAN) by kan-bayashi

**Something new**

- Support different datasets
- Support muti-band
- Support different sample_rate, hop_size ...

**Current Training...**

**Firstly**, the datasets structure like below.

    datasets:
        wavs:
            speaker1:
                ???.wav
            speaker2:
                ???.wav
            ..... 

**Secondly**, create training.txt 

    python preprocess.py

**Thirdly**, training
    
    python train.py

**Some problems**

while using pqmf merge four subbands(value between -1 and 1), value may greater than 1.0 and less than -1.0.
I think it may cause by PQMF filters (can't reconstruct perfectly)