# Anime face dataset

[English-README](README-en.md)

## [数据集下载地址](https://github.com/luzhixing12345/anime-face-dataset/releases/download/v0.0.1/anime256.zip)

> 如果下载速度过慢可以使用[Github proxy](https://ghproxy.com/)加速

解压后文件名为 `anime256`

## 简介

这是一个动漫头像的数据集,所有图片来源于 <http://konachan.net/post/> 和 <https://wallhaven.cc/>

使用[Github-动漫人脸检测](https://github.com/nagadomi/lbpcascade_animeface)搜集了所有动漫头像

除自动识别外我**手动过了三遍**,还是挺累的

- 剔除了一些低质量的图片和低分辨率的图片
- 剔除了一些多次重复的图片
- 剔除了饱和度,对比度,亮度奇怪的图片
- 剔除了其他的一些奇奇怪怪的图片,和一些我不喜欢的图片

## 数据集特点

- 图片总量为27588,所有图片大小为 **256x256**
- 单人单张,图片名没有任何意义
- 绝大部分图片为**正脸**
- 绝大部分图片为**脸部**,不漏肩部及以下
- 绝大部分图片原图对应位置分辨率高于256x256
- 绝大部分色域正常,不会过亮过暗

本项目采用 MIT 协议,可自行下载使用. 如果对你有所帮助请给本仓库点个:star: star :star:谢谢,不枉我手动筛了几遍

## 数据集部分图片

![20220511181820](https://raw.githubusercontent.com/learner-lu/picbed/master/20220511181820.png)

![20220511181849](https://raw.githubusercontent.com/learner-lu/picbed/master/20220511181849.png)

![20220511181933](https://raw.githubusercontent.com/learner-lu/picbed/master/20220511181933.png)

![20220511182000](https://raw.githubusercontent.com/learner-lu/picbed/master/20220511182000.png)

## 相关其他数据集

- [6w,96x96,质量不是特别好](https://github.com/bchao1/Anime-Face-Dataset)
- [5w,96x96,质量不错](https://github.com/luzhixing12345/Anime-WGAN/releases/download/v0.0.2/faces.zip)
- [14w,512x512,质量超高](https://www.kaggle.com/datasets/lukexng/animefaces-512x512)

## 相关GAN项目

- [WGAN生成动漫头像](https://github.com/luzhixing12345/Anime-WGAN) - (我的,厚脸皮推一下)
- [DCGAN生成动漫头像](https://github.com/jayleicn/animeGAN)
- [DCGAN+styleGan3](https://github.com/xiaoyou-bilibili/anime_avatar_gen)
