这里提供一下autosub库的安装包
==============================
###1.其他版本的可能会有问题，请使用我这个版本安装<br>
###2.你所在的IP是国内，或者是香港，对普通话识别会有问题（香港会理解你在说粤语，国内ip是无法执行的，所以，请使用其他国家的ip地址，我测试德国ip一切正常）<br>
###3.识别的准确率是根据你的普通话标准程度决定的，处理完毕还希望能自行校验一下。<br>
###4.如果想得到相关翻译字幕，请提供Google API的密钥<br>
例如：<br>
  中文转英文<br>
  autosub -S zh-CN -D en -K AIzaSyAzs***************************2Bs -F srt 1.mp3<br>
  英文转中文<br>
  autosub -S en -D zh-CN -K AIzaSyAzs***************************2Bs -F srt 1.mp3<br>

###5.最好提交的是mp3文件，这样速度会快一些，当然mp4也是可以识别的。<br>
  mp4例子：<br>
  autosub -F srt -S zh-CN -D zh-CN video.mp4<br>
  mp3例子：<br>
  autosub -F srt -S zh-CN -D zh-CN 1.mp3<br>

###6.安装autosub库<br>
  在库对应的路径，运行<br>
  python setup.py 即可<br>
  或者pip install ./<br>
<br>
