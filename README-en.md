# Anime face dataset

## Introduction

This is a dataset of cartoon avatars. All pictures come from <http://konachan.net/post/> and <https://wallhaven.cc/>

Crawl a total of 32151 Ultra HD pictures (22.7gb) and use [GitHub animation face detection](https://github.com/nagadomi/lbpcascade_animeface) to collect all animation avatars

In addition to automatic recognition, I also **manually** select for three times, actually it's a little tired~

- Eliminate some low quality pictures and low resolution pictures

- Eliminate some repeated pictures

- Eliminate pictures with strange saturation, contrast and brightness

- Eliminate some other strange pictures which I don't like

## Dataset Characteristics

- The total number of pictures is, and the size of all pictures is **256x256**

- Single leaflet (it is well known that girls like to paste)

- Most of the pictures only contain **forward faces**

- Most of the pictures only contain **hair and faces**

- The corresponding position resolution of most of the original images is higher than 256x256

- Most of the color gamut is normal and will not be too bright or too dark

This project adopts MIT protocol, which can be downloaded and used by yourself. If it's helpful to you, please :star: star :star: this repo, thank you. It's worth sifting it manually for several times

## Part of dataset images

![20220511181820](https://raw.githubusercontent.com/learner-lu/picbed/master/20220511181820.png)

![20220511181849](https://raw.githubusercontent.com/learner-lu/picbed/master/20220511181849.png)

![20220511181933](https://raw.githubusercontent.com/learner-lu/picbed/master/20220511181933.png)

![20220511182000](https://raw.githubusercontent.com/learner-lu/picbed/master/20220511182000.png)

## Other related dataset

- [6w,96x96,well](https://github.com/bchao1/Anime-Face-Dataset)
- [5w,96x96,nice](https://github.com/luzhixing12345/Anime-WGAN/releases/download/v0.0.2/faces.zip)
- [14w,512x512,high quality!!!](https://www.kaggle.com/datasets/lukexng/animefaces-512x512)

## Other related GAN work

- [use WGAN to generate anime faces](https://github.com/luzhixing12345/Anime-WGAN)
- [use DCGAN to generate anime faces](https://github.com/jayleicn/animeGAN)
- [DCGAN+styleGan3 to generate anime faces](https://github.com/xiaoyou-bilibili/anime_avatar_gen)