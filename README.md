# Mutiband-HIFIGAN

An implementation of HIFIGAN with muit-band.

This project is based on:
1. Offical implementation of [HIFI-GAN](https://github.com/jik876/hifi-gan) by jik876
2. Unoffical implementation of [ParallelWaveGAN](https://github.com/kan-bayashi/ParallelWaveGAN) by kan-bayashi

- Support different datasets
- Support muti-band
- Support different sample_rate, hop_size ...

Current traning...

First, the data structure like below.

    datasets:
        wavs:
            speaker1:
                ???.wav
            speaker2:
                ???.wav
            ..... 

Second, create training.txt 
    
    python preprocess.py
    
Thirdly, training
    
    python train.py

