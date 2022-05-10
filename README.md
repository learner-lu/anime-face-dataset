# Anime face dataset

[English-README](README-en.md)

## 简介

这是一个动漫头像的数据集,所有图片来源于 <http://konachan.net/post/>

爬取总计32151张超高清图片(22.7GB),使用[Github-动漫人脸检测](https://github.com/nagadomi/lbpcascade_animeface)搜集了所有动漫头像

图片总量为,所有图片大小为 **256x256**

除自动识别外我**手动过了一遍**,剔除了一些低质量的图片和低分辨率的图片,剔除了一些多次重复的图片

本项目采用 MIT 协议,可自行下载使用. 如果对你有所帮助麻烦本仓库点个star谢谢,不枉我人眼筛一遍:+1:

## 数据集部分图片

## [数据集下载地址](123)

> 如果下载速度过慢可以使用[Github proxy](https://ghproxy.com/)加速

## 相关内容

- [Github-动漫头像数据集](https://github.com/bchao1/Anime-Face-Dataset)
- [另一个数据集,96x96,5w张](123)
- [Github-使用WGAN生成动漫头像](https://github.com/luzhixing12345/Anime-WGAN)
- [Github-使用DCGAN生成动漫头像](https://github.com/jayleicn/animeGAN)

## 爬虫和人脸检测的使用方法

- 安装依赖

  ```bash
  pip install -r requirements.txt
  ```

- 爬取图片

  ```bash
  python spider.py
  ```

  > 默认线程数 100, python中的GIL对于IO密集的程序,多线程是要比单线程快的

- 动漫头像识别保存

  ```bash
  python anime_face_detect.py
  ```
